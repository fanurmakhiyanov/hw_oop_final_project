from data.Basket import Basket


class BasketService:
    def __init__(self):
        self.basket = Basket()

    def put_foods_in_basket(self, foods):
        basket_list = self.basket.get_basket_list()
        basket_list.append(foods)
        a = 1

    def get_basket_foods(self):
        return self.basket.get_basket_list()

    def calculate_foods(self):
        list_of_foods = self.basket.get_basket_list()
        total = 0
        for item in list_of_foods:
            total += item.get_price() * item.get_amount()

        return total