def encoded_caesar(key, message):
    encoded = ""

    ## Your Code Here
    for i in range(len(message)): 
      curr = ord(message[i])
      if curr >= 97 and curr <= 122: # lower case
        encoded += chr((curr + key - ord('a')) % 26 + ord('a'))
      elif curr >= 65 and curr <= 90: # upper case
        encoded += chr((curr + key - ord('A')) % 26 + ord('A'))
      else: # specal characters 
        encoded += message[i]

    return encoded

## Print out the Encoded Text 
# Get User Input; both a key and a message
def main(): 
  user_key = int(input("Enter a key: "))
  user_message = input("Enter a message: ") # "Dogs do not like cats! But they love ZEBRAS" 

  # Uncomment the following line to test your code 
  print(encoded_caesar(user_key, user_message))  # Epht ep opu mjlf dbut! Cvu uifz mpwf AFCSBT
  
if __name__ == "__main__":  
  main()