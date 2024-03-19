def solution(arr, divisor):
    newArr=[]
    for i in arr:
        if(i%divisor==0):
            newArr.append(i)
    if(len(newArr) == 0):
        newArr.append(-1)
    newArr.sort()
    return newArr