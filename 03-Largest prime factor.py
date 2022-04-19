def get_num():
    number = int(input("please enter number: "))
    return number


def prime_numbers(n):
    i = 1
    factors = []
    prime = []
    not_prime = []
    while i <= num:
        if (num % i == 0):
            factors.append(i)
        i += 1
    factors.pop(0)
    factors.pop(len(factors) - 1)
    print("factors : ")
    print(factors)

    for x in factors:
        for j in range(2, x - 1):
            if x % j == 0:
                not_prime.append(x)
                break

    for y in factors:
        if y not in not_prime:
            prime.append(y)

    print("not prime:")
    print(not_prime)

    print("prime:")
    print(prime)


while input("do you want to calculate? (y / n) : ") == 'y':
    num = get_num()
    prime_numbers(num)
