import math
import sys

def solve():
    # Read number of test cases
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    
    for _ in range(T):
        B = int(input_data[idx])
        LS = int(input_data[idx+1])
        idx += 2
        
        # Calculate min and max RS
        # Min RS: hypotenuse is LS, leg is B
        rs_min = math.sqrt(LS**2 - B**2)
        # Max RS: hypotenuse is RS, legs are LS and B
        rs_max = math.sqrt(LS**2 + B**2)
        
        print(f"{rs_min} {rs_max}")

if __name__ == '__main__':
    solve()