t = int(input())
for _ in range(t):
    coin = int(input())
    print(coin//25, (coin%25)//10,((coin%25)%10)//5,(((coin%25)%10)%5)//1)