import sys

sys.stdin = open("_암호문1.txt")

for test_case in range(1, 2) :
    N = input()
    origin =  input().split()
    order_N = int(input())
    i = 1
    j = 2 

    
    order = input().split()
    for a in range(order_N) :
        x = order[i]
        y = order[j]
        print(i,j)
        s = " ".join(order[i+2:2+i+j])
        origin.insert(int(x),s)
        i += 2+2+int(x)+int(y)
        j += 3+2+int(x)+int(y)
        
    print(origin)

