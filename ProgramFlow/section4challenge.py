# allows users to choose from a list of options (1-9)
option = ""
while option != 0:
    option = int(input("\n"
                       "\tPlease choose from the list\n "
                       "\n 0. Exit \n 1. Learn {0} "
                       "\n 2. Learn {1} \n" " 3. Learn {2} \n 4. Learn {3} "
                       "\n 5. Learn {4} \n 6. Learn {5}"
                       "\n 7. Learn {6} \n 8. Learn {7} \n 9. Learn {8}"
                       " ".format("C", "Rust", "Python", "Java", "C++", "C#",
                                  "Assembly", "Ruby", "To Give Up")))
    if 1 <= option <= 9:
        print("\n You're chose to {}".format(option))
    elif option == 0:
        print("\n Exiting Program")
        break
    else:
        print("\n You're not learning :(")
