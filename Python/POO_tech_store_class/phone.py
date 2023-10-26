from item import Item

class Phone(Item): # whitout inheritance (Item) - Phone instances wont be made, since the atributes are not declared 
   
   def __init__(self, name: str, price: float,broken_phone: int ,quantity=0 ):
       # call super() method to have full acess to all methods/atributes from Item 
        super().__init__(name, price, quantity)
        assert broken_phone >= 0 , f'Broken phones {broken_phone} is not greater or equal 0'
        self.bronken_phone = broken_phone
       