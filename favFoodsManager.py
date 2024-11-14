favourite_foods = []  # empty list for latter use

while True:
    print("*****Favourite Foods Manager*****")
    print("0. Exit")
    print("1. Add foods")
    print("2. Remove Food")
    print("3. View all favourite foods")

    choice = input("Choose an option-> ")  # Taking user option to execute command

    if choice == "0":  # exit from the application
        print("Thank you for choosing Favourite Foods Manager")
        break

    elif choice == "1":  # add item in the list
        food = input("Enter your favourite food name: ")
        favourite_foods.append(food)
        print(f"{food} is added to the favourite food list")

    elif choice == "2":  # remove item in the list
        food = input("Enter the foods' name you want to REMOVE from favourite list-> ")
        if food in favourite_foods:  # searching for the item
            favourite_foods.remove(food)
            print(f"{food} is removed form the favourite list")
        else:  # not found case
            print(f"{food} doesn't exists in the favourite list")

    elif choice == "3":  # showing the full list
        if favourite_foods:
            print("*****Your favourite food list*****")
            for index, food in enumerate(favourite_foods, start=1):
                print(f"{index}.{food}")
            print("**********************************")
        else:  # if the list is empty
            print("Your favourite food list is empty")
    else:
        print("Invalid Choice")
