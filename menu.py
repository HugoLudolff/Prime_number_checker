def menu():
    menu = """
===========MENU==========
[1] - Start
[2] - Prime range
[3] - Quit
=========================
--> """
    return input(menu)


def menu_numero():
    menu_numero = """
=======NUMBER=========
Enter a positive number 
or use 0(zero) to return to main menu
======================
-> """
    return int(input(menu_numero))