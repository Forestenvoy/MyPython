import shelve

integers1 = [1, 2, 3, 5, 6]
integers2 = [6, 7, 8, 9, 10]
integers3 = [100, 101, 102, 103]

# "c"- create, "r" - read, "w" - write
with shelve.open(".\Input_Ouput_File\shelve_example", "c") as shelf:
    shelf["integers1"] = integers1
    shelf["integers2"] = integers2
    shelf["integers3"] = integers3

with shelve.open(".\Input_Ouput_File\shelve_example", "r") as shelf:
    for kry, val in shelf.items():
        print(kry, val)
