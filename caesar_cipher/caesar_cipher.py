from caesar_cipher.corpus import name_list, word_list


def encrypt(text, shift):
    encrypted_text = ''
    for i in range(len(text)):
        if text[i] == ' ':
            encrypted_text = encrypted_text + text[i]
        elif text[i].isupper():
            encrypted_text = encrypted_text + chr((ord(text[i])+shift-65)%26+65)
        else:
            encrypted_text = encrypted_text + chr((ord(text[i])+shift-97)%26+97)
    return encrypted_text

def decrypt(encoded, shift):
    return encrypt(encoded, -shift)



def crack(encrypted_text):
    pass