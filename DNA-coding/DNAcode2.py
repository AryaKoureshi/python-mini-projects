from DNADic import DNA_dic
from DNA180 import Dna2
from DNAexept35 import Dna3
import math
Dna = "AGTCGATGCATGCTAATAAAGACGTCTTCCTCACCCAACTGTCTCAAAGCCTCTTAACCCCGGAGCGGTAACTCGTTTCACAGATCG"
dnastr = ""
DNA_decode = ""
w = 0
while w in range(len(Dna2)) and w+2 < len(Dna2):
    dnastr += Dna2[w]
    dnastr += Dna2[w+1]
    dnastr += Dna2[w+2]
    DNA_decode += DNA_dic(dnastr)
    w += 3
    dnastr = ""
print(DNA_decode)