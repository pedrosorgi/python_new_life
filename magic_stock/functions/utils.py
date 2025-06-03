import os
import sys

def clear_screen():
    """
    Clears the terminal screen.

    This function clears the console screen to imrpive readability.
    """
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def ask_register_more_cards():
    """
    Asks the user if they want to register more cards.

    Returns
    -------
    str
        'Y' if the user wants to register more cards,
        'N' if the user does not want to register more.
    """
    while True:
        answer_register_more_cards = input('Would you like to register more cards? (y/n): ').upper()

        if answer_register_more_cards in ('Y', 'N'):
            return answer_register_more_cards
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def ask_update_more_cards():
    """
    Asks the user if they want to update more cards.

    Returns
    -------
    str
        'Y' if the user wants to update more cards,
        'N' if the user does not want to update more.
    """
    while True:
        answer_update_more_cards = input('Would you like to update more cards? (y/n): ').upper()

        if answer_update_more_cards in ('Y', 'N'):
            return answer_update_more_cards
        else:
            print("Invalid input. Please enter 'y' or 'n'.")    

def menu():
    """
    Display the program's main menu and get the user's choice.

    Returns
    -------
    str
        The user's choice, converted to uppercase. Possible options are:
        'R' for Register Cards,
        'U' for Update Quantities,
        'S' for Show Stock,
        'D' for Delete Card,
        'E' for Exit.
    """
    print()
    print('Choose an option: ')
    print()
    return input('[R]egister Cards\n[U]pdate Quantities\n[S]how Stock\n------------\n[D]elete Card\n[E]xit\n\n-> ').upper()

def back_menu():
    """
    Asks the user if they want to return to the main menu.

    Returns
    -------

    str 
        'Y' if the user wants to go back to the main menu, 
        'N' if the user wants to exit the program.
    """
    while True:
        back_menu_answer = input("Go back to the main menu? (y/n). Enter 'n' to exit: ").upper()
        if back_menu_answer in ('Y', 'N'):
            return back_menu_answer
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def show_nothing():
    """
    Displays a message when there are no cards in the stock.

    This function prints a notification informing that the product list is empty.
    """
    print('Sorry. Nothing to show here.')
    print()


def quit_program():
    """
    Clear terminal screen and exit the program.

    This function clears the console screen to improve readability before
    terminating the script with a goodbye message.
    """
    clear_screen()
    sys.exit('Thanks for using the script. Goodbye!')