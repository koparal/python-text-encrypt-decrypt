MAX_KEY_SIZE = 26
#Mode Function
def getMode():
    while True:
        print('Would you like to (E)ncrypt or (D)ecrypt?:')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

#Get Message From User
def getMessage():
    print('Enter your message:')
    return input()

#Get Message From Key
def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = input()
        if(key.isdigit()):
            key = int(key)
            if (key >= 1 and key <= MAX_KEY_SIZE):
                return key

#Decide Action        
def decideActionAndRun(mode,text,key):
    val = ""
    if(mode[0] == "e"):
        val = encryptMessage(message, key)
    else:
        val = decryptMessage(message, key)

    return val

#Encrypt Function
def encryptMessage(text, key):

    encryptMessageed = ""

    for c in text:

        if c.isupper(): #check if it's an uppercase character

            c_index = ord(c) - ord('A')

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encryptMessageed += c_new

        elif c.islower(): #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a')

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encryptMessageed += c_new

        elif c.isdigit():

            # if it's a number,shift its actual value
            c_new = (int(c) + key) % 10

            encryptMessageed += str(c_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encryptMessageed += c

    return encryptMessageed

#Decrypt Function
def decryptMessage(text, key):

    decryptMessageed = ""

    for c in text:

        if c.isupper():

            c_index = ord(c) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decryptMessageed += c_og

        elif c.islower():

            c_index = ord(c) - ord('a')

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decryptMessageed += c_og

        elif c.isdigit():

            # if it's a number,shift its actual value
            c_og = (int(c) - key) % 10

            decryptMessageed += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decryptMessageed += c

    return decryptMessageed


while (1):
    
    mode = getMode()
    message = getMessage()
    key = getKey()
    
    print('Your translated message is:')
    print(decideActionAndRun(mode,message,key))
