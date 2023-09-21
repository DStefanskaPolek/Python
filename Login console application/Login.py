import os
import time
import re
import json


# clears screen after 2s delay
def clear_screen():
    time.sleep(2)
    os.system('cls')


# saves dictionary to json file, closes file afterward
def save_to_file(dictionary):
    with open("user_data.json", "w") as file:
        json.dump(dictionary, file)
    file.close()


# opens json file and saves data to dictionary
def read_from_file():
    with open("user_data.json", "r") as file:
        dictionary = json.load(file)
    file.close()
    return dictionary


# opens file in append mode / creates new one if not existing
def create_file():
    file = open("user_data.json", "a+")
    file.close()


# validates password with RegEx, matching pattern:
# (1 digit, 1 uppercase letter, 1 lowercase letter, minimum 8 characters)
# returns:
#  - true if password is correct,
#  - false if password is incorrect
def validate_password(password_arg):
    if re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8,}$", password_arg):
        return True
    else:
        return False


# checks the availability of the username
# the while loop continues until the user quits or provides a name that does not exist in the database
# returns:
#  - boolean (which makes it easier to quickly check the conditions when creating an account)
#  - a username from input
def create_name():
    global name
    is_name_correct = True

    print("Choose a username.")
    print("After creating your account,")
    print("you will not be able to change it.")

    while is_name_correct:
        name = input("Enter: ")

        if name.lower() == 'q':
            break
        elif name in users:
            print("Username is occupied. Try with different one or [Q]uit.")
        else:
            print("Username is available.")
            is_name_correct = False

    return is_name_correct, name


# checks the correctness of the username
# the while loop continues until the user quits or provides a correct password
# returns:
#  - boolean (which makes it easier to quickly check the conditions when creating an account)
#  - a password from input
def create_password():
    global password
    correct_password = False

    print("Create your password. You can change it later.")
    print("Password must contain at least:")
    print("- 1 uppercase letter")
    print("- 1 lowercase letter")
    print("- 1 digit")
    print("- 8 characters")

    while correct_password is not True:
        password = input("Enter: ")

        if password.lower() == 'q':
            break
        elif validate_password(password):
            print("Password correct.")
            correct_password = True
        else:
            print("Password is invalid. Try again.")

    return correct_password, password


# clears the console for aesthetic reasons only,
# creates a file if it doesn't already exist
# and saves user data into a dictionary
clear_screen()
create_file()
users = read_from_file()

# ensures that the program will run until the user decides to quit
while True:
    # for testing purposes
    print(users)
    for key, value in users.items():
        print(key, ":", value)
    print("There are", len(users), "users")
    print()
    # welcome page after starting the program
    print("Hello! Welcome to user options:")
    print()
    print("1. Create a new user")
    print("2. Log in to an existing account")
    print("[Q]uit")
    user_input = input("Enter your choice here: ")
    user_input = user_input.lower()

    match user_input:

        # 1. Create a new user
        case '1':
            # calls name and password creating functions
            # the returned data, i.e. boolean and user input, are saved to the variables
            clear_screen()
            is_name_existing, name = create_name()
            clear_screen()
            is_password_correct, password = create_password()

            # checks whether the username is free and whether the provided password is correct,
            # if the conditions are met, the dictionary with user data is expanded with a new user,
            # the entire dictionary is saved to the file again
            # and a message is displayed that the user creation was successful
            if is_name_existing is not True and is_password_correct is True:
                users.update({name: password})
                save_to_file(users)
                print("Account has been created. Welcome!")
                clear_screen()

        # 2. Log in to an existing account
        case '2':
            # sets the boolean variable to an initial value of false
            # to easily control the login status of an account
            clear_screen()
            is_login_success = False

            #  the loop allows the username to be re-entered until
            #   - the user exits the login page
            #  or
            #   - until the user is successfully logged in
            while is_login_success is not True:
                print("Log in to an existing account or [Q]uit.")
                name = input("Enter your username: ")

                # breaks the loop by the user's choice
                if name.lower() == 'q':
                    break
                # if the dictionary contains a user with the given username,
                # a password entry field is displayed
                elif name in users:

                    # the user has a total of 3 login attempts
                    for i in range(3):
                        password = input("Enter your password: ")

                        # if the password matches the one contained in the dictionary (at the appropriate index),
                        # the boolean value is changed to true
                        # and the loop breaks
                        if password == users[name]:
                            print("User logged in!")
                            is_login_success = True
                            break
                        # if the password is incorrect, a message is displayed
                        # along with the remaining number of attempts
                        # *i is in the range (0, 1, 2), therefore i == 1 displays the last attempt message*
                        elif i < 2:
                            print("Password is invalid. Try again. You have", 3 - (i + 1), end=" ")
                            # if i == 1:
                            #     print(3 - (i + 1), "attempt left.")
                            # else:
                            #     print(3 - (i + 1), "attempts left.")
                            print("attempt{plural} left.".format(plural="" if i == 1 else "s"))
                        # on the third incorrect attempt, access is denied
                        # and the loop returns to the beginning (Enter your username:)
                        else:
                            print("Password is invalid. Access denied.")
                            clear_screen()
                # if the user does not exist in the dictionary,
                # it is not possible to log in,
                # a message is displayed and the loop returns to the beginning (Enter your username:)
                else:
                    print("User does not exist.")
                    clear_screen()

                # the loop ensures that the user menu continues to display until
                #  - the user exits
                # or
                #  - the user logs out
                while is_login_success:
                    clear_screen()
                    print("Welcome back, " + name + "!")
                    print()
                    print("What do you want to do today?")
                    print("1. Change password")
                    print("2. Delete an account")
                    print("3. Log out")
                    user_input = input("Enter your choice here: ")
                    user_input = user_input.lower()

                    match user_input:

                        # 1. Change password
                        case '1':
                            # checks whether the provided password is correct,
                            # if so, the dictionary is updated with a new password,
                            # then it's saved to the file again,
                            # a message is displayed that the password change was successful
                            # and the user is logged out,
                            # the loop returns to the beginning (Enter your username:)
                            clear_screen()
                            is_password_correct, password = create_password()
                            users.update({name: password})
                            save_to_file(users)
                            print("New password set! User logged out!")
                            clear_screen()
                            is_login_success = False
                            break

                        # 2. Delete an account
                        case '2':
                            # confirmation question
                            user_input = input("Are you sure? [Y] or [N]: ")

                            # the user is removed from the dictionary,
                            # then the entire dictionary is saved to the file,
                            # a message about account deletion is displayed
                            # and the user is logged out,
                            # the loop returns to the beginning (Enter your username:)
                            if user_input.lower() == 'y':
                                users.pop(name)
                                save_to_file(users)
                                print("Account deleted!")
                                clear_screen()
                                is_login_success = False
                                break
                            # displays user menu page,
                            # without account deletion
                            elif user_input.lower() == 'n':
                                continue
                            # displays selection error message and user menu page
                            else:
                                print("Invalid choice.")

                        # 3. Log out
                        case '3':
                            # the appropriate message is displayed
                            # and user is logged out
                            # the loop returns to the beginning (Enter your username:)
                            print("User logged out!")
                            clear_screen()
                            is_login_success = False

                        # [Q]uit
                        # the loop returns to the original welcome page
                        case 'q':
                            break

                        # default case
                        # starts the loop over again in case of incorrect selection
                        case _:
                            print("Invalid choice.")
                            clear_screen()

        # [Q]uit
        case 'q':
            break

        # default case
        # starts the loop over again in case of incorrect selection
        case _:
            print("Invalid choice.")
            clear_screen()
