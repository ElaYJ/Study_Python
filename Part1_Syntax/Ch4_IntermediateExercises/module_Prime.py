class NotPrimeException(Exception):

    def __init__(self, n):
        super().__init__(f'{n} is not prime number.')


class PrimeException(Exception):

    def __init__(self, n):
        super().__init__(f'{n} is prime number.')


def isPrime(number):
    flag = True
    for n in range(2, number):
        if number % n == 0:
            flag = False
            break

    if flag == False:
        raise NotPrimeException(number)
    else:
        raise PrimeException(number)



