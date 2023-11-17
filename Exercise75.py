m=int(input())
n=int(input())
if(m==n):
    print(m)
elif(m%n==0):
    print(n)
elif(m%n==0):
    print(m)
elif(m<n):
    d=m
    while(d!=0):
        if((m%d==0) and (n%d==0)):
            print(d)
            break
        d=d-1
elif(n<m):
    d=n
    while(d!=0):
        if((m%d==0) and (n%d==0)):
            print(d)
            break
        d=d-1