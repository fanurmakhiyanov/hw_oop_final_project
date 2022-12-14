from data.Foods import Foods

class Meat(Foods):
    
    def __init__(self, type_of_foods, price, amount, type_of_meat):
        super().__init__(type_of_foods, price, amount)
        self.type_of_foods = type_of_meat

@property
def get_type_of_meat(self):
    return self.type_of_meat

def __str__(self):
    return f"Мясо: {super().get_foods_name()}, Цена: {super().get_price()}, Сумма: {super().get_amount()}, " \
               f"Вид мяса: {self.get_type_of_meat} "