#2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

num = 20
counter = []
i = 1
while True:
    while i < 11 :
        if num % i !=0 :
            print(num.__str__() + " is not diversiable")
            num += 1
            counter.clear()
            i=1
            break
        else:
            counter.append(i)
            i += 1
            if len(counter) == 10 :
                print()
                print(counter)
                smallest_positive_num = num
                print(smallest_positive_num.__str__() + " is the smallest positive number")
                print()
                for x in counter:
                    print(f"{num} / {x} = " + (num / x).__str__() + " , remaining = " + (num % x).__str__())
                exit()


