# Write a function called "swap" that takes a string as input, and returns a new string with lowercase changed to uppercase, uppercase changed to lowercase.
def swap(target):
    result = ""
    for item in target:
        if item == item.upper():
            result += item.lower()
        elif item == item.lower():
            result += item.upper()
    print(result)


swap("Aloha")  # returns "aLOHA"
swap("Love you.")  # returns "lOVE YOU."
