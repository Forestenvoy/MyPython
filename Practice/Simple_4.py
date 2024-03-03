# Write a function called "findSmallCount" that takes one list of integers and one integer as input, and returns an integer indicating how many elements in the list is smaller than the input integer.
def findSmallCount(numbers, target):
    count = 0
    for num in numbers:
        if num < target:
            count += 1
    print(count)


findSmallCount([1, 2, 3], 2)  # returns 1
findSmallCount([1, 2, 3, 4, 5], 0)  # returns 0
