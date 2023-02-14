# %% Imports
from DNA_dic import DNA_dic_code, DNA_dic_decode
from DNA180 import Dna2
# %% Initializations
#DNA = "5AGTCGATGCATGCTAATAAAGACGTCTTCCTCACCCAACTGTCTCAAAGCCTCTTAACCCCGGAGCGGTAACTCGTTTCACAGATCG3"
dna = []
i = int(DNA[0])
k = int(DNA[-1])
c = 1
dnastr = ""
DNA_decode = ""
w = 0
# %% Find Code From DNA
while c == 1:
    while i != 88:
        dna.append(DNA[i])
        i += 5
        if i >= len(DNA)-1:
            i = i - len(DNA)
            if DNA[i] == "3":
                k = 3
                break
            if DNA[i] == "5":
                break
    while k != 0:
        dna.append(DNA[k])
        k -= 3
        if k <= 0:
            k = len(DNA) + k - 1
            if DNA[k] == "3":
                c = 0
                break
            if DNA[k] == "5":
                i = 5
                break
    #while k != 0:
     #   dna.append(DNA[k])
      #  k += 3
       # if k >= len(DNA)-1:
        #    k = k - len(DNA)
         #   if DNA[k] == "3":
          #      c = 0
           #     break
            #if DNA[k] == "5":
             #   i = 5
              #  break
# %% Decode
while w in range(len(dna)) and w+2 < len(dna):
    dnastr += dna[w]
    dnastr += dna[w+1]
    dnastr += dna[w+2]     
    DNA_decode += DNA_dic(dnastr)
    w += 3
    dnastr = ""
print(DNA_decode)