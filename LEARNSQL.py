# Read the three inputs
r, c, e = map(int, input().split())

# Calculate total cells: (initial rows + extra rows) * columns
print((r + e) * c)