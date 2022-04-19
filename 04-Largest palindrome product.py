#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

i = 100
j = 100
list1 = []
while i < 1000 :
    while j < 1000 :
       product = i * j
       j += 1
       prd = product.__str__()
       print(prd)
       if prd[0] == prd[-1] :
           list1.append(prd)
    i += 1
    j = 100

#print(list1)
list2 = []

# now Let's filter numbers more accurately
#if len(list1) == 5:
for x in list1:
    if x[0:2] == (x[-1] + x[-2]):
        if(len(x) == 5):
            list2.append(x)
        else:
            break

list3 = []
for y in list1:
    if (len(y) == 6):
        if y[0:3] == (y[-1] + y[-2] + y[-3]):
            list3.append(y)


print("5-digit output = ")
print(list2)
print("6-digit output = ")
print(list3)
print("the largest 3-digits palindrome  = " + max(list3).__str__())