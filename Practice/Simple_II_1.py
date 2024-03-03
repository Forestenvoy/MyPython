# Write a function called "stars" which prints out layers of stars in the following pattern:
def stars(n):
    for i in range(1, n+1):
        print("*" * i)


stars(1)
# *
stars(4)
# *
# **
# ***
# ****
