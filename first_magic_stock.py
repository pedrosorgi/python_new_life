import os

def stock_up(product_list):
    new_card = input('Enter card name: ')
    card_type = input('Enter card type: ')
    card_condition = input('Enter card condition: ')

    card_price = input('Enter card price: ')
    card_price_float = float(card_price)

    card_quantity = input('Enter card(s) quantity: ')
    card_quantity_int = int(card_quantity)

    cartas = {
        'name': new_card,
        'type': card_type,
        'condition': card_condition,
        'price': card_price_float,
        'quantity': card_quantity_int
    }

    product_list.append(cartas)


def show_products(product_list):
    for p in product_list:
        print(f"\nCard name: {p['name']}\nCard type: {p['type']}\nCondition: {p['condition']}\nUnity card price: {p['price']}\nCard(s) quantity: {p['quantity']}")

def update_quantity(product_list):
    for i, product in enumerate(product_list):
        print(f"{i}-) Name: {product['name']}\nQuantity: {product['quantity']}")
    
    updated_card = input('Enter the number of the card to be updated: ')
    updated_card_int = int(updated_card)

    updated_card_quantity = input('Enter the quantity of cards to be added: ')
    updated_card_quantity_int = int(updated_card_quantity)

    product_list[updated_card_int]['quantity'] += updated_card_quantity_int
    print(f"The card {product_list[updated_card_int]['name']} was updated with {updated_card_quantity_int} more card(s)!")
    print(f"Totaling {product_list[updated_card_int]['quantity']} cards.")

card_list = []

while True:
    print('Choose an option: ')
    print()
    entry = input('[R]egister Cards\n[U]pdate Quantities\n[S]how Stock\n\n-> ').upper()

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
    
    elif entry not in 'RUS':
        print('Invalid option. Please try again')
        continue