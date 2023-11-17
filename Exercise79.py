import random
dem=-1
max=0
for i in range(1,100+1):
    n=random.randint(1,100)
    if(n>max):
        max=n
        dem=dem+1
    print(n)
print('The maximum value found was',max)
print('The maximum value was updated',dem,'times')