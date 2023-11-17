n=int(input())
thuong=1
S=''
Sn=''
while(thuong!=0):
    thuong=n//2
    du=str(n%2)
    n=thuong
    S=S+du
x=len(S)
for i in range(x-1,-1,-1):
    Sn=Sn+S[i]
print(Sn)

