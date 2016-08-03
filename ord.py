#given p/q<3/7
#p*7<q*3
#p*7<=q*3-1
#p<=(3*q-1)/7

num = 3
denom = 7
sub = 1
s = 1
r = 0
denom_ceiling = 1000000
for q in range(1000000, 2, -1):
    p = (num*q-sub)/denom
#verify current iteration is optimal.
    if p*s > q*r:
        s = q
        r = p
print r, "/", s


