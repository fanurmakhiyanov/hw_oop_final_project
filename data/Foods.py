class Foods:
    def __init__(self, type_of_foods, price, amount):
        self.__type_of_foods = type_of_foods
        self.__price = price
        self.__amount = amount
        
    def get_foods_name(self):
        return self.__type_of_foods
    
    def get_price(self):
        return self.__price
    
    def get_amount(self):
        return self.__amount
    
    
    