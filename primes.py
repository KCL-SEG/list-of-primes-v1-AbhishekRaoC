"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    big = 10000

    for i in range(2, big):
        for x in range(2, i):
            if(i%x == 0):
                break
        else:
            if(len(list) < number_of_primes):
                list.append(i)

        


    return list
