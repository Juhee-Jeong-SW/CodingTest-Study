# 큰 수의 법칙
import sys

def solution(n, m, k):
    answer, count, count_k = 0, 1, 1
    n.sort()
    
    while count <= m:
        if count_k == k:
            answer += n[-2]
            count +=1
            count_k = 0
            
        else:
            answer += n[-1]
            count += 1
            count_k += 1
            
    return answer

if __name__ == "__main__":
    size, n, m = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    print(solution(nums, n, m))



    