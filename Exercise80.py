import random

num_simulations = 10
total_flips = 0

for _ in range(num_simulations):
    flips = ''
    consecutive_count = 0
    flips_count = 0

    while consecutive_count < 3:
        flip = random.choice(['H', 'T'])
        flips += flip
        flips_count += 1

        if len(flips) >= 3:
            if flips[-3:] == 'HHH' or flips[-3:] == 'TTT':
                consecutive_count = 3

    print(f"{flips} ({flips_count} flips)")
    total_flips += flips_count

average_flips = total_flips / num_simulations
print(f"\nOn average, {average_flips:.1f} flips were needed.")
