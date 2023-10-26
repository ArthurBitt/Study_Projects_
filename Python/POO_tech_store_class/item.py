import csv

class Item:

    #class atribute - every single instance has the same value 0.7
    discount = 0.8
    all = []



    #constructo magic method
    def __init__(self, name: str, price: float, quantity = 0): # default values force the type of data (quantity : int)


        # actions - assign to self objct/instance
        Item.all.append(self)
        

        # assert declaration run a verificantion in the arguments receveid
        assert price >=0 , f" price is not grater or equal {price}"
        assert quantity >=0, f" price is not grater or equal {quantity}"
        
        # every instance has the atribute with value passed in parameter
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        



    # getters and setters 

    @property # modify the encapsulation with __atribute and now, only setter methods can change the value of __name - no long work use object.atribute = new value
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, name):
        self.__name = name
        
    @property
    def price(self):
        return self.__price
    
    def calc_total_price(self):
        # using the atribute values of the instace who calls the method
        return self.__price * self.__quantity

    def apply_discount(self):
        self.__price *= self.discount
        return self.__price
    
    def increment_price(self, increment:float):
        self.__price = self.__price + self.__price * increment
        return self.__price


        # representation
    def __repr__(self) -> str:
        return f'class:{__class__.__name__} Product:{self.name} Price:{self.__price}$ Qt:{self.__quantity}'

        #methods

    

    # @static/classmethod can be called by class and instances - the main diference between then is the parameter/ class cls parameter is mandatory, self in static is not

    @classmethod
    def instantiate_from_csv(cls):
        with open("mycsv.csv","r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                print(item)
                # item(   # using get method and treating like a dictionary
                #     name = item.get('name'),
                #     price = float(item.get('price')),
                #     quantity = int(item.get('quantity'))
                # )
    
    @staticmethod
    def is_float(num):
        if isinstance(num, float):
            return num.is_integer() # return de method
        
        elif isinstance(num, int):
            return False
        else:
            return False
        



        # abstraction is run a function or system whitout the way how it works be visible - using __methods()/ private methods can be called only in class level
        # polymosphism is a concept that says one entity(functions, methods...) can refers multiple types - duck typing


                                # len(list); len(str); len(dict) - len methods explain the essence of plymorphism

                                # def quack(self)
                                    #return "duck says quack"
                                # def quack(self)
                                    #return "dog says auau"
                                # entity_dog.quack()>> "dog says auau"
                                # entity_duck.quack()>> "duck say quack"