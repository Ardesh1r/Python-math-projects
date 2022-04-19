#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

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
    if( x < stop_num):
        x += 1
    else:
        break

print(prime)
print("Length of prime list = " + len(prime).__str__())
print(f"the {len(prime)}th number is {max(prime)}")
sum_prime = 0
for x in prime :
    sum_prime += x
print(f"sum of prime numbers below {stop_num} is {sum_prime}")