t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    total=a*b
    if a > 1000:
        total*=0.9
        print(total)
    else:
        print(total)