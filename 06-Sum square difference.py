#The sum of the squares of the first 100 natural numbers is,
#The square of the sum of the first 100 natural numbers is,
while True:
    i = int(input("please enter number range. i: "))
    j = int(input("please enter number range. j: "))
    sum_1 = 0
    sum_2 = 0
    numbers_1 = []
    product = 1
    numbers_2 = []

    for x in range (i, j + 1):
        product = x ** 2
        numbers_1.append(product)
        sum_1 += product

    for y in range (i, j + 1):
        sum_2 += y
    sum_2 = sum_2 ** 2

    print(numbers_1)
    print()
    print(sum_1)
    print(sum_2)
    print()
    print(f"difference betweeen {sum_2} - {sum_1} = " + (sum_2 - sum_1).__str__() )

