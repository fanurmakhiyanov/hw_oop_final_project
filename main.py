from controller.Controller import Controller
from data.Meat import Meat
from data.Vegetables import Vegetables
from data.Basket import Basket

if __name__ == '__main__':
    controller = Controller()
    controller.put_foods(Meat("Victoria Secret", 100, 1, "3S"))
    controller.put_foods(Meat("Armani", 200, 2, "4S"))
    controller.put_foods(Meat("Gucci", 500, 1, "2M"))
    controller.put_foods(Vegetables("Jovvani", 350, 1, "red"))
    controller.put_foods(Vegetables("Mirage", 50, 1, "blue"))
    controller.show_foods_in_basket()
    controller.calculate_foods()