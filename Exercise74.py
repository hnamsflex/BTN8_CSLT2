print("   ",end="")
for x in range(1,11):
    print(" ",x," ",end="",sep="")
print()
for i in range(1,11):
    if i != 10:
        print(" ",end="")
    print(i,"",end="")
    
    for j in range(1,11):
        kq=i*j
        if len(str(kq)) == 1:
            print(" ",end="")
        if j == 10 and kq != 100 :
            print(" ",end="")
        print(kq,"",end="")
    print()