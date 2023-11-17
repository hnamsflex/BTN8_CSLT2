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
print(f"The admission cost for the group is: ${total_cost:.2f}")

    
    