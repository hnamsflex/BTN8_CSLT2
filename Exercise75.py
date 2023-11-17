#thanh_van
m=int(input(''))
n=int(input(''))
d=min(m,n)
if m>0 and n>0:
    while m%d != 0 or n%d != 0:
         d=d-1
    print('the greatest common divisor is',d)
else:
    print('enter a positive integer')