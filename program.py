#Get Choose Function
def getChoose():
    while True:
        print('\nWould you like to (E)ncrypt or (D)ecrypt?:')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

#Get Message
def getMessage():
    print('Enter your message:')
    return input()

#Get Key
def getKey():
    max_size = 26
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (max_size))
        key = input()
        if(key.isdigit()):
            key = int(key)
            if (key >= 1 and key <= max_size):
                return key

#Decide Action        
def decideActionAndRun(choose,text,key):
    val = ""
    if(choose[0] == "e"): 
        val = encryptMessage(message, key)
    else:
        val = decryptMessage(message, key)

    return val

#Encrypt Function
def encryptMessage(text, key):

    encryptMessageed = ""

    for c in text:
        # is upper
        if c.isupper(): #check if it's an uppercase character

            c_index = ord(c) - ord('A')

            # shift txhe current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encryptMessageed += c_new
            
        # is lower
        elif c.islower(): #check if its a lowecase character

            c_index = ord(c) - ord('a')

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encryptMessageed += c_new
            
        # is digit
        elif c.isdigit():

            c_new = (int(c) + key) % 10

            encryptMessageed += str(c_new)

        else:
            encryptMessageed += c

    return encryptMessageed

#Decrypt Function
def decryptMessage(text, key):

    decryptMessageed = ""

    for c in text:
        
        # is upper
        if c.isupper():

            c_index = ord(c) - ord('A')

            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decryptMessageed += c_og
            
        # is lower
        elif c.islower():

            c_index = ord(c) - ord('a')

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decryptMessageed += c_og
            
        # is digit
        elif c.isdigit():

            c_og = (int(c) - key) % 10
            
            decryptMessageed += str(c_og)

        else:
           decryptMessageed += c

    return decryptMessageed


while (1):
    
    choose = getChoose()
    message = getMessage()
    key = getKey()
    
    print('Your translated message is:')
    print(decideActionAndRun(choose,message,key))
