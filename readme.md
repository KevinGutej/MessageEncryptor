<h1>Ceaser Cipher Code Breaker</h1> 

This program will allow you to under stand how to break Ceasers Ciphers code and how he used to communicate in the old times.




##Installation:
Use the link to download code(GitHub):
https://github.com/KevinGutej/MessageEncryptor

Here are your options:
```python
print("Message Encryptor")
print("1. Encrypt Message")
print("2. Decript Message")
```


Main Part of the code:
```python
if option == 1:
    message = open('test.txt')
    textmessage = message.read()
    encrypt
elif option == 2:

def encrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
        return result
# check the above function
text = "CEASER CIPHER DEMO"
s = 4

print
"Plain Text : " + text
print
"Shift pattern : " + str(s)
print
"Cipher: " + encrypt(text, s)
```

License(Please read if you are unsure of anything...)
[CLICK HERE!!](https://choosealicense.com/licenses/mit/)