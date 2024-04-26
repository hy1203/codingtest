import sys
input = sys.stdin.readline
n, l = map(int,input().split())
word_dict={}

for w in range(n):
    w = input().strip()
    if len(w) < l:
        continue
    if word_dict.get(w):
        word_dict[w][0] += 1
    else:
        word_dict[w] = [1, len(w), w]
result = sorted(word_dict.items(),key = lambda x : (-x[1][0],-x[1][1],x[1][2]))
for r in result:
    print(r[0])