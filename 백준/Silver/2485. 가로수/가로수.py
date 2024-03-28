from math import gcd
n = int(input())
a = int(input())
street = []
result = 0

for _ in range(n-1):
    num = int(input())
    street.append(num-a)
    a = num
    
g = street[0]
for i in range(1, len(street)):
    g = gcd(g, street[i])

for i in street:
    result += i // g -1
    
print(result)
