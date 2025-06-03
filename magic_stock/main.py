"""
Main script for managing the Magic card stock.

Allows the user to register new cards, show the current stock,
update quantities, delete cards, and quit the program.
"""
from models.card import CardStock
from functions.stock_functions import stock_up, update_quantity, get_card_data, save_stock_to_json, load_stock_from_json, del_card
from functions.utils import clear_screen, quit_program, menu, back_menu, show_nothing, ask_register_more_cards, ask_update_more_cards
import os

stock = CardStock()

# Load existing stock data from JSON file
load_stock_from_json(stock)

while True:
    menu_choice = menu()

    # Register new cards
    if menu_choice == 'R':
        clear_screen()
        card_data = get_card_data()
        stock_up(stock, *card_data)
        save_stock_to_json(stock)

        # Ask if user wants to register more cards
        while True:
            user_answer = ask_register_more_cards()
            if user_answer == 'Y':
                clear_screen()
                card_data = get_card_data()
                stock_up(stock, *card_data)
                save_stock_to_json(stock)
                continue
            else:
                clear_screen()
                break
    
    # Show stock list (with empty stock check)
    elif menu_choice == 'S' and len(stock.cards) == 0:
        clear_screen()
        show_nothing()

        # Wait user to go back or quit
        while True:
            user_answer = back_menu()
            if user_answer == 'Y':
                clear_screen()
                break
            else:
                quit_program()

    # Show stock list
    elif menu_choice == 'S':
        clear_screen()
        stock.show_list()
        while True:
            user_answer = back_menu()
            if user_answer == 'Y':
                clear_screen()
                break
            else:
                quit_program()

    # Update stock quantity (with empty stock check)
    elif menu_choice == 'U' and len(stock.cards) == 0:
        clear_screen()
        show_nothing()

        # Wait user to go back or quit
        while True:
            user_answer = back_menu()
            if user_answer == 'Y':
                clear_screen()
                break
            else:
                quit_program()    

    # Update stock quantity
    elif menu_choice == 'U':
        clear_screen()
        update_quantity(stock)
        save_stock_to_json(stock)

        # Ask if user wants to update more cards
        while True:
            user_answer = ask_update_more_cards()
            if user_answer == 'Y':
                clear_screen()
                update_quantity(stock)
                save_stock_to_json(stock)
                continue
            else:
                clear_screen()
                break

        # Wait user to go back or quit
        while True:
            user_answer = back_menu()
            if user_answer == 'Y':
                clear_screen()
                break
            else:
                quit_program()

    # Quit program confirmation
    elif menu_choice == 'E':
        clear_screen()
        while True:
            user_answer = input('Would you like to quit the program? (y/n): ').upper()
            if user_answer == 'Y':
                quit_program()
            else:
                clear_screen()
                break
    
    # Delete card (with empty stock check)
    elif menu_choice == 'D' and len(stock.cards) == 0:
        clear_screen()
        show_nothing()

        # Wait user to go back or quit
        while True:
            user_answer = back_menu()
            if user_answer == 'Y':
                clear_screen()
                break
            else:
                quit_program()    

    # Delete card
    elif menu_choice == 'D':
        clear_screen()
        del_card(stock)
        save_stock_to_json(stock)
    
    # Handle invalid menu option
    elif menu_choice not in ('R', 'S', 'U', 'E', 'D'):
        print()
        print('Invalid menu option. Please try again.')
        continue
