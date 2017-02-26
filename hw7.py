# -*- coding: utf-8 -*-
"""
Intro to Python HW 7
Created on Sat Feb 25 14:37:15 2017

@author: Chad Caron

notes: this program demonstrates user input handling from the command line.
"""
#added comment 

#from collections import OrderedDict
from sortedcontainers import SortedDict

"""
print( 'Regular dictionary')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print (k, v)
    
print ('\nOrderedDict:')
d = OrderedDict()
d['b'] = 'B'
d['a'] = 'A'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print (k, v)

print ('\nSortedDict:')
d = SortedDict()
d['a'] = 'A'
d['e'] = 'E'
d['c'] = 'C'
d['d'] = 'D'
d['b'] = 'B'


for k, v in d.items():
    print (k, v)
"""

def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a User Name')
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

#display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    try:
        menu_choice = int(input("Type in a number (1-5): "))
    except ValueError:
        print("Please input an INTEGER 1-5...")
        menu_choice = ()
        #raise ValueError
        
    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x,y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x,y))
            
    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        usernames[name] = username
        
    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        name = input("Name or Username: ")
        if name in usernames:# or name in usernames.values():
            #pass # delete that entry
            del usernames[name]
        elif name in list(usernames.values()):#stole this bit from stack overflow
            name2 = list(usernames.keys())[list(usernames.values()).index(name)]
            del usernames[name2]

    # view user name      
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        if name in usernames:
            print("the Username for {} is {}.".format(name, usernames[name]))
        else:
            print("the Username {} is not in the dictionary.".format(name))

    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print_menu()
