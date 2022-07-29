import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for test_case in range(1, T+1) :
    number = list(map(int , input().split()))
    even = number[1::2]
    odd  = number[::2]
    total =sum(even) + sum(odd) * 2
    
    for N in range(10) :
        if (total + N) % 10 == 0:
            print(f'#{test_case} {N}')