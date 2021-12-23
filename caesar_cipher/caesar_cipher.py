
def encrypt(plain, key):
    encrypted_text = ""

    for i in range(len(plain)):
        char = plain[i]
        # Encrypt uppercase characters in plain text

        if (char.isupper()):
            encrypted_text += chr((ord(char) + key-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
    return encrypted_text


def decrypt(encoded, key):
    return encrypt(encoded, -key)


# if __name__ == "__main__":
#     pins = [
#         "1234",
#         "9876",
#         "0000",
#         "9999",
#     ]

#     for pin in pins:
#         key = random.randint(1, 9)
#         print("plain pin", pin)
#         encrypted_pin = encrypt(pin, key)
#         print("encrypted_pin", encrypted_pin)
#         decrypted_pin = decrypt(encrypted_pin, key)
#         print("decrypted_pin", decrypted_pin)
