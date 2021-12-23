
def encrypt(plain, key):
    encrypted_text = ""

    for i in range(len(plain)):
        char = plain[i]
        # Encrypt uppercase characters in plain text

        if (char.isupper()):
            encrypted_text += chr((ord(char) + key - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
    return encrypted_text


def decrypt(encoded, key):
    return encrypt(encoded, -key)