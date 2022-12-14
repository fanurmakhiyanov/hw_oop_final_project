from service.BasketService import BasketService as bs


class Console:
    def __init__(self):
        self.bs = bs()

    def show_foods_in_basket(self):
        for item in self.bs.get_basket_foods():
            print(item)

    def show_total_summ(self, value):
        print(f'Общая стоимость продуктов: {value} руб.')