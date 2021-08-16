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

# numeric cipher with a shift (alpha -> ASCII + shift)
key = 0 # 14

message = "a dog is an animal"
for i in range(len(message)):
    print(str(ord(message[i]) + key) + " ", end = "")

# decode our shifted numeric cipher 
print("")
encryptedShifted = "130 118 115 46 112 111 130 130 122 115 46 133 119 122 122 46 129 130 111 128 130 46 111 130 46 115 119 117 118 130"
print("Encrypted with a shift: ", encryptedShifted)
print("Decrypted result: ")
words2 = encryptedShifted.split(" ")
for w in words2:
    print(chr(int(w) - key), end ="")


# make what we just did into a function 
def shiftedASCII(message, key):
    '''
    inputs
    ---------
    message: string 
    key: int

    output
    --------
    result: string 
    '''
    result = ""

    for i in range(len(message)):
        result += str(ord(message[i]) + key) + " "

    return result

key = 1
msgAscii = shiftedASCII("z dog is an animal", 1) 
print("ASCII Msg", msgAscii) # 98 33 101 112 104 33 106 116 33 98 111 33 98 111 106 110 98 109

nums = msgAscii.split()

for n in nums:
    n = int(n)
    n = (n - ord('a')) % 26 + ord('a')
    if n == 32 + key:
        print(" ", end="")
    else:
        print(chr(n), end="")

# output: b eph jt bo bojnbm

print()
# numeric cipher with a shift with rotation - use mod (alpha -> (ASCII) + key - 1st ASCII) % 26 + 1st ASCII)
#  IMPORTANT FOR YOUR CIPHERS

# if a user enters a key of 52 -> result in NO shift
# example below is only for lower case letters

msg = "peter piper picked a peck of pickled peppers"
key = 17 
for i in range(len(msg)):
    cur = (ord(msg[i]) + key - ord('a')) % 26 + ord('a')
    if msg[i] == " ":
        print(" ", end ="")
    print(chr(cur), end = "")

# lower case are between 97 and 122