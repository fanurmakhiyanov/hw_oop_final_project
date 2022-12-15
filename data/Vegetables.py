from data.Foods import Foods

class Vegetables(Foods):
    
    def __init__(self, type_of_foods, price, amount, type_of_vegetable):
        super().__init__(type_of_foods, price, amount)
        self.type_of_vegetable = type_of_vegetable

    @property
    def get_type_of_vegetable(self):
        return self.type_of_vegetable

    def __str__(self):
        return f"Наименование продукта: {super().get_foods_name()}, Цена: {super().get_price()} руб., Количество: {super().get_amount()} кг, " \
                f"Тип овоща: {self.get_type_of_vegetable} "