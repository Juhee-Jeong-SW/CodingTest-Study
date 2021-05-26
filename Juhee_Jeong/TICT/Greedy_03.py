# 1이 될 때까지
# side-notes : 단순하게 푸는 방식으로만 하게 되어서 교재 소스코드 참고함.
import sys

def solution(n, k, result):
    while True:
        target = (n // k) * k
        result = result + (n - target)
        n = target

        if n < k:
            break

        result += 1
        n = n // k
    
    result += (n - 1)
    return result

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    result = 0
    print(solution(n, k, result))