from DNADic180 import DNA_dic_180
from DNAexept35 import Dna3
Dna = "AGTCGATGCATGCTAATAAAGACGTCTTCCTCACCCAACTGTCTCAAAGCCTCTTAACCCCGGAGCGGTAACTCGTTTCACAGATCG"
Dna2 = ""
dna4 = ""
for k in range(len(Dna)):
    dna4+=Dna[-k-1]
print(dna4)
for i in range(len(dna4)):
    Dna2 += DNA_dic_180(dna4[i])
print(Dna2)
