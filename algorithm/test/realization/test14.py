import math


def solution(brown, yellow):
    answer = []
    s = brown+yellow
    for i in range(s,2,-1):
        if s % i == 0:
            a = s // i
            if yellow == (i-2)*(a-2):
                return [i,a]
print(solution(10,2))