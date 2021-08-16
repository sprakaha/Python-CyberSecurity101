# if we needed to import external libraries we would do so here
# no imports are needed for this project

# a function we create to deal with non numeric input
def get_int(a):
    '''
    Input: a - string
    Output: either number or -1 if invalid
    '''
    # checks if the inputted string is a number, if it is return an int of the number
    if a.isnumeric(): 
        return int(a)
    else:
        return -1 

# prompt the user for input height
height = get_int(input("Height: "))

# check if the input is valid
# repeteadly prompts the user, if it is invalid
while height < 1 or height > 8:
    height = get_int(input("Height: "))

# loop through 1 to height (the last number in range is EXCLUDED)
for i in range(1, height + 1): 
    # prints out a string made up of spaces and #s
    print( " " * (height - i) + "#" * i)


    '''
      # - 1 hashtag & 2 spaces
     ## - 2 hashtags & 1 space
    ### - 3 hashtags & 0 spaces 
    '''