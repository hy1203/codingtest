import math,sys
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

n = int(input())

for _ in range(n):
    num = int(sys.stdin.readline())
    while True:
        if num == 0 or num == 1:
            print(2)
            break
        if isPrime(num):
            print(num)
            break
        else:
            num += 1
