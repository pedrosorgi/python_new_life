from models.card import Card
from functions.utils import clear_screen
import os
import json

def save_stock_to_json(stock, filename='python_new_life/magic_stock/stock.json'):
    """
    Saves the current stock of cards to a JSON file.

    Parameters
    ----------
    stock : Stock
        The stock object containing the list of cards.
    filename : str, optional
        The path to the JSON file where the data will be saved.
        Default is 'python_new_life/magic_stock/stock.json'.
    """
    data = []

    # Convert each card object into a dictionary
    for card in stock.cards:
        data.append({
            'name': card.name,
            'card_type': card.card_type,
            'condition': card.condition,
            'price': card.price,
            'quantity': card.quantity
        })

    # Write the list of card dictionaries to the JSON file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_stock_from_json(stock, filename='python_new_life/magic_stock/stock.json'):
    """
    Loads card data from a JSON file and adds it to the current stock.

    Parameters
    ----------
    stock : Stock
        The stock object where the loaded cards will be added.
    filename : str, optional
        The path to the JSON file to load from.
        Default is 'python_new_life/magic_stock/stock.json'.

    Notes
    -----
    If the JSON file does not exist, the function does nothing.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

            for card_data in data:
                card = Card(
                    card_data['name'],
                    card_data['card_type'],
                    card_data['condition'],
                    card_data['price'],
                    card_data['quantity'],
                )
                stock.cards.append(card)

    except FileNotFoundError:
        pass


def get_card_data():
    """
    Prompts the user to input card information.

    Returns
    -------
    tuple
        A tuple containing:
        - name : str
            The name of the card.
        - card_type : str
            The type of the card.
        - condition : str
            The condition of the card.
        - price : float
            The price of the card.
    """
    # Prompt user for card details
    name = input('Enter card name: ')
    card_type = input('Enter card type: ')
    condition = input('Enter card condition: ')
    
    # Loop to validate and get the card price as an float
    while True:
        price = input('Enter card price: ')
        try:
            price_float = float(price)
            break
        except ValueError:
            print('Invalid input option. Please enter a valid number for the price.')

    # Loop to validate and get the card quantity as an integer
    while True:
        quantity = input('Enter card(s) quantity: ')
        try:
            quantity_int = int(quantity)
            break
        except ValueError:
            print('Invalid input option. Please enter a valid number for the quantity.')

    return name, card_type, condition, price_float, quantity_int

def stock_up(stock, name, card_type, condition, price_float, quantity_int):
    """
    Adds a new card to the stock.

    Parameters
    ----------
    stock : Stock
        The stock object where the card will be added.
    name : str
        The name of the card.
    card_type : str
        The type of the card.
    condition : str
        The condition of the card ('Near Mint', 'Played').
    price_float : float
        The price of the card.
    quantity_int : int
        The quantity of the card to be added.
    """
    stock.add_new_card(name, card_type, condition, price_float, quantity_int)

def get_update_quantity_data(stock):
    """
    Prompts the user to select a card and specify how to update its quantity 
    (add or remove), including input validation.

    Parameters
    ----------
    stock : Stock
        The stock object containing the list of cards.

    Returns
    -------
    tuple
        A tuple containing:
        - update_type : str
            'A' to add cards or 'R' to remove cards.
        - updated_card_quantity_int : int
            The quantity of cards to update.
        - updated_card_int : int
            The index of the selected card in the stock list.
    """
    # Show the current stock list to the user
    stock.show_list()

    # Ask which card to update and validate the input
    while True:
        updated_card = input('Enter the number of the card to be updated: ')
        try:
            updated_card_int = int(updated_card) - 1
        except ValueError:
            print('Invalid input option. Please enter a valid card number.')
            continue

        if 0 <= updated_card_int < len(stock.cards):
            break
        else:
            print('Invalid input option. Please enter a valid card number')
            continue
    
    # Ask whether to add or remove cards and validate the input
    while True:
        update_type = input('Do you want to add or remove cards? (a/r): ').upper()
        if update_type not in ('A', 'R'):
            print("Invalid input option. Please enter 'a' to add or 'r' to remove.")
            continue
        else:
            break

    # Ask the quantity of cards to update and validate the input
    while True:
        updated_card_quantity = input('Enter the quantity of cards to be updated: ')
        try:
            updated_card_quantity_int = int(updated_card_quantity)
            break
        except ValueError:
            print('Invalid input option. Please enter a valid quantity number.')
            continue
        
     
    return update_type, updated_card_quantity_int, updated_card_int


def update_quantity(stock):
    """
    Updates the quantity of a card in the stock by adding or removing cards.

    The function prompts the user to select a card and choose whether to add 
    or remove a certain quantity. It includes validation to prevent negative stock.

    Parameters
    ----------
    stock : Stock
        The stock object containing the list of cards.
    """

    # Get the update data: card index, operation type (add/remove), and quantity
    update_type, updated_card_quantity_int, updated_card_int = get_update_quantity_data(stock)

    while True:
        # Adding cards
        if update_type == 'A':
            stock.add_cards(updated_card_int, updated_card_quantity_int)
            clear_screen()
            stock.show_list()
            print(f"{updated_card_quantity_int} card(s) added to {stock.cards[updated_card_int].name}")
            print(f"Total: {stock.cards[updated_card_int].quantity} cards.")
            break

        # Removing cards with validation to prevent negative stock
        elif update_type == 'R':
            if updated_card_quantity_int <= stock.cards[updated_card_int].quantity:
                stock.remove_cards(updated_card_int, updated_card_quantity_int)
                clear_screen()
                stock.show_list()
                print(f"{updated_card_quantity_int} card(s) removed from {stock.cards[updated_card_int].name}")
                print(f"Total: {stock.cards[updated_card_int].quantity} cards.")
                break
            else:
                print("Product quantity can't be negative. Please try again.")
                break

def get_card_delete_data(stock):
    """
    Prompts the user to select a card to be deleted from the stock.

    Displays the current stock list and asks the user to input the number 
    corresponding to the card. Includes input validation.

    Parameters
    ----------
    stock : Stock
        The stock object containing the list of cards.

    Returns
    -------
    int
        The index of the selected card to be deleted in the stock list.
    """
    # Display the current stock list to the user
    stock.show_list()

    # Ask which card to delete and validate the input
    while True:
        updated_card = input('Enter the number of the card to be deleted: ')
        try:
            updated_card_int = int(updated_card) - 1
        except ValueError:
            print('Invalid input option. Please enter a valid card number.')
            continue

        if 0 <= updated_card_int < len(stock.cards):
            break
        else:
            print('Invalid input option. Please enter a valid card number')
            continue
        
    return updated_card_int


def del_card(stock):
    """
    Deletes a card from the stock after user confirmation.

    Parameters
    ----------
    stock : Stock
        The stock object containing the list of cards."
    """
    # Get the index of the card to delete
    updated_card_int = get_card_delete_data(stock)
    card_to_delete = stock.cards[updated_card_int].name

    # Confirm deletion with the user
    while True:
        user_answer = input(f'The card {card_to_delete} will be deleted, are you sure? (y/n): ').upper()
        if user_answer not in ('Y', 'N'):
            print("Invalid input option. Please enter 'y' to confirme or 'n' to cancel.")
            continue
        
        if user_answer == 'Y':
            stock.del_card(updated_card_int)
            clear_screen()
            print(f'The card {card_to_delete} was successfully deleted.')
            break

        else:
            print()
            clear_screen()
            print('Operation cancelled.')
            break





        





