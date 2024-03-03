# Write a function called "flatten" that flattens an list.
result = []


def flatten(List):
    for item in List:
        if isinstance(item, list):
            flatten(item)
        else:
            result.append(item)
    return result


print(flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]))
# returns [1, 2, 0, 1, 3, 1, 3, 3, 4, 1, 2]
