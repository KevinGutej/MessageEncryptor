print("Welcome in Ceasar encryptor!")
print("Choose option")
print("1. Encrypt message")
print("2. Decrypt message")
choice = int(input())

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

if choice == 1:
    print("Give me txt file name:")
    fileName = input()
    print("Which shift?")
    shift = int(input())
    file = open(fileName)
    content = file.read()
    result = ceasarEncrypt(content, shift)
    print(result)
    file.close()
    outputFile = open('output.txt', 'w')
    outputFile.write(result)
    outputFile.close()

elif choice == 2:
    print("Give me txt file name:")
    fileName = input()
    print("Which shift?")
    shift = int(input())
    file = open(fileName)
    content = file.read()
    result = ceasarDecrypt(content, shift)
    print(result)

else:
    print("Invalid number")