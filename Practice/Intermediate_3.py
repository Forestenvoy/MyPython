# Write a function called "palindrome" that checks if the input string is a palindrome. (Search on google if you don't know what a palindrome is.)
def palindrome(s):
    # 回文檢查
    # 檢查 字串 是否相等於 字串(反轉)
    if s == s[::-1]:
        print(True)
    else:
        print(False)


palindrome("bearaeb")  # true
palindrome("Whatever revetahW")  # true
palindrome("Aloha, how are you today?")  # false
