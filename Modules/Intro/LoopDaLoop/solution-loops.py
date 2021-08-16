### LOOPS PRACTICE ###

## FOR LOOPS

# 1. Ask the user to input a number. This represents money inputted in the bank.
# Also ask the user for the number of the years they would like to keep their money in the bank.
# Use a for loop to apply an interest rate of 5% to the money that is inputted.

amount = float(input("Enter the amount of money you would like in the bank: "))
years = int(input("Enter the number of years you would like your money in the bank: "))

print("Your starting balance is: ", str(amount))

for i in range(years):
    amount *= 1.05
print("Your balance after " + str(years) + " years is " + str(amount))

## WHILE LOOPS

# 2.  Ask the user to input an amount of money in cents. 
# Use a while loop to find out the maximum number of quarters, dimes, nickels, & pennies can be made out of it 
money_in_cents = int(input("Enter an amount of money in cents: "))
quarters = 0
dimes = 0 
nickels = 0
pennies = 0

while money_in_cents - 25 >= 0:
    quarters += 1
    money_in_cents -= 25

while money_in_cents - 10 >= 0:
    dimes += 1
    money_in_cents -= 10

while money_in_cents - 5 >= 0:
    nickels += 1
    money_in_cents -= 5

while money_in_cents - 1 >= 0:
    pennies += 1
    money_in_cents -= 1

print("Quarters: "+ str(quarters) + "\nDimes: " + str(dimes) + "\nNickels: " + str(nickels) + "\nPennies: " + str(pennies))

## LOOPS WITH VARIABLES

# 3. Ask the user to input an number. Then create a multiplication table.
# E.g. if the user inputs 3. Print out a 3 x 3 multiplication table. 

num = int(input("Enter a number: "))
for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(str(i) + " * " + str(j) + " = " + str(i * j))
    print("")