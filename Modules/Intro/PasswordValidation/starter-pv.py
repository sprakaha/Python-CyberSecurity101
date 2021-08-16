
# parse the text file into a list 
# the below code saves 10,000 common English words into the list called validWords
f = open("Modules/Intro/PasswordValidation/valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()

# TODO: Repeatedly prompt the user for a password until they enter a strong password
# If there password is not strong, give reasoning as to why