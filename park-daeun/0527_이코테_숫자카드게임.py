import sys

n, m = map(int, sys.stdin.readline().split())
cards = []
max = 0

for _ in range(0, n):
    cards = list(map(int, sys.stdin.readline().split()))
    if max < min(cards):
        max = min(cards)
print(max)

'''
입력 예시
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4

출력 예시
2

3
'''
