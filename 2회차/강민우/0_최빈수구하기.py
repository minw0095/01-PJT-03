import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())

for test_case in range(1, T+1) :
    s = input()
    N = map(int , input().split())
    score = {}
    for a in list(N):
        score[a] = score.get(a ,0) +1
    
    for a in sorted(score.keys() , reverse =True) :
        if score[a] == max(score.values()) :
            print(f'#{test_case} {a}')
            break

