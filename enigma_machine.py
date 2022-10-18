alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
plugboard = alphabet[:]
#rotor1 = "PEZUOHXSCVFMTBGLRINQJWAYDK"
#rotor2 = "ZOUESYDKFWPCIQXHMVBLGNJRAT"
#rotor3 = "EHRVXGAOBQUSIMZFLYNWKTPDJC"

rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

rotor1_pointer = 1
rotor2_pointer = 1
rotor3_pointer = 1

#reflector = "IMETCGFRAYSQBZXWLHKDVUPOJN"
reflector = "EJMZALYXVBWFCRQUONTSPIKHGD"
plugboardPairs = {"AR" , "GK" , "OX"}

def createPlugboard():
    global plugboard
    
    for pair in plugboardPairs:
        letter1 = pair[0]
        letter2 = pair[1]

        index1 = alphabet.index(letter1)
        index2 = alphabet.index(letter2)
    
        plugboard[index1] = alphabet[index2]
        plugboard[index2] = alphabet[index1]
    #del letter1, letter2 , pair, index1, index2
    #enigmaMachine(plugboard2)
    
def turnRotors(index , pointer):
    for counter in range (0 , pointer):
        index = index + 1
        if index >= 26:
            index = 0

    #print(index , ' ' ,  pointer)
    return index

def enigmaMachine(message):
    global rotor1_pointer
    global rotor2_pointer 
    global rotor3_pointer
    #print(plugboard)
    word = ''
    for i in message:
       
        if rotor3_pointer >= 27: 
            rotor3_pointer = 1
            rotor2_pointer = rotor2_pointer + 1

        if rotor2_pointer >= 27:
            rotor2_pointer = 1
            rotor1_pointer = rotor1_pointer + 1

        if rotor1_pointer >= 27: 
            rotor1_pointer = 1
        #print(rotor1_pointer , ' ' , rotor2_pointer , ' ' , rotor3_pointer)

        char = i.capitalize()
        letterIndex = plugboard.index(char) #7
        
        index = turnRotors(letterIndex,rotor3_pointer-1)
        letter = rotor3[index]
        letterIndex = alphabet.index(letter)
        #print(letter)

        index = turnRotors(letterIndex,rotor2_pointer-1)
        letter = rotor2[index]
        letterIndex = alphabet.index(letter)
        #print(letter)

        index = turnRotors(letterIndex,rotor1_pointer-1)
        letter = rotor1[index ]
        letterIndex = alphabet.index(letter)
        #print(letter)

        letter = reflector[letterIndex]            #reflect
        letterIndex = alphabet.index(letter)
        #print(letter)

        index = turnRotors(letterIndex,rotor1_pointer-1)
        letter = alphabet[index]
        letterIndex = rotor1.index(letter)
        #print(letter)

        index = turnRotors(letterIndex,rotor2_pointer-1)
        letter = alphabet[index]
        letterIndex = rotor2.index(letter)
        #print(letter)

        index = turnRotors(letterIndex,rotor3_pointer-1)
        letter = alphabet[index]
        letterIndex = rotor3.index(letter)
        #print(letter)
        
        letter = plugboard[letterIndex]
        word = word + letter
        #rotor3_pointer = rotor3_pointer + 1
    print('your word is ' + word)    
        

#print(alphabet.index(letter1))
#print(plugboard[alphabet.index(letter1)])


if __name__ == '__main__':
    print("please input a message with no spaces, numbers or special characters")
    input1 = input()
    createPlugboard()
    enigmaMachine(input1)
