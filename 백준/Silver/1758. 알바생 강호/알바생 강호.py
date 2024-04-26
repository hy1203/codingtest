import sys
input = sys.stdin.readline
n = int(input().rstrip())
tip=[int(input().rstrip()) for _ in range(n)]
result = 0
    
tip = sorted(tip,reverse=True)

for i in range(len(tip)):
    r_tip = tip[i]-i
    if r_tip < 0:
        continue
    result += r_tip
print(result)