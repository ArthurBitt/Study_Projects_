from item import Item
from phone import Phone

# Item.instantiate_from_csv()
item1 = Item('Notebook', 1000, 2)
# item1.name = "Kindle"
print(item1.name)



print(item1.price)
item1.increment_price(0.1)
print(item1.price)
# instances 
# item1 = Item('Phone', 100, 2)
# item2 = Item('Notebook', 1000, 3)

# reasigning the value of class atribute in item2 instance
# item2.discount = 0.7

# print("T.Price:", item2.calc_total_price())
# print("I.Price: ", item2.apply_discount())


# print(Item.__dict__) # magic atribute __dict__ returns the class atributes

# instances 
# item1 = Item('Notebook', 1000, 2)
# item2 = Item('Phone', 100, 3)
# item3 = Item('Laptop', 500, 4)
# item4 = Item('mouse', 40, 5)
# item5 = Item('cable', 10, 6)


# print(Item.all.__repr__())
# # item1.instantiate_from_csv()
# print(Item.is_float(7.0))