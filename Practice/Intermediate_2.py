# Write a function called "isPrime" that takes an integer as input, and returns a boolean value that indicates if the input number is prime.
def isPrime(number):
    if number < 2:
        print(False)
        return
    for i in range(2, number):
        if number % i == 0:
            print(False)
            return
    print(True)


isPrime(1)  # returns false
isPrime(5)  # returns true
isPrime(91)  # returns false
isPrime(1000000)  # returns false
