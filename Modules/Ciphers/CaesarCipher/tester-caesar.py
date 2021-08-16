from startercaesar import encode_caesar
import time 

test_case = {'hello': (5, 'mjqqt'), 'helloo': (29, 'khoorr'), 'my name is': (17,'dp erdv zj'), 'How could you go to Greece without me': (13, 'Ubj pbhyq lbh tb gb Terrpr jvgubhg zr')}
score = 0

print("tester-caesar.py is testing your code....")
time.sleep(1)
for key, value in test_case.items():
    print("Testing encoding the MESSAGE = " + key + " with a Caesar cipher for KEY = " + str(value[0]), end="", flush=True)
    if encode_caesar(value[0], key) == value[1]:
        print(" [Correct]", flush=True)
        score += 1
    else: 
        print(" [Incorrect]", flush=True)
        print("Your program gives: " + encode_caesar(value[0],key) + "\nExpected Output: " + value[1], flush=True)
    time.sleep(1)
print(str(score) + "/" + str(len(test_case)) + " Test Cases Passed")