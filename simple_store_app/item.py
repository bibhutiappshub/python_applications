import csv


class Item:
    # Class level variable
    all = []
    pay_rate = 0.8

    def __init__(self, name, price, quantity):
        # Initializing instance attributes

        # Applying double underscore makes this a private variable.
        # Which is not accessible outside the class. We use @property decorator
        # to access it through "name" and at the same time restrict it from
        # re-assignment.

        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Run validation on certain attributes
        assert price >= 0, f"{price} should be greater than 0"
        assert quantity >= 0, f"{quantity} should be greater than 0"

        # Actions to perform
        Item.all.append(self)

    # To make any property readable and prevent reassignment we use @property decorator
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, value):
        self.__name = value

    @price.setter
    def price(self, value):
        self.__price = value

    # Readable representation of object
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def calculate_total_price(self):
        return self.price * self.quantity

    # To convert instance method to a class method use @classmethod decorators.
    # We convert this method because we need to access this on class level to create
    # instances by reading data from CSV file.

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(name=item["name"],
                 price=float(item["price"]),
                 quantity=int(item["quantity"])
                 )

    # Static method is just a regular function where no implicit class/object reference
    # passed into this function. We can create static methods by using
    # @staticmethod decorators.

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero.
        # For example 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False