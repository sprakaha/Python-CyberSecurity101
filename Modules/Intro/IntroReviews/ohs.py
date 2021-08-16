## RANGE

# range() can take in 1 to 3 arguments
# an argument is the value that we pass into a function

# when we pass in 1 number that represents the ending value - 1
# by default it starts at 0
for i in range(4):
    print(i)

# when we pass in 2 numbers that represents the ending value - 1
# by default it starts at 0
start = 3
end = 10
for i in range(start, end):
    print(i)

# 3 parameters: start, end, iterator/count by
for i in range(10, 3, -2):
    print(i)


for i in range(4):
    for j in range(3):
        print(str(i) + " * " + str(j) + "=", i * j)

# going in order 0, 1, 2, 3
#  each thing is printing 3 times 


# the END parameter in range is excluded, that means that 

for i in range(5):
    print(i)
print("")
for i in range(5 + 1):
    print(i)