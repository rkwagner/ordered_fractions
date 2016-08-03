from fractions import gcd

p = 0
for d in range(1, 12001):
    for n in range(1, d):
        if (d < n*3) and (n*2 < d) and gcd(n, d) == 1:
            p = p + 1
print p
