alphabets = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z", 
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
]

from art import logo

print(logo)

command = input("Type 'encode' to encrypt text or 'decode' to decrypt text: ").lower()


text = input("Type your message here: ").lower()
shift_num = int(input("Enter number of secret shift number: "))
shift_num = shift_num % 26

def ceaser(direction, start_text, key):
        end_text = ""        
        if direction == "decode":
                key *= -1
        for letter in start_text:
            if letter not in alphabets:
                end_text += letter
            else:
                position = alphabets.index(letter)
                new_position = position + key;
                end_text += alphabets[new_position]
        print(f"Your {direction}d is {end_text}")

ceaser(direction=command, start_text=text, key=shift_num)

user_input = input("Would you want to go again? Type 'yes' else 'no': ")

while user_input == "yes":
    command = input("Type 'encode' to encrypt text or 'decode' to decrypt text: ").lower()
    text = input("Type your message here: ").lower()
    shift_num = int(input("Enter number of secret shift number: "))
    shift_num = shift_num % 26
    ceaser(direction=command, start_text=text, key=shift_num)
    user_input = input("Would you want to go again? Type 'yes' else 'no': ")
    if user_input == "no":
        print("That was fun😊. Goodbye👋🏼")