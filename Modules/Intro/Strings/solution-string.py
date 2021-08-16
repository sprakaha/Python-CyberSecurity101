### LOOPS & STRINGS 

# ask the user to enter a single word. save this as a string
word = input("Enter a single word: ")

# 1. using a for loop print out every letter in the string 
for w in word: 
    print(w)

# 2. using a while looop print out every other letter in the string 
x = 0 
while x < len(word):
    print(word[x])
    x += 2

# 3. using a for loop print out the word backwards
backwards = ""
for i in range(len(word) - 1, -1, -1):
    backwards += word[i]
print(backwards)

# 4. using a for loop print out the ASCII value of each letter in the string
for w in word: 
    print(ord(w))

## PYTHON STRING INDEXING 

# ask the user to enter a sentence that is at least 20 characters. save this as a string 
sentence = input("Enter a single sentence: ")
while len(sentence) < 20: 
    sentence = input("Try again. Enter a longer sentence: ")

# 5. print out the last character WITHOUT using a loop
print(sentence[-1])

# 6. print out the last 4 characters WITHOUT using a loop
print(sentence[len(sentence) - 4:])

# 7. print out the first 10 characters WITHOUT using a loop 
print(sentence[:10])

# 8. check if the word that the user entered in step 1 exists in the sentence they entered. 
if word in sentence: 
    print("The word you entered is in the sentence.")
else: 
    print("The word you entered is not in the sentence.")


