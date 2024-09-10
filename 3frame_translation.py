#This Python script reads a FASTA file, extracts sequences, translates them into protein sequences based on the three possible reading frames (ORFs), and writes the translated sequences to an output file. It uses the Bio module from Biopython for handling sequence data. Here's a breakdown of the code:

import sys
from Bio import Seq,SeqIO
from Bio.Alphabet import IUPAC

handle=open(sys.argv[1],'r')
output=open(sys.argv[2],'w')

for record in SeqIO.parse(handle,'fasta'):
    seq=record.seq
    ORF1=seq.translate()
    ORF2=seq[1::].translate()
    ORF3=seq[2::].translate()
    
    if record.id=="":
        print(record.description, record.seq)
        continue
    output.write("%s\n%s\n" % ('>'+record.id+'_ORF1',ORF1))
    output.write("%s\n%s\n" % ('>'+record.id+'_ORF2',ORF2))
    output.write("%s\n%s\n" % ('>'+record.id+'_ORF3',ORF3))
            
handle.close()

output.close()
