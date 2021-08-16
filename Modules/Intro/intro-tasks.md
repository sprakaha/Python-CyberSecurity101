## Intro 

These tasks will help you gain a basic understanding of Python.
The goal is to build your familiarity with concepts we will be using often.

# 1. Hello World 

Implement a program that prints out a simple greeting to the user, per the below.

``` 
What is your name?
David
hello, David
```

Find the solution here [https://github.com/sprakaha/Python-CyberSecurity101/blob/main/Modules/Intro/HelloWorld/hello.py]

Functions You Will Likely Use: 
- input() - https://www.w3schools.com/python/ref_func_input.asp
- print() - https://www.w3schools.com/python/ref_func_print.asp

Key Concepts: 
- Strings: https://www.w3schools.com/python/python_strings.asp

# 2. Pyramid Building 

Implement a program that prints out a half-pyramid of a specified height, per the below.

```
Height: 4
   #
  ##
 ###
####
```
The user input should be a **positive integer between 1 and 8**, inclusive. If the user fails to provide a positive integer no greater than 8, you should **re-prompt** for the same again. Then, generate (with the help of print and one or more loops) the desired half-pyramid. Make sure that the pyramid is right aligned. 

Find the solution here [https://github.com/sprakaha/Python-CyberSecurity101/blob/main/Modules/Intro/Pyramid/pyramid.py]

Functions You Will Likely Use: 
- input() - https://www.w3schools.com/python/ref_func_input.asp
- range() - https://www.w3schools.com/python/ref_func_range.asp
- isnumeric() - https://www.geeksforgeeks.org/python-string-isnumeric-application/
- int() - https://www.geeksforgeeks.org/convert-string-to-integer-in-python/

Key Concepts: 
- Conditionals: https://www.w3schools.com/python/python_conditions.asp
- Loops: https://www.w3schools.com/python/python_for_loops.asp

# 3. Loop Da Loop

This exercise will give you more practice working with loops.
Implement the three tasks in the starter-loops.py file. 

STARTER CODE: [https://github.com/sprakaha/Python-CyberSecurity101/blob/main/Modules/Intro/LoopDaLoop/starter-loops.py]

Implement the tasks should result in output that looks like the following:

Task 1: Apply an interest of 5% to an entered amount over the specified number of years. 
```
Enter the amount of money you would like in the bank: 1000
Enter the number of years you would like your money in the bank: 5

Your starting balance is: 1000
Your balance after  years is 1276.2815625000003
```

Task 2: Convert pennies to the maximum amount of quarters, dimes, nickels, & pennies.
```
Enter an amount of money in cents: 116
Quarters: 4
Dimes: 1
Nickels: 1
Pennies: 1
```

Task 3: Create a n x n multiplication table, where n is a number the user enters.
```
Enter a number: 3
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6

3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
```


Functions You Will Likely Use: 
- float(), str() - https://www.w3schools.com/python/python_casting.asp

Key Concepts: 
- Nested Loops: https://www.educba.com/python-nested-loops/
- While Loop: https://www.w3schools.com/python/python_while_loops.asp
- For Loop:  https://www.w3schools.com/python/python_for_loops.asp
- Casting: https://www.w3schools.com/python/python_casting.asp

# 4. Strings

This exercise will have you practice working with strings, characters, and ASCII values. 
Implement the eight tasks in the starter-string.py file. 

STARTER CODE: [https://github.com/sprakaha/Python-CyberSecurity101/blob/main/Modules/Intro/Strings/starter-string.py]

Functions You Will Likely Use: 
- ord() - https://www.w3schools.com/python/ref_func_ord.asp

Key Concepts: 
- ASCII: https://www.asciitable.com/
- String Indexing/Looping : https://www.w3schools.com/python/python_strings.asp

Find the solution here [https://github.com/sprakaha/Python-CyberSecurity101/blob/main/Modules/Intro/Strings/solution-string.py]

# 5. Password Validation

At this point, you have done loops, strings, conditionals! We are going to combine this knowledge into 
a project to create a program that determines the strength of your password. 

Background: Strong passwords are of extreme importance in cybersecurity.
Passwords provide the first line of defense against unauthorized access to your computer and personal information. 
Passwords can be cracked via a hacker forcefully guessing your password (brute force), using key logging malware which records passwords as they are entered, accessing passswords that were leaked from a previous data breach,  and many other methods. 

Although having a strong password cannot protect against all these attacks. It is extremely helpful for 

Implement a program that verifies that a password is strong.
Based on some https://www.att.org.uk/cyber-security-making-most-passwords
A strong password MUST:
- have at least 8 characters
- have at least one upper case letter and one lower case letter
- have at at least 2 special characters & 2 numbers

Start this task by opening the starter-pv.py file. 
STARTER CODE: Find the solution here [https://github.com/sprakaha/Python-CyberSecurity101/blob/main/Modules/Intro/PasswordValidation/solution-pv.py]

```
Welcome to the Password Validator...
I'll help you creat a strong password

Please enter your password: hello
Weak. This is word in the dictionary.
Weak. This password is too short.
Weak. There are not enough special characters.
Weak. There are not enough numbers.
Weak. There needs to be an upper case & lower case letter.

Please enter your password: asdhdh5hg8fk9
Weak. There are not enough special characters.
Weak. There needs to be an upper case & lower case letter.

```

Key Concepts: 
- ASCII: https://www.asciitable.com/
- Conditionals, Loops 

Intro Task 1 & 2 Ideas courtesy: https://cs50.harvard.edu/x/2020/psets/6/hello/