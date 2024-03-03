# Write a function called "findAllSmall" that takes one list of integers and another integer as input, and returns an list of integers that contains all elements that are smaller than the input integer.
def findAllSmall(numbers, target):
    result = []
    for num in numbers:
        if num < target:
            result.append(num)
    print(result)


findAllSmall([1, 2, 3], 10)  # returns [1, 2, 3]
findAllSmall([1, 2, 3], 2)  # returns [1]
findAllSmall([1, 3, 5, 4, 2], 4)  # returns [1, 3, 2]
