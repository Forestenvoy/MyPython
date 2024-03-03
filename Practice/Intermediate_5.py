# Write a function called "inversePyramid" that draws pyramid upside down.
def inversePyramid(n):
    for i in range(n, 0, -1):
        print(" "*(n-i) + "*"*(2*i-1))


inversePyramid(4)
# *******
#  *****
#   ***
#    *
