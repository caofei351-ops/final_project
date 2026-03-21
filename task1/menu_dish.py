class Dish:
    def __init__(self, name, student_price, retail_price):
        self.name = name
        self.student_price = student_price
        self.retail_price = retail_price

    def get_type(self):
        raise NotImplementedError("Subclasses must implement get_type method")

class MainCourse(Dish):
    def get_type(self):
        return "Main Course"

class Snack(Dish):
    def get_type(self):
        return "Snack"

class Drink(Dish):
    def get_type(self):
        return "Drink"

class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        if isinstance(dish, Dish):
            self.dishes.append(dish)
        else:
            print("Add failed: Not a valid Dish object!")

    def show_menu(self):
        print("\n=== HKMUcoffee Menu ===")
        dish_types = ["Main Course", "Snack", "Drink"]
        type_titles = {
            "Main Course": "[Afternoon Tea]",
            "Snack": "[Hot Sandwiches]",
            "Drink": "[PREMIUM COFFEE]"
        }

        global_idx = 1

        for t in dish_types:
            print(f"\n{t} {type_titles[t]}")
            print(f"{'No.':<4} {'Name of dishes':<40} {'STAFF & STUDENT PRICE':<15} {'RETAIL PRICE':<10}")
            print("-" * 80)
            current_dishes = [d for d in self.dishes if d.get_type() == t]
            if not current_dishes:
                print("  No dishes available")
                continue
            for dish in current_dishes:
                print(f" {global_idx:<4}. {dish.name:<40} ${dish.student_price:<14} ${dish.retail_price:<10}")
                global_idx += 1

    def get_dish_by_index(self, actual_idx):
        if 0 <= actual_idx < len(self.dishes):
            return self.dishes[actual_idx]
        else:
            return None

    def init_default_dishes(self):
        # Main Course
        self.add_dish(MainCourse("All Day Breakfast", 54, 68))
        self.add_dish(MainCourse("Spaghetti Bolognese with Fried Egg Toast", 38, 45))
        self.add_dish(MainCourse("Nissin Demae Itcho with Two Toppings", 29, 36))
        self.add_dish(MainCourse("Shin Ramyun with Two Toppings", 34, 42))
        self.add_dish(MainCourse("Shrimp Toast with Quinoa Green Salad", 30, 36))
        self.add_dish(MainCourse("Korean Yugi Chicken Wings with Fries", 28, 36))
        self.add_dish(MainCourse("American Hot Dog with Fries", 29, 36))

        # Snack (Hot Sandwiches)
        self.add_dish(Snack("Avocado & Cheddar Cheese Panini", 37, 48))
        self.add_dish(Snack("Slow Cooked Chicken Caesar Panini", 37, 48))
        self.add_dish(Snack("Roast Beef, Wild Mushroom & Mustard Panini", 39, 50))
        self.add_dish(Snack("Honey Mustard & Smoked Salmon Panini", 39, 50))
        self.add_dish(Snack("Avocado & Quinoa Mexican Wrap", 33, 43))
        self.add_dish(Snack("Slow Cooked Chicken Caesar Mexican Wrap", 33, 43))
        self.add_dish(Snack("Roast Beef, Wild Mushroom & Honey Mustard Wrap", 35, 46))
        self.add_dish(Snack("Smoked Salmon & Egg Mexican Wrap", 35, 45))

        # Drinks
        self.add_dish(Drink("Double Espresso (2oz)", 16, 20))
        self.add_dish(Drink("Black Coffee", 19, 24))
        self.add_dish(Drink("White Coffee", 22, 28))
        self.add_dish(Drink("Cappuccino", 22, 28))
        self.add_dish(Drink("Caffè Latte", 22, 28))
        self.add_dish(Drink("Caffè Mocha", 27, 33))
        self.add_dish(Drink("Hazelnut Latte", 27, 33))
        self.add_dish(Drink("Caramel Latte", 27, 33))
        self.add_dish(Drink("Dirty Coffee", 31, 39))
        self.add_dish(Drink("Coffee Tonic", 31, 39))
        self.add_dish(Drink("Espresso Shot", 5, 5))
        self.add_dish(Drink("Change to Oat Milk", 5, 5))
        self.add_dish(Drink("Change to Skimmed Milk", 0, 0))

if __name__ == "__main__":
    menu = Menu()
    menu.init_default_dishes()
    menu.show_menu()
