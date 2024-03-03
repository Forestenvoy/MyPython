# Write a function called "table9to9" that prints out the multiplication table:
def table9to9():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i*j:2d} ", end="")
        print()


table9to9()
