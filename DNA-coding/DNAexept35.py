Dna = "AGTCGATGCATGCTAATAAAGACGTCTTCCTCACCCAACTGTCTCAAAGCCTCTTAACCCCGGAGCGGTAACTCGTTTCACAGATCG"
Dna3 = ""
i=0
while i < len(Dna):
    if ((i)%3 == 0 or (i+1)%5 == 0) :
        i+=1
    else:
        Dna3 += Dna[i]
        i +=1
Dna3+="G"
print(len(Dna3))