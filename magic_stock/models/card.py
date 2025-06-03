class Card:
    """
    Represents a trading card with specific attributes.

    This class stores information about a card, such as its name, type, 
    condition, price, and available quantity.

    Attributes
    ----------
    name : str
        The name of the card.
    card_type : str
        The type or category of the card (e.g., Creature, Spell).
    condition : str
        The physical condition of the card (e.g., Near Mint, Played).
    price : float
        The price of the card.
    quantity : int
        The quantity of this card in stock.
    """
    def __init__(self, name, card_type, condition, price, quantity):
        self.name = name
        self.card_type = card_type
        self.condition = condition
        self.price = price
        self.quantity = quantity

class CardStock:
    """
    Manages a collection of Card objects representing a stock inventory.

    Provides methods to add new cards, display the list of cards, 
    update quantities, and delete cards from the stock.

    Attributes
    ----------
    cards : list of Cards
        A list containing the cards currently in stock.

    Methods
    -------
    add_new_card(name, card_type, condition, price, quantity)
        Creates a new Card and adds it to the stock.
    show_list()
        Prints the list of cards with details.
    remove_cards(index, quantity)
        Decreases the quantity of a card at the given index.
    add_cards(index, quantity)
        Increases the quantity of a card at the given index.
    del_card(index)
        Deletes the card at the given index from the stock.
    """
    def __init__(self):
        self.cards = []

    def add_new_card(self, name, card_type, condition, price, quantity):
        """
        Creates a new Card instance and appends it to the stock list.

        Parameters
        ----------
        name : str
            Name of the card.
        card_type : str
            Type/category of the card.
        condition : str
            Physical condition of the card.
        price : float
            Price of the card.
        quantity : int
            Quantity of the card to add.
        """
        new_card = Card(name, card_type, condition, price, quantity)
        self.cards.append(new_card)
    
    def show_list(self):
        """
        Prints all cards in the stock with their details.
        """
        for i, c in enumerate(self.cards, start=1):
            print(f'({i}) Name: {c.name} - Type: {c.card_type} - Condition: {c.condition} - Price: {round(c.price, 2)} - Quantity: {c.quantity}\n')
    
    def remove_cards(self, index, quantity):
        """
        Reduces the quantity of the specified card by the given amount.

        Parameters
        ----------
        index : int
            Index of the card in the stock list.
        quantity : int
            Number of cards to remove.
        """
        self.cards[index].quantity -= quantity
    
    def add_cards(self, index, quantity):
        """
        Increases the quantity of the specified card by the given amount.

        Parameters
        ----------
        index : int
            Index of the card in the stock list.
        quantity : int
            Number of cards to add.
        """
        self.cards[index].quantity += quantity

    def del_card(self, index):
        """
        Delete the entire card from the stock at the specified index.

        Parameters
        ----------
        index : int
            Index of the card in the stock list.
        """
        del(self.cards[index])