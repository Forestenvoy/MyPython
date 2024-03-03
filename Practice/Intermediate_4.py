# Write a function called "pyramid" that takes an integer as input, and prints a pyramid in the following pattern:
def pyramid(n):
    for i in range(n):
        print(" "*(n-i-1) + "*"*(2*i+1))


pyramid(1)
# *
pyramid(2)
#  *
# ***
pyramid(4)
#    *
#   ***
#  *****
# *******
