import os
import sys
from stock_functions.core import show_products, stock_up, update_quantity

# List to store all registered cards
card_list = []

# Main program loop
while True:
    print()
    print('Choose an option: ')
    print()
    entry = input('[R]egister Cards\n[U]pdate Quantities\n[S]how Stock\n------------\n[E]xit\n\n-> ').upper()

    # Register a new cards
    if entry == 'R':
        os.system('cls')
        stock_up(card_list)
        while True:
            user_continue = input('Would you like to register more cards? (y/n): ').upper()
            if user_continue == 'Y':
                os.system('cls')
                stock_up(card_list)
                continue
            else:
                os.system('cls')
                entry = input("Go back to the main menu? (y/n). Enter 'n' to exit: ").upper()
                if entry == 'Y':
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    sys.exit('Thanks for using the script. Goodbye!')

    # Try to update cards when none are registered
    elif entry == 'U' and len(card_list) == 0:
            os.system('cls')
            print('Sorry. Nothing to show here.')
            print()
            entry = input("Go back to the main menu? (y/n). Enter 'n' to exit: ").upper()
            if entry == 'Y':
                os.system('cls')
                continue
            else:
                os.system('cls')
                sys.exit('Thanks for using the script. Goodbye!')
                
    # Update existing cards
    elif entry == 'U':
        os.system('cls')
        update_quantity(card_list)
        print()
        while True:
            user_continue = input('Would you like to update more cards? (y/n): ').upper()
            if user_continue == 'Y':
                os.system('cls')
                update_quantity(card_list)
                continue
            else:
                os.system('cls')
                user_continue = input("Go back to the main menu? (y/n). Enter 'n' to exit: ").upper()
                if user_continue == 'Y':
                    os.system('cls')
                    break
                else:
                    os.system('cls')
                    sys.exit('Thanks for using the script. Goodbye!')

    # Show message if stock is empty
    elif entry == 'S' and len(card_list) == 0:
        os.system('cls')
        print('Sorry :( nothing to show here.')
        print()
        entry = input("Go back to the main menu? (y/n). Enter 'n' to exit: ").upper()
        if entry == 'Y':
            os.system('cls')
            continue
        else:
            os.system('cls')
            sys.exit('Thanks for using the script. Goodbye!')

    # Show cards if there are any
    elif entry == 'S':
        os.system('cls')
        show_products(card_list)
        print()
        user_continue = input("Go back to the main menu? (y/n). Enter 'n' to exit: ").upper()
        if user_continue == 'Y':
            os.system('cls')
            continue 
        else:
            os.system('cls')
            sys.exit('Thanks for using the script. Goodbye!')           
            
    elif entry == 'E':
        os.system('cls')
        sys.exit('Thanks for using the script. Goodbye!')

    # Handling invalid options
    elif entry not in ('R', 'U', 'S', 'E'): 
        print('Invalid option. Please try again')
        continue
    
    # Handling invalid option len
    elif len(entry) > 1:
        print('Please enter only one option. Try again') 
        continue
