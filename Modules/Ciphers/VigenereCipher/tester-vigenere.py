from startervigenere import encode_vigenere
import time 

test_case = {'ATTACKATDAWN': ('LEMONLEMONLE', 'LXFOPVEFRNHR'), 'GEEKSFORGEEKS' : ('AYUSH', 'GCYCZFMLYLEIM'), 'Meet me at the park at eleven am': ('bacon', 'Negh zf av huf pcfx bt gzrwep oz'), 'How could you go to Greece without me': ('mapletree', 'Tol nsnch cau vz xh Xviqct hmmysyf mt')}
score = 0

print("tester-vigenere.py is testing your code....")
time.sleep(1)
for key, value in test_case.items():
    print("Testing encoding the MESSAGE = " + key + " with a Vigenere cipher for KEY = " + value[0], end="", flush=True)
    if encode_vigenere(value[0], key) == value[1]:
        print(" [Correct]", flush=True)
        score += 1
    else: 
        print(" [Incorrect]", flush=True)
        print("Your program gives: " + encode_vigenere(value[0],key) + "\nExpected Output: " + value[1], flush=True)
    time.sleep(1)
print(str(score) + "/" + str(len(test_case)) + " Test Cases Passed")