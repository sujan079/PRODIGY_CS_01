alphabets = 'abcdefghijklmnopqrstuvwxyz1234567890'
nAlphabets = len(alphabets)
def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == '':
            index = alphabets.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= nAlphabets:
                    new_index -= nAlphabets
                ciphertext += alphabets[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext =''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == '':
            index = alphabets.find(letter)
            if index == -1 :
                plaintext += letter
            else:
                new_index = index - key
                if new_index <0:
                    new_index += nAlphabets
                plaintext += alphabets[new_index]
    return plaintext

print()
print("**** CAESAR CIPHER PROGRAM ****")
print()


while True:
    print("Do you want to encrypt or decrypt?:e/d ")
    print("Enter 'q' to quit the program")
    user_input = input().lower()
    if user_input == "e":
        print("Encryption")
        key = int(input(f"Enter the key(number) from 1 to {nAlphabets-1} "))
        if key > nAlphabets-1:
            print('invalid Input')
            exit()
        text = input("Enter the the text you want to encrypt: ")
        print()
        print("Encrypting...")
        ciphertext = encrypt(text, key)
        print(f"Ciphertext:{ciphertext}")
    elif user_input == "d":
        print("**Decryption**")
        key = int(input(f"Enter the key(number) from 1 to {nAlphabets-1} :"))
        if key > nAlphabets-1:
            print('invalid Input')
            exit()
        text = input("Enter the the text you want to encrypt: ")
        print()
        print("Decrypting...")
        plaintext = decrypt(text, key)
        print(f"Plaintext:{plaintext}")
    elif user_input == "q":
        break
    else:
        print("invalid input, please try again")
