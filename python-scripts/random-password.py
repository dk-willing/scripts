import random

alphabets = [
  "a","b","c","d","e","f","g","h","i","j","k","l","m",
  "n","o","p","q","r","s","t","u","v","w","x","y","z",
  "A","B","C","D","E","F","G","H","I","J","K","L","M",
  "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to Dev Qwecu's Random Password Generator😊")

# Gets users password preference
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password = []

# Gets random symbols and appends to the password list
for symbol in range(0, num_symbols):
    password.extend(random.choice(symbols))

# Gets random numbers and appends to the password list
for number in range(0, num_numbers):
    password.extend(random.choice(numbers))

# Gets random letters and appends to the password list
for alphabet in range(0, num_letters):
    password.extend(random.choice(alphabets))

# Shuffles/reorders the order of the password to make it more random
random.shuffle(password)
results = "".join(password)
print(results)





