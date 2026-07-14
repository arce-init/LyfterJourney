def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def get_primes(my_list):
    primes = []
    for  number in my_list:
        if is_prime(number):
            primes.append(number)
    return primes

print(get_primes([1, 4, 6, 7, 13, 9, 67]))