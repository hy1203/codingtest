import sys
input = sys.stdin.readline
votes = []
cnt = 0
n = int(input())
first = int(input())
for _ in range(n-1):
    vote = int(input())
    votes.append(vote)
votes = sorted(votes,reverse = True)

if n == 1:
    print(0)
else:
    while votes[0] >= first:
        first += 1
        votes[0] -= 1
        cnt += 1
        votes.sort(reverse=True)
    print(cnt)