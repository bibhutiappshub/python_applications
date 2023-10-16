from Item import Item

Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(10))
print(Item.is_integer(10.5))
print(Item.is_integer("Hello"))