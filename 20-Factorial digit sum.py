# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

number = int(input("enter number: "))
factorial = 1
for x in reversed (range (1, number + 1)) :
    factorial *= x

print(factorial)
factorial_str = factorial.__str__()
factorial_char = []
for x in factorial_str :
    x = int(x)
    factorial_char.append(x)
sum_factorial = 0
for x in factorial_char :
    sum_factorial += x

print(f"the sum of the digits ({number}!) = ", sum_factorial)


