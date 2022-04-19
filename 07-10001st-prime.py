# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

status = False
prime = []
prime.append(2)
stop_num = int(input("please enter stop number: "))
x = 2
while True :
#for x in range (2, 1000) :
    y = 2
    while y < x :
        if x % y != 0 :
            status = True
            y += 1
        else :
            status = False
            break
    if status :
        prime.append(x)
    if(len(prime) != stop_num):
        x += 1
    else:
        break

print(prime)
print("Length of prime list = " + len(prime).__str__())
print(f"the {len(prime)}th number is {max(prime)}")



