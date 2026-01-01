# Cypher Encryption and decryption program

import string, random
chars = " " +string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)




def main():
    is_running = True

    while is_running:
        type = input("Choose the type of cypher (Encryption or Decryption): E/D or Q to quit:")

        if type == 'E':
            encrypt_text()
        elif type == 'D':
            decrypt_text()
        elif type.lower() == 'q':
            is_running = False
            print("End of program!!")
        else:
            print("Choose correct type of cypher value. ")


def encrypt_text():

    input_text = input("Enter the text you want to encrypt: ")
    cypher_text = ""
    for letter in input_text:
        index = chars.index(letter)
        cypher_text += key[index]
    
    print(f"the encrypted message is: {cypher_text}")


def decrypt_text():

    input_text = input("Enter the text you want to decrypt: ")
    plain_text = ""
    for letter in input_text:
        index = key.index(letter)
        plain_text += chars[index]
    
    print(f"the original message after decryption is: {plain_text}")



if __name__ == "__main__":
    main()