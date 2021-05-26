# 숫자 카드 게임
# idea : 행마다 작은 수를 찾은 후 그 수 중 가장 큰 수 찾기.
import sys

def solution(n, m, r):
    for i in range(n):
        nums = list(map(int, sys.stdin.readline().split()))
    
        min_num = min(nums)
        result = max(r, min_num)
    return result

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    result = 0
    print(solution(n, m, result))