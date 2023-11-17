message = input("Enter the message: ")
shift = int(input("Enter the shift amount: "))
encrypted_message = ""
# c or char 
for c in message:
    if c.isalpha():
        is_upper = c.isupper() # true false
        #Shift the character by the specified amount
        char_code = ord(c) + shift
        # print(char_code)
        if is_upper:
            encrypted_message += chr((char_code - 65) % 26 + 65)
        else:
            encrypted_message += chr((char_code - 97) % 26 + 97)
    else:
        #Non-letter characters will remain intact
        encrypted_message += c
print(f"The encrypted message is: {encrypted_message}")
