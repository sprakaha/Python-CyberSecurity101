## REVIEW ##

## Modulo - returns the remainder of division 
# % 
# 4 % 2 = 0
# 7 % 3 = 1
# 6 % 4 = 2 
# even nuumber - ALWAYS divisible by 2 
''' 
number = int(input("Enter a number: "))
# check if number is even
if number % 2 == 0:
    print("Even")
'''

## FUNCTIONS
# What is a function used for?
# e.g. f(x) = x^2 -> f(3) = 9 
# def function_name(a, b, c ...)

# Exercise 1 : Function to print out "hello" 5 times
def hello_5():
    for i in range(5):
        print("hello")

# hello_5()

# Exercise 2: Function to print out "hello" the number of times inputted if it is even, else - enter an even number
def hello_n(num):
    print(num)
    if num % 2 == 0:
        for i in range(num):
            print("hello")
    else:
        print("Please enter an even number.")

#number = int(input("Enter a number: "))
#hello_n(number)

## LOOPS & CONDITIONALS
# e.g. Linear Searching Algorithm 

### NEW CONCEPTS ##
# lots of different types of data, but in the end it all comes down to numbers
# numeric representations of data

## STRINGS

# Exercise 3: Get first & last character of a string
word1 = "hello"
print(word1[0])
print(word1[len(word1) - 1])

# Exercise 4: Get last 4 letters of a string

# Exercise 5: Function to convert a word into pig-latin
# Pig Latin - input: hello -> elloway 

## ASCII

# Convert letters to ASCII
print(ord('a')) # letter to number we use ord() 
print(chr(98)) # to go from number to letter we use chr() 

# Exercise 6: Convert a word into ASCII code
word = input("Enter a word: ")
for i in range(0, len(word)):
    print(ord(word[i]))

# Exercise 7: Count the number of upper case and lower case letters in a word
uppercase_count = 0
lowercase_count = 0 

word2 = input("Enter a word: ")
for i in range(0, len(word2)):
    # lowercase check 
    if ord(word2[i]) >= 97 and ord(word2[i]) <= 122: 
        lowercase_count += 1
    #  uppercase 
    if ord(word2[i]) >= 65 and ord(word2[i]) <= 90:
        uppercase_count +=1
print("Upper Case Letters: ", uppercase_count)
print("Lower Case Letters", lowercase_count)