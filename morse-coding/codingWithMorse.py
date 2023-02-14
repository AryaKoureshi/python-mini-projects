from morse_dic import morse, demorse

def coding(word):
    morsed = ""
    for i in range(len(word)):
        trash = word[i]
        morsed += morse(trash) + "."
    return morsed

def decoding(code):
    demorsed = ""
    trash = ""
    i = 0
    while i < len(code) :
        if code[i] != "." :
            trash += code[i]
            if i+1 == len(code) : demorsed += demorse(trash)
        else :
            demorsed += demorse(trash)
            trash = ""
        i += 1
    return demorsed

print("What do you want?")
while True :
    a = input("Please enter the number ( 1.Code | 2.DeCode | 3.Exit ) : ")
    if a == "1" :
        print("Please dont use . char for coding!")
        word_inputed = input("Enter what do you every want : ")
        print(coding(word_inputed))
    elif a == "2" :
        morse_inputed = input("Enter Morse Coded your received : ")
        print(decoding(morse_inputed))
    elif a == "3" :
        break
    else :
        print("Don't use other char or word! Try again.")