#thanh_van
x=float(input())
g=x/2
while abs(g*g-x)>=10**(-12):
    g=(g+x/g)/2
print('The square root of',x,'is approximately',g)