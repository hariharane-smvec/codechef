t=int(input())
for i in range(t):
    n=input()
    rev_n=n[::-1]
    if n==rev_n:
        print("wins")
        

    else:
        print("loses")
