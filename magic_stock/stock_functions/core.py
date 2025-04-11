# Function to add a new card to the stock
def stock_up(product_list):
    new_card = input('Enter card name: ')
    card_type = input('Enter card type: ')
    card_condition = input('Enter card condition: ')
    
    # Get a card price and convert to float
    card_price = input('Enter card price: ')
    card_price_float = float(card_price)

    # Get a card quantity and convert to integer
    card_quantity = input('Enter card(s) quantity: ')
    card_quantity_int = int(card_quantity)

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

    # Ask which card to update
    updated_card = input('Enter the number of the card to be updated: ')
    updated_card_int = int(updated_card)
    
    # Ask how many cards to add
    updated_card_quantity = input('Enter the quantity of cards to be added: ')
    updated_card_quantity_int = int(updated_card_quantity)

    # Update the quantity of the selected card
    product_list[updated_card_int]['quantity'] += updated_card_quantity_int
    print(f"The card {product_list[updated_card_int]['name']} was updated with {updated_card_quantity_int} more card(s)!")
    print(f"Totaling {product_list[updated_card_int]['quantity']} cards.")
