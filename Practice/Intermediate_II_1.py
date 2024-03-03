# Write a function called "factorPrime" that takes an integer as input, and returns the prime factorization of the input.
def factorPrime(n):
    result = ""
    num = n
    for i in range(2, n):
        while num % i == 0:
            num /= i
            result += str(i) + " x "
            if (num == 1):
                print(result[:-3])
                return


factorPrime(120)  # returns "2 x 2 x 2 x 3 x 5"
