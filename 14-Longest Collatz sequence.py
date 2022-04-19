# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# Which starting number, under one million, produces the longest chain?
temp_chain = []
chain_length = []
dic = {}

start_index = 13
stop_index = 100
for x in range(start_index, stop_index) :
    temp_chain.append(x)
    primitive_x = x
    while True :
        if x % 2 == 0 :
            x = int(x/2)
            temp_chain.append(x)
        else :
            x = int(3 * x + 1)
            temp_chain.append(x)
        if x == 1 :
            chain_length.append(len(temp_chain))
            print(temp_chain)
            a = {primitive_x : len(temp_chain)}
            dic.update(a)
            temp_chain.clear()
            break

print()

#print(chain_length)

for key in dic :
    print(key , '->' , dic[key])
    temp_chain.append(dic[key])

max_v = max(temp_chain)

for k in dic :
    if dic[k] == max_v :
        print("Which starting number is the longest chain :" , k)
        break

