## Strings Review

# strings are a list of characters 
# "hello" -> 'h', 'e', 'l', 'l', 'o'

greeting = "Hello! How are you?"

# Get first character of a string
# print(greeting[0])

# Get last character of a string
# print(greeting[len(greeting) - 1])
# print(greeting[len(greeting)]) # this will give an error - IndexError

# Get the middle character of a string
mid = int((len(greeting) - 1) / 2)
# print(greeting[mid])
# print(len(greeting))

# Pig latin 
# e.g. hello ->  ellohay
test1 = "book"
output = ""
output2 = ""

# for loop way
for i in range(1, len(test1)):
    output += test1[i]
output += test1[0] + "ay" # concatenation 
# print(output)

# Pythonic - special to Python! 
output2 += test1[1:] + test1[0] + "ay"
# print(output2)

## Password Validation Review

# Get user input
password = input("Enter the password you want: ")

uppercase_letters = 0
lowercase_letters = 0

# Loop over EACH character in the string 
for i in range(len(password)):
    current = password[i]
    # Count numbers, special characters, if in the words, etc...
    # UPPER CASE is between - 65 to 90
    # LOWER CASE is between - 97 to 122
    if ord(current) >= 65 and ord(current) <= 90:  # check if the character is uppercase ord() 
        uppercase_letters += 1
    if ord(current) >= 97 and ord(current) <= 122:
        lowercase_letters += 1
print("upper case count: ",uppercase_letters)
print("lower case count: ", lowercase_letters)

# Conditional to check if our rules are broken 
if uppercase_letters < 1:
    print("Not enough Upper case letters!")
if lowercase_letters < 1:
    print("Not enough lower case letters!")

## Ciphers 

# an algorithm for performing encryption or decryption
# algorithm is a series of well-defined steps that can be followed as a procedure
# deterministic! - following the same procedure always gets the same results

# What are some ideas for encrypting data you have?

# numeric cipher (alpha -> ASCII)
message = "the battle will start at eight"
print("Encrypted")
for i in range(len(message)):
    print(str(ord(message[i])) + " ", end = "")
print("")

print("Decrypted: ")
encrypted = "116 104 101 32 98 97 116 116 108 101 32 119 105 108 108 32 115 116 97 114 116 32 97 116 32 101 105 103 104 116"
words = encrypted.split(" ")
for w in words:
    print(chr(int(w)), end="")

print("")
