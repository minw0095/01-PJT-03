import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())


for test_case in range(1, T+1) :
    number = {}
    new_number = {}
    N = input().split()
    
    for a in N :
        number[a] = number.get(a , 0) + 1
    miner = min(number.values())
    
    for a in number :
        if number[a] == miner :
            print(f'#{test_case} {a}')