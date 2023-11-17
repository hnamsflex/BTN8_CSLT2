#thanh_van
str_input = input("Enter string:")
length = len(str_input)
x = 0
y = length - 1
palindrome = True
while x < y :
    if str_input[x] != str_input[y]:
        palindrome = False
        print("not palindrome")
        break
    x += 1
    y -= 1

if palindrome:
    print("is palindrome")
    
    
    

