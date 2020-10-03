from Bio.Seq import Seq
import pandas as pd
import numpy as np
def pfm(alignment_sbjct, pro_seq):
    """
     Create Postion frequency matrix

     Input : Alignments match , Protein sequence

     Output : PFM matrix

    """

    protein_column = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N',
                      'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

    pfm_matrix = pd.DataFrame(np.zeros((len(pro_seq), len(protein_column))), columns=protein_column)

    seq_len = len(pro_seq)

    for amino in range(0, seq_len):

        for alignm in alignment_sbjct:

            if alignm[amino] in protein_column:
                pfm_matrix[alignm[amino]][amino] = pfm_matrix[alignm[amino]][amino] + 1

    return pfm_matrix
my_seq = Seq("DNLVLIRMKPDENGRFGFNVKGGYDQKMPVIVSRVAPGTPADLCVPRLNEGDQVVLINGRDIAEHTHDQVVLFIKASCERHSGELMLLVRPN")
print(len(my_seq))
for i in range(0, len(my_seq)):
    pfm_matrix = pfm(my_seq[i], my_seq[i])
#pssm = pwm.log_odds()
print(pfm_matrix)
