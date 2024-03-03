# Write a function called "position" that returns a tuple of the first uppercase letter and its index location. If not found, returns -1.

def position(word):
    for i in range(len(word)):
        if word[i].isupper():
            ans = word[i], i
            print(ans)
            return
    print(-1)


position("abcd")  # returns -1
position("AbcD")  # returns ('A', 0)
position("abCD")  # returns ('C', 2)
