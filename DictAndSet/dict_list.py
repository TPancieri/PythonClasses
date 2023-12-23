available_parts = {"1": "computer",
                   "2": 'monitor',
                   "3": 'keyboard',
                   "4": 'mouse',
                   "5": 'hdmi cable',
                   "6": 'dvd drive',
                   }

current_choice = None
computer_parts = []
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            computer_parts.remove(chosen_part)
        else:
            computer_parts.append(chosen_part)
            print(chosen_part)
    else:
        print("Please choose an available part")
        for k, i in available_parts.items():
            print(k, i, sep=": ")
    print(computer_parts)
    current_choice = input("> ")
