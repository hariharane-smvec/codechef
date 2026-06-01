t = int(input())

for _ in range(t):
    n = int(input())
    reversed_n = 0
    while n > 0:
        remainder = n % 10
        reversed_n = (reversed_n * 10) + remainder
        n = n // 10
    print(reversed_n)