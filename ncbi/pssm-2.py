from Bio import AlignIO
from Bio.PDB import *
alignments = AlignIO.parse(open("Test.fasta"), "fasta")
print(alignments)
for alignment in alignments:
   print(alignment)