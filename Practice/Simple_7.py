# Write a function called "summ" that takes one list of numbers, and return the sum of all elements in the input list.
def summ(numbers):
    result = 0
    for num in numbers:
        result += num
    print(result)


summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # returns 55
summ([])  # return 0
summ([-10, -20, -30])  # return -60
