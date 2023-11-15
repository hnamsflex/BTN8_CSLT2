# A particular zoo determines the price of admission based on the age of the guest.
# Guests 2 years of age and less are admitted without charge. Children between 3 and
# 12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
# for all other guests is $23.00.
# Create a program that begins by reading the ages of all of the guests in a group
# from the user, with one age entered on each line. The user will enter a blank line to
# indicate that there are no more guests in the group. Then your program should display
# the admission cost for the group with an appropriate message. The cost should be
# displayed using two decimal places.

total_cost = 0
while True:
    age_input = input("Enter guest age:")
    if age_input == "":
        break
    
    guest_age = int(age_input)
    
    if guest_age != 0:
        if guest_age <= 2:
            personal_cost = 0.00
        elif guest_age in range(3,13):
            personal_cost = 14.00
        elif guest_age in range(13,65):
            personal_cost = 23.00
        else:
            personal_cost = 18.00
    # print(personal_cost)
    total_cost += personal_cost
print(f"The admission cost for the group is: {total_cost:.2f}")

    
    