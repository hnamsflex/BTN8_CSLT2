dem=0
tong=0
while True:
    n=int(input())
    dem=dem+1
    if(n==0):
        break
    tong=tong+n
if(dem==1):
    print('Error message')
else:
    ave=tong/(dem-1)
    print(ave)