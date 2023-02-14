# %% Dictionary for DNA
def DNA_dic_code(a):
    if a == "a": return "AAA"
    if a == "b": return "AAC"
    if a == "c": return "AAG"
    if a == "d": return "AAT"
    if a == "e": return "ACA"
    if a == "f": return "ACC"
    if a == "g": return "ACG"
    if a == "h": return "ACT"
    if a == "i": return "AGA"
    if a == "j": return "AGC"
    if a == "k": return "AGG"
    if a == "l": return "AGT"
    if a == "m": return "ATA"
    if a == "n": return "ATC"
    if a == "o": return "ATG"
    if a == "p": return "ATT"
    if a == "q": return "CAA"
    if a == "r": return "CAC"
    if a == "s": return "CAG"
    if a == "t": return "CAT"
    if a == "u": return "CCA"
    if a == "v": return "CCC"
    if a == "W": return "CCG"    
    if a == "x": return "CCT"    
    if a == "y": return "CGA"    
    if a == "z": return "CGC"    
    if a == "A": return "CGG"    
    if a == "B": return "CGT"    
    if a == "C": return "CTA"    
    if a == "D": return "CTC"    
    if a == "E": return "CTG"    
    if a == "F": return "CTT"    
    if a == "G": return "GAA"    
    if a == "H": return "GAC"    
    if a == "I": return "GAG"    
    if a == "J": return "GAT"    
    if a == "K": return "GCA"    
    if a == "L": return "GCC"    
    if a == "M": return "GCG"    
    if a == "N": return "GCT"    
    if a == "O": return "GGA"    
    if a == "P": return "GGC"    
    if a == "Q": return "GGG"    
    if a == "R": return "GGT"    
    if a == "S": return "GTA"    
    if a == "T": return "GTC"    
    if a == "U": return "GTG"    
    if a == "V": return "GTT"    
    if a == "W": return "TAA"    
    if a == "X": return "TAC"    
    if a == "Y": return "TAG"    
    if a == "Z": return "TAT"    
    if a == "1": return "TCA"    
    if a == "2": return "TCC"    
    if a == "3": return "TCG"    
    if a == "4": return "TCT"    
    if a == "5": return "TGA"    
    if a == "6": return "TGC"    
    if a == "7": return "TGG"    
    if a == "8": return "TGT"    
    if a == "9": return "TTA"    
    if a == "0": return "TTC"    
    if a == " ": return "TTG"    
    if a == ".": return "TTT"

def DNA_dic_decode(a):
    if a == "AAA": return "a"
    if a == "AAC": return "b"
    if a == "AAG": return "c"
    if a == "AAT": return "D"
    if a == "ACA": return "e"
    if a == "ACC": return "f"
    if a == "ACG": return "g"
    if a == "ACT": return "h"
    if a == "AGA": return "i"
    if a == "AGC": return "j"
    if a == "AGG": return "k"
    if a == "AGT": return "l"
    if a == "ATA": return "m"
    if a == "ATC": return "n"
    if a == "ATG": return "o"
    if a == "ATT": return "p"
    if a == "CAA": return "q"
    if a == "CAC": return "r"
    if a == "CAG": return "S"
    if a == "CAT": return "t"
    if a == "CCA": return "u"
    if a == "CCC": return "v"
    if a == "CCG": return "w"    
    if a == "CCT": return "x"    
    if a == "CGA": return "y"    
    if a == "CGC": return "z"    
    if a == "CGG": return "A"    
    if a == "CGT": return "B"    
    if a == "CTA": return "C"    
    if a == "CTC": return "D"    
    if a == "CTG": return "E"    
    if a == "CTT": return "F"    
    if a == "GAA": return "G"    
    if a == "GAC": return "H"    
    if a == "GAG": return "I"    
    if a == "GAT": return "J"    
    if a == "GCA": return "K"    
    if a == "GCC": return "L"    
    if a == "GCG": return "M"    
    if a == "GCT": return "N"    
    if a == "GGA": return "O"    
    if a == "GGC": return "P"    
    if a == "GGG": return "Q"    
    if a == "GGT": return "R"    
    if a == "GTA": return "S"    
    if a == "GTC": return "T"    
    if a == "GTG": return "U"    
    if a == "GTT": return "V"    
    if a == "TAA": return "W"    
    if a == "TAC": return "X"    
    if a == "TAG": return "Y"    
    if a == "TAT": return "Z"    
    if a == "TCA": return "1"    
    if a == "TCC": return "2"    
    if a == "TCG": return "3"    
    if a == "TCT": return "4"    
    if a == "TGA": return "5"    
    if a == "TGC": return "6"    
    if a == "TGG": return "7"    
    if a == "TGT": return "8"    
    if a == "TTA": return "9"    
    if a == "TTC": return "0"    
    if a == "TTG": return ""    
    if a == "TTT": return "."