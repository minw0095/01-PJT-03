import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for test_case in range(1, T+1) :
    N = input()
    new_word = []
    change ={
        'b' : 'd',
        'd' : 'b',
        'p' : 'q',
        'q' : 'p'
     }
    word = list(N)[::-1]
    print(word)
    for a in word :
        if a in change.keys() :
            a = change[a]
            new_word.append(a)
    print(f"#{test_case} {''.join(new_word)}")
