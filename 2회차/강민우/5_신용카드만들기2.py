import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for test_case in range(1, T+1) :
    N = input()
    number =  N.replace('-' , '' )
    number_list = list(number)
    start_list = list('34569')

    if not number_list[0] in start_list :
        print(f'#{test_case} {0}')
    elif len(number_list) != 16 :
        print(f'#{test_case} {0}')
    else :
        print(f'#{test_case} {1}')