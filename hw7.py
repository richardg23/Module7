#!/usr/bin/env python3

'''
This is a interactive program to display, add, delete and lookup users by 
selecting numeric integer 1 to 4. Selecting numeric integer 5 will quit the 
program.
I tried to do extra challenge(can you figure out how to delete a user by name OR username?).
However, I couldn't resolved it.
Here is a sample display when selecting username to be deleted:

Type in a number (1-5): 3
Remove User

Choose a Name or User name of User to be removed: songDude

You have selected songDude.
Traceback (most recent call last):
  File "hw7.py", line 72, in <module>
    choice[key] = value
TypeError: 'str' object does not support item assignment

This was the code:
                print("Remove User\n")
                choice = input("Choose a Name or User name of User to be removed: ")
                print("\nYou have selected {}.".format(choice))
                for key, value in usernames.items():
                    if choice == key:
                        del usernames[choice]
                    # Tried to do to delete by username. 
                    else:
                        choice[key] = value
                        del usernames[choice[key]]
'''

# library from "pip3 install sortedcontainers" terminal
from sortedcontainers import SortedDict


# function to display menu
def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    print()

# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

# display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    try: 
        # get menu choice from user
        menu_choice = int(input("Type in a number (1-5): "))  
        # view current entries
        if menu_choice == 1:
            try:
                print("Current Users:")
                for x,y in usernames.items():
                    print("Name: {} \tUser Name: {} \n".format(x,y))
            except:
                print("Please run the program again.")
               
        # add an entry
        elif menu_choice == 2:
            try:
                print("Add User")
                name = input("Name: ")
                username = input("User Name: ")
                usernames[name] = username
            except:
                print("Please run the program Ragain and enter valid user name.")
        
        # remove an entry
        elif menu_choice == 3:
            try:
                print("Remove User\n")
                name = input("Name: ")
                # It will delete the name(key-value pair of list usernames).
                if name in usernames:
                    # The syntax del will remove name and username in the list.
                    del usernames[name]                  
            except:
                print("Please check the name and username.")


        # view user name      
        elif menu_choice == 4:
            try:
                print("Lookup User")
                name = input("Name: ")
                # It will search the name(key of list usernames)
                if name in usernames:
                    # The below syntax will get the username based on the name.
                    display = usernames.get(name)
                    print("The username is {}.".format(display))
                else:
                    # If name is not in the list. It will display "Username not found!"
                    print("Username not found!")
            except:
                print_menu()
        
    
        # if user enters something strange, show them the menu
        elif menu_choice != 5:
            try:
                print_menu()
            except:
                print("Please run again the program.")

    except ValueError:
        print("Please enter an integer number not a string or float(e.g. 3.0). \nFor e.g. 1, 4 etc.. ")
