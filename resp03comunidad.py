def is_prime(number):
    divisors = 0;
    if (number < 2):
        return False
    for num in range(1, number + 1):
        if (number % num == 0):
            divisors += 1
    return True if divisors == 2 else False
for num in range(1, 101):
    if (is_prime(num)):
        print(num)