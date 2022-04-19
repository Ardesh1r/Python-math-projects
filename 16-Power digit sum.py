# 2 ^ 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?
import math

status = True
while status :
    x = int(input("enter base: "))
    y = int(input("enter power: "))
    power = x ** y
    print(f"{x} ^ {y} = ", power)
    power_arr = []
    power_String = str(power)
    for x in power_String :
        power_arr.append(x)

    sum_power_chars = 0
    for x in power_arr :
        x = int(x)
        sum_power_chars += x

    print(f"sum of the digits of the number = ", sum_power_chars)
    status = True
    print("-------start--------")



