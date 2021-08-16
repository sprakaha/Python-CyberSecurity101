# DATA TYPES
# What is a data type?
# Which ones have we learned? 
let = 's' # character 
name = "Salena" # string - a list of characters

age = 5 # integers - whole numbers
height = 20.5 # double & floats are both decimal numbers 
print("Int: ", age)
print(float(age))
print(int(height))

# LOOPS
# What are loops? REPEAT!!
# What are the types? while & for 

# mini exercise 1: print out the numbers from 20 to 35 with a for loop
print("exercise 1")
for i in range(20, 35 + 1):
    print(i)

print("exercise 2")
# mini exercise 2: print out the first 10 multiples of 3 (e.g. 0, 3, 6, 9, 12, 15)
# 0 * 3 = 0, 1 * 3 = 3, 2 * 3 = 6, 3 * 3 = 9, 4 * 3 = 12
for i in range(0, 10):
    print(i * 3)

print("exercise 3")
# use a while loop when you have a CONDITION!
# print out the numbers from 20 to 35 with a while loop
x = 20 # init
while (x < 36): # have a condition that we check
    print(x)
    x = x + 1 # is the same as x += 1

print("exercise 4")
# want to use a while loop to reprompt the user to enter their password until it is correct
password = "password"
login = input("Enter your password: ")

# equals : ==
# not equals : != 

while (login != password): 
    login = input("Incorrect. Enter your password: ")

print("Congrats! You are logged in.") # code is read from top to bottom

# CONDITIONALS 

# What is a conditional used for? to check a condition 
# elif vs else if vs. if 

# print out if someone is an adult (older than 18) or not (younger than 18)
print("exercise 5")
age = input("Enter your age: ")
age = int(age)

if age >= 18:
    print("You are an adult")
else: # this captures age < 18 
    print("You are a child")

# add more conditions
print("exercise 6")
age = input("Enter your age: ")
age = int(age)

if age >= 18:
    print("You are an adult")
elif age >= 13 and age <= 17:
    print("You are a teen")
elif age >= 10 and age <= 12:
    print("You are a tween")
else: # else MUST be the last condition/line in the if/elif/else statements
    print("You are a child")
