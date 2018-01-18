import sys
import os
import getopt

if len(sys.argv[1:])<=1:  ### Indicates that there are insufficient number of command-line arguments
    print ("Warning! wrong command, please read the mannual in Readme.txt.")
    print ("Example: python lab_sub_pos.py --input_psm PSM_filename --output output_filename")
else:
    options, remainder = getopt.getopt(sys.argv[1:],'', ['input_psm=','nsSNPdb=','output='])
    for opt, arg in options:
        if opt == '--input_psm': input_file=arg
        elif opt == '--nsSNPdb': snp_db=arg
        elif opt == '--output': output_file=arg
        else:
            print ("Warning! Command-line argument: %s not recognized. Exiting...") % opt; sys.exit()


handle= SeqIO.parse(snp_db,"fasta")
db_dic={}
for record in handle:
    db_dic[record.description] = str(record.seq)

input1=open(input_file,"r") # novpep tab table

header= input1.strip().split("\t")
header += ["from.SNPdb"]

output=open(output_file,"w") # output table

print ("searching SNPdb to see if any novel peptides derived from nsSNPs")
for line in input1:
    row=line.strip().split("\t")
    pep = row[0]
    
    query_output = ""
    for pro in db_dic:
        if pep in db_dic[pro]:
            query_output=pro
            break

    row.append(query_output)
    output.write("\t".join(row)+"\n")

input1.close()
output.close()
handle.close()

