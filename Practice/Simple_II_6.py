# Write a function called "findMin" which takes an list as input, and returns the minimum element in the input list.
def findMin(numbers):
    if len(numbers) == 0:
        print("undefined")
        return
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    print(min)


findMin([1, 2, 5, 6, 99, 4, 5])  # returns 1
findMin([])  # returns undefined
findMin([1, 6, 0, 33, 44, 88, -10])  # returns -10
