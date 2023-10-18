from item import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all)

# Let's say we have several phones in the store but some of them are broken. We can't sell
# those, that's why we need to calculate how many actual phones that we wanted to sell
# by subtracting number of broken phones from total number of phones available. The
# attribute is specific to the Phones so, we can't add class variable/instance variable
# into Item class and also the method inside Item class because it is relevant to
# Phones not for others.So, we will use inheritance for this case.
phone1 = Phone("iPhone14", 55000, 10, 1)
phone2 = Phone("Samsung Galaxy", 80000, 8, 1)
print(phone1.calculate_total_price())
print(Item.all)
print(Phone.all)

# Restrict the re-assignment of the name by using encapsulation.
item1 = Item("Watches", 25000, 5)
item1.name = "Bag" #This is possible and we have to restrict it by using encapsulation
item1.price = 60000 #This is possible and we have to restrict it by using encapsulation
print(item1.name)
print(item1.price)


