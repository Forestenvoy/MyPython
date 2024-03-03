# Write a function that check if a list contains a subsequence of 007
def spyGame(nums):
    first = False
    second = False
    for i in range(len(nums)):
        if nums[i] == 7 and second == True:
            return True
        if nums[i] == 0 and first == True:
            second = True
        if nums[i] == 0:
            first = True
    return False


print(spyGame([1, 2, 4, 0, 3, 0, 7]))  # True
print(spyGame([1, 2, 5, 0, 3, 1, 7]))  # False
