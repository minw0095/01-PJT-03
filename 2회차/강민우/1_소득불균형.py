import sys

sys.stdin = open("_소득불균형.txt")
T = int(input())

for test_case in range(1, T+1) :
    N = int(input())
    number = list(map(int, input().split()))
    number_list = []

    for a in number :
      if a <= sum(number) / len(number) :
        number_list.append(a)
    print(f'#{test_case} {len(number_list)}')