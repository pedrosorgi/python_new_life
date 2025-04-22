# Function to add a new card to the stock
def stock_up(product_list):
    new_card = input('Enter card name: ')
    card_type = input('Enter card type: ')
    card_condition = input('Enter card condition: ')
    
    # Loop to validate and get the card price, then convert it to float
    while True:
        card_price = input('Enter card price: ')
        try:
            card_price_float = float(card_price)
            break
        except ValueError:
            print('Invalid input option. Please enter a valid number for the price.')
    
    # Loop to validate the card quantity and convert to integer
    while True:
        card_quantity = input('Enter card(s) quantity: ')
        try:
            card_quantity_int = int(card_quantity)
            break
        except ValueError:
            print('Invalid input option. Please enter a valid number for the quantity.')

    # Create a dictionary with the card data
    cards = {
        'name': new_card,
        'type': card_type,
        'condition': card_condition,
        'price': card_price_float,
        'quantity': card_quantity_int
    }

    # Add the new card to the product list
    product_list.append(cards)


# Function to display all cards in the stock
def show_products(product_list):
    for p in product_list:
        print(f"\nCard name: {p['name']}\nCard type: {p['type']}\nCondition: {p['condition']}\nUnity card price: {p['price']}\nCard(s) quantity: {p['quantity']}")


# Function to update the quantity of an existing cards
def update_quantity(product_list):
    for i, product in enumerate(product_list):
        print(f"{i}-) Name: {product['name']}\nQuantity: {product['quantity']}")

    # Ask which card to update and validate the input
    while True:
        updated_card = input('Enter the number of the card to be updated: ')
        try:
            updated_card_int = int(updated_card)
            if 0 <= updated_card_int < len(product_list):
                break
            else:
                print('Invalid input option. Please enter a valid card number')
                continue
        except ValueError:
            print('Invalid input option. Please enter a valid card number.')
            continue
    
    # Ask the quantity of cards to update and validate the input
    while True:
        updated_card_quantity = input('Enter the quantity of cards to be updated: ')
        try:
            updated_card_quantity_int = int(updated_card_quantity)
            break
        except ValueError:
            print('Invalid input option. Please enter a valid quantity number.')
            continue
    
    # Ask for add or remove cards and validate the 
    while True:
        update_type = input('Do you want to add or remove cards? (a/r): ').upper()
        if update_type not in ('A', 'D'):
            print("Invalid input option. Please enter 'a' to add or 'r' to remove.")
            continue
        elif len(update_type) > 1:
            print("Invalid input option. Please enter 'a' to add or 'r' to remove.")
            continue
        else:
            break

    # Adding cards
    if update_type == 'A':
        product_list[updated_card_int]['quantity'] += updated_card_quantity_int
        print(f"{updated_card_quantity_int} card(s) added to {product_list[updated_card_int]['name']}.")
        print(f"Total: {product_list[updated_card_int]['quantity']} cards.")

    # Removing cards
    elif update_type == 'R':
        product_list[updated_card_int]['quantity'] -= updated_card_quantity_int
        print(f"{updated_card_quantity_int} card(s) removed from {product_list[updated_card_int]['name']}.")
        print(f"Total: {product_list[updated_card_int]['quantity']} cards.")




