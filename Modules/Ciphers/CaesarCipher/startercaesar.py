## TODO: Get the user to input a key & the message they wish to encrypt.
## Return the encrypted message using a Caesar Cipher
## Make sure to test for both lower & upper case letters

## Encode the String using Caesar Cipher 
# DO NOT CHANGE FUNCTION NAME OR RETURN TYPE
def encode_caesar(key, message):
    encoded = ""

    ## Your Code Here


    return encoded

## Print out the Encoded Text 
def main(): 
    # Get User Input; both a key and a message
    user_key = int(input("Enter a key: "))
    user_message = input("Enter a message: ")
    # Uncomment the following line to test your code 
    # print(encode_caesar(user_key, user_message))

if __name__ == "__main__":
    main()