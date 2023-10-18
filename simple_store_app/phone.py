from item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"{broken_phones} should be greater than 0"

        # Initializing instance attributes
        self.broken_phones = broken_phones
