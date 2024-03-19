def solution(x):
    sum=0
    num=x
    while (x>0):
        sum+= x%10
        x //= 10
    if(num%sum==0):
            return True
    else:
            return False
