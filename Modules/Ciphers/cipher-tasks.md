# Ciphers & Data Conversion

You now have a good understanding of the core concepts of Python programming.

Let's recap. You have learned:
- Strings, Characters, & Numeric Data Types
- Variables 
- Functions 
- For & While Loops
- If/Else Statements 
- ASCII

Now we can start to dive into using Python for more Cybersecurity related topics. Last module, you worked on a Password Validator. This helped ensure that a password would be hard to guess for malicious actors who may be trying to brute force their way into an account, server, or database.

Now, we turn to learning how to keep this data even more secure with encryption. 

We will first start by covering some ciphers. Ciphers capture the core concepts behind sending data that cannot be read if interecepted. Lets say you want to send a message to Alice that you do not want anyone else to read. If you send Alice the message in a special *language* that only you two know, then even if someone gets the message they could not read it. 

This is the main idea behind encryption. Ciphers are one of the oldest forms of data encryption. 

# 1. Caesar Cipher

Caesar ciphers are one of the oldest form of data encryption. Thought to have been used during the Roman Empire by Caesar himself, it was used to prevent enemies from reading messages related to war and trade. 

The Caesar cipher works by shifiting letters in the alphabet to reconstruct your word. For example, if we shift the alphabet by one letter 'a' becomes 'b' and 'b' becomes 'c'. So, the word 'cat' would be 'dbu' under a Caesar Cipher with a single letter shift. 

Now that you know the basics, you can start coding your on Caesar Cipher.

FIRST, go through CS50's explaination of the Caesar Cipher: https://docs.cs50.net/2018/x/psets/2/caesar/caesar.html
Note: there sample code is in C. Another programming language, but the concepts ddiscussed still apply to Python.

THEN, play around with using a Caesar Cipher on Khan Academy's site: https://www.khanacademy.org/computing/computer-science/cryptography/crypt/pi/caesar-cipher-exploration
FINALLY, implement a program that takes in a word and a key, then prints out the result encoded using a Caesar Cipher.

``` 
Enter a phrase to encode: HELLO
Key: 13
Result: URYYB

Enter a phrase to encode:  be sure to drink your Ovaltine
Key: 13
Result: or fher gb qevax lbhe Binygvar
```

It is IMPORTANT to start with the starter code in the [startercaesar.py](https://github.com/sprakaha/Python-CyberSecurity101/blob/main/Modules/Ciphers/CaesarCipher/startercaesar.py) file. Do not change the function headers or file name. 

When you are done writing your code, [tester-caesar.py](https://github.com/sprakaha/Python-CyberSecurity101/blob/main/Modules/Ciphers/VigenereCipher/tester-caesar.py) file on your computer and see what score you get. Make sure this file is in the same folder as the startervigenere.py file. 
Keep changing your code until you get 100%.

Functions You Will Likely Use: 
- input() - https://www.w3schools.com/python/ref_func_input.asp
- print() - https://www.w3schools.com/python/ref_func_print.asp
- ord() - https://www.w3schools.com/python/ref_func_ord.asp
- modulo operator - https://www.w3schools.com/python/python_operators.asp

Key Concepts: 
- ASCII - https://www.asciitable.com/
- Caesar Cipher - https://en.wikipedia.org/wiki/Caesar_cipher

For more information & the history of the Caesar Cipher, check ou the Wiki Page: https://en.wikipedia.org/wiki/Caesar_cipher

# 2. Vigenere Cipher 

Just like the Caesar Cipher, the Vigenere Cipher is another method that people once used to encode messages.
You may have noticed while working on the Caesar Cipher, that one of the draw backs is that it can be easy to guess the encrypted message. There are only 25 shifts in the alphabet. If you try all of them, eventually someone can decrypt your message.

The Vigenere Cipher is a bit more complicated for people to decode your message.

FIRST, go through CS50's explaination of the Vigenere Cipher: https://docs.cs50.net/2018/x/psets/2/vigenere/vigenere.html
Note: there sample code is in C. Another programming language, but the concepts ddiscussed still apply to Python.

THEN, implement a program that takes in a word and a key, then prints out the result encoded using a Vigenere Cipher.

```
Enter a phrase to encode: Meet me at the park at eleven am
Key: bacon
Result: Negh zf av huf pcfx bt gzrwep oz

Enter a phrase to encode: How could you go to Greece without me 
Key: mapletree
Result: Tol nsnch cau vz xh Xviqct hmmysyf mt
```

It is IMPORTANT to start with the starter code in the [startervigenere.py](https://github.com/sprakaha/Python-CyberSecurity101/blob/main/Modules/Ciphers/VigenereCipher/startervigenere.py) file. 

When you are done writing your code, run the [tester-vigenere.py](https://github.com/sprakaha/Python-CyberSecurity101/blob/main/Modules/Ciphers/VigenereCipher/tester-vigenere.py) file on your computer and see what score you get. Make sure this file is in the same folder as the startervigenere.py file. 
Keep changing your code until you get 100%.

Functions You Will Likely Use: 
- input() - https://www.w3schools.com/python/ref_func_input.asp
- print() - https://www.w3schools.com/python/ref_func_print.asp
- ord() - https://www.w3schools.com/python/ref_func_ord.asp
- modulo operator - https://www.w3schools.com/python/python_operators.asp

Key Concepts: 
- ASCII - https://www.asciitable.com/
- Vigenere Cipher - https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

For more information & the history of the Vigenere Cipher, check ou the Wiki Page: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
Implement a program that takes in a word and a key, then prints out the result encoded using a Vigenere Cipher.