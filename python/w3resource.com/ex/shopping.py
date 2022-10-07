#!/usr/bin/python3

import os

shopping_list = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_help():
    print('what we should pick up at the store'.title())
    print('''
        Enter 'DONE' to stop adding  items.
        Enter 'HELP' for this help.
        Enter 'LIST' to see your current list.
        Enter 'REMOVE' to delete an item from your list.
    ''')


def add_to_list(new_item):
    if len(shopping_list):
        position = input("Where Should I Add {}\n"
                         "Press Enter To Add To End Of list\n"
                         "> ".format(new_item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None

    if position is not None:
        shopping_list.insert(position-1,new_item)
    else:
        shopping_list.append(new_item)

    show_list()


def show_list():
    clear_screen()
    print('Here\'s your list:')
    index = 1
    for item in shopping_list:
        print("{}. {}".format(index,item))
        index += 1


def remove_from_list(item):
    show_list()
    what_to_remove = input('What would you like to remove?\n> ')
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

show_help()


while True:
    new_item = input('> ')
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
    elif new_item.upper() == 'LIST':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list(new_item)
    else:
        add_to_list(new_item)

show_list()
