message = input("Enter the message: ")
shift = int(input("Enter the shift amount: "))
encrypted_message = ""

for char in message:
    if char.isalpha():
        is_upper = char.isupper()
        #Shift the character by the specified amount
        char_code = ord(char) + shift
        print(char_code)
        if is_upper:
            encrypted_message += chr((char_code - 65) % 26 + 65)
        else:
            encrypted_message += chr((char_code - 97) % 26 + 97)
    else:
        #Non-letter characters will remain intact
        encrypted_message += char
print(f"The encrypted message is: {encrypted_message}")
