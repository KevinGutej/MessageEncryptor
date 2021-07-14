
print("Message Encryptor")
print("1. Encrypt Message")
print("2. Decript Message")
option = int(input())


def ceasarEncrypt(message, shift):
    message = message.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alphabet:
            letter_index = (alphabet.find(letter) + shift) % len(alphabet)
            result = result + alphabet[letter_index]
        else:
            result = result + letter
    return result

def ceasarDecrypt(message, shift):
    message = message.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alphabet:
            letter_index = (alphabet.find(letter) - shift) % len(alphabet)
            result = result + alphabet[letter_index]
        else:
            result = result + letter
    return result

if option == 1:
    print("Give me txt file name:")
    filename = input()
    print("Give me shift")
    shift = int(input())
    message = open(filename)
    textmessage = message.read()
    print(textmessage)
    encrypt = ceasarEncrypt(textmessage, shift)
    print(encrypt)
    message.close()
    newfile = open("output.txt","w")
    newfile.write(encrypt)
    newfile.close()
elif option == 2:
    print("Give me txt file name:")
    filename = input()
    print("Give me shift")
    shift = int(input())
    message = open(filename)
    textmessage = message.read()
    print(textmessage)
    decrypt = ceasarDecrypt(textmessage, shift)
    print(decrypt)
    message.close()