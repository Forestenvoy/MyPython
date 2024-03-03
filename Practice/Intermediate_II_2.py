# Write a function called "intersection" that takes 2 lists, and returns an list of elements that are in the intersection of 2 list.

def intersection(list1, list2):
    print(list(set(list1) & set(list2)))


intersection([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0])  # returns [3, 4]

# 使用在 set 型態時，& 可用來進行交集，| 可用來做聯集，^ 可用來做互斥，除此之外，上面的程式中也看到了，- 可用來做減集，>、<（以及 >=、<=、==）可用來測試兩集合的包括關係。
