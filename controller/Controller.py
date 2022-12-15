from service.BasketService import BasketService
from view.Console import Console

class Controller:
    def __init__(self):
        self.basket_service = BasketService()
        self.console = Console()
        
    def put_foods(self, foods):
        self.basket_service.put_foods_in_basket(foods)
        
    def show_foods_in_basket(self):
        self.console.show_foods_in_basket()
        
    def calculate_foods(self):
        self.console.show_total_summ(self.basket_service.calculate_foods())