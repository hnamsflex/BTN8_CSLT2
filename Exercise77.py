S=str(input())
n=len(S)
dem=0
so=0
for i in range(n-1,-1,-1):
    x=2**dem
    dem=dem+1
    y=x*int(S[i])
    so=so+y
print(so)
