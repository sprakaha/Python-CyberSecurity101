# parse the text file into a list 
# the below code saves 10,000 common English words into the list called validWords
f = open("Modules/Intro/PasswordValidation/valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()

print("Welcome to the Password Validator...\nI'll help you creat a strong password")

while True: 
    # prompt the user to set up a password
    password = input("Please enter your password: ")

    # intialize boolean for whether the password is strong or not
    valid = True

    # check if the password is an English word
    if password in validWords:
        print("Weak. This is a word in the dictionary.")
        valid = False

    # check that it is at least 8 charcters
    if len(password) < 8:
        print("Weak. This password is too short.")
        valid = False

    # check contents of the password
    special_characters = 0
    upper_case = 0 
    lower_case = 0
    nums = 0
    for char in password: 
        if ord(char) >= 65 and ord(char) <= 90:
            upper_case += 1
        elif ord(char) >= 97 and ord(char) <= 122:
            lower_case += 1
        elif ord(char) >= 32 and ord(char) <= 47:
            special_characters += 1
        elif ord(char) >= 48 and ord(char) <= 57:
            nums += 1

    # check that there are two special characters
    if special_characters < 2: 
        print("Weak. There are not enough special characters.")
        valid = False

    # check if there are two numbers 
    if nums < 2: 
        print("Weak. There are not enough numbers.")
        valid = False

    # check that there are at least one upper & one lower
    if upper_case < 1 and lower_case < 1:
        print("Weak. There needs to be an upper case & lower case letter.")
        valid = False

    # if none of the above conditions are correct, it is valid
    if valid:
        print("Strong. This is a good password.")
        break