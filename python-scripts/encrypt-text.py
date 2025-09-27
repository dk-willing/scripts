alphabets = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z", 
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
]

command = input("Type 'encode' to encrypt text or 'decode' to decrypt text: ").lower()


text = input("Type your message here: ").lower()
shift_num = int(input("Enter number of secret shift number: "))

# Encrypt function
def encrypt(message, key):
    cipher_text = "";
    for letter in text:
        if letter == " ":
            cipher_text += " "
        else:
            idx = alphabets.index(letter)
            new_idx = idx + shift_num
            cipher_text += alphabets[new_idx]
    print(f"The encrypted text is {cipher_text}")

def decrypt(message, key):
    decoded_text=""
    for letter in message:
        if letter == " ":
            decoded_text += " "
        else:
            idx = alphabets.index(letter)
            new_idx = idx - key
            decoded_text += alphabets[new_idx] 
    print(f"The decrypted text is {decoded_text}")

if command == "encode":
    encrypt(message=text, key=shift_num)
elif command == "decode":
    decrypt(message=text, key=shift_num)