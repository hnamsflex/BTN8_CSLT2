n=int(input('Enter an interger (2 or greater) : '))
dem=0
if(n<2):
    print('Error')
else:
    for i in range(1,n+1):
        if(n%i==0):
            dem=dem+1
    if(dem==2):
        print(n)
    else:
        print('The prime factors of',n,'are:')
        j=2
        while(n!=1):
            if(n%j==0):
                print(j)
                n=n/j
            else:
                j=j+1
