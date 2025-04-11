import os
from stock_functions.core import show_products, stock_up, update_quantity

# List to store all registered cards
card_list = []

# Main program loop
while True:
    print('Choose an option: ')
    print()
    entry = input('[R]egister Cards\n[U]pdate Quantities\n[S]how Stock\n\n-> ').upper()

    # Register a new cards
    if entry == 'R':
        os.system('cls')
        stock_up(card_list)
        user_continue = input('Would you like to register more cards? (y/n): ').upper()
        if user_continue == 'Y':
            os.system('cls')
            continue
        else:
            os.system('cls')
            entry = input('Would you like to update some card quantities? (y/n): ').upper()
            if entry == 'Y':
                os.system('cls')
                update_quantity(card_list)
                continue
            else:
                entry = input('Would you like to list the registered cards? (y/n): ').upper()
                if entry == 'Y':
                    os.system('cls')
                    show_products(card_list)
                    continue
                else:
                    entry = input('Go back to the main menu? (y/n): ').upper()
                    if entry == 'Y':
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print('Thanks for using the script. Goodbye!')
                        break

    # Try to update cards when none are registered
    elif entry == 'U' and len(card_list) == 0:
            os.system('cls')
            print('Sorry :( nothing to show here.')
            print()
            entry = input('Go back to the main menu? (y/n): ').upper()
            if entry == 'Y':
                os.system('cls')
                continue
            else:
                os.system('cls')
                print('Thanks for using the script. Goodbye!')
                break
                
    # Update existing cards
    elif entry == 'U':
        os.system('cls')
        update_quantity(card_list)
        user_continue = input('Would you like to update more cards? (y/n): ').upper()
        if user_continue == 'Y':
            os.system('cls')
            continue
        else:
            entry = input('Go back to the main menu? (y/n): ').upper()
        if entry == 'Y':
            os.system('cls')
            continue
        else:
            os.system('cls')
            print('Thanks for using the script. Goodbye!')
            break

    # Show message if stock is empty
    elif entry == 'S' and len(card_list) == 0:
        os.system('cls')
        print('Sorry :( nothing to show here.')
        print()
        entry = input('Go back to the main menu? (y/n): ').upper()
        if entry == 'Y':
            os.system('cls')
            continue
        else:
            os.system('cls')
            print('Thanks for using the script. Goodbye!')
            break

    # Show cards if there are any
    elif entry == 'S':
        os.system('cls')
        show_products(card_list)
        print()
        user_continue = input('Go back to the main menu? (y/n): ').upper()
        if user_continue == 'Y':
            os.system('cls')
            continue 
        else:
            print('Thanks for using the script. Goodbye!')
            break
            
    # Handling invalid options
    elif entry not in ('R', 'U', 'S'): # Modification for commit, upgrade in handling invalid options
        print('Invalid option. Please try again')
        continue
    
    # Handling invalid option len
    elif len(entry) > 1:
        print('Please enter only one option. Try again') 
        continue
