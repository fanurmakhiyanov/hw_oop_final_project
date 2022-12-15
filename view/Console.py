from service.BasketService import BasketService


class Console:
    def __init__(self):
        self.BasketService = BasketService()

    def show_foods_in_basket(self):
        for item in self.BasketService.get_basket_foods():
            print(item)

    def show_total_summ(self, value):
        print(f'===================================================================\n Общая стоимость продуктов: {value} руб.')