# Write a function called "mySort" that takes an list of integers as input, and returns the sorted version of the input list. You are not allowed to use the built-in sorted() function.

def mySort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print(numbers)


mySort([17, 0, -3, 2, 1, 0.5])  # returns [-3, 0, 0.5, 1, 2, 17]
