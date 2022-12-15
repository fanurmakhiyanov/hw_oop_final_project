from controller.Controller import Controller
from data.Meat import Meat
from data.Vegetables import Vegetables
from data.Basket import Basket

controller = Controller()
controller.put_foods(Meat("Вырезка", 300, 2, "говядина"))
controller.put_foods(Meat("Окорок", 200, 1, "курица"))
controller.put_foods(Meat("Шейка", 500, 1, "свинина"))
controller.put_foods(Vegetables("Морковь", 80, 1, "органический"))
controller.put_foods(Vegetables("Картофель", 50, 3, "неорганический"))
controller.show_foods_in_basket()
controller.calculate_foods()