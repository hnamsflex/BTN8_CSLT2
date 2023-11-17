#hoai_nam
while True:
    bits_input = input("Enter 8 bits:")

    if not bits_input:
        break

    if len(bits_input) != 8:
        print("Error: Please enter exactly 8 bits.")
        continue

    # Count the number of one bits in the input
    one_bits_count = bits_input.count('1')
    print(bits_input.count('1'))

    if one_bits_count % 2 == 1:
        parity_bit = 1  
    else:
        parity_bit = 0

    print(f"The parity bit should be: {parity_bit}")
