import uuid
import copy
from typing import List, Tuple
from base_classes import User
from menu_dish import Menu, Dish  
from user_classes import Student, Teacher  

def linear_search(dish_list: List[Tuple[Dish, int]], target_dish: Dish) -> int:
    for idx, (d, _) in enumerate(dish_list):
        if d.name == target_dish.name:
            return idx
    return -1

class Cart:
    def __init__(self, user: User, menu: Menu):
        self.user: User = user        
        self.menu: Menu = menu        
        self.selected_dishes: List[Tuple[Dish, int]] = [] 

    def add_dish(self, dish_idx: int, num: int = 1) -> None:
        if not isinstance(dish_idx, int) or not isinstance(num, int):
            print("❌ Add failed: Index and quantity must be integer!")
            return
        dish = self.menu.get_dish_by_index(dish_idx - 1)
        if not dish:
            print("❌ Add failed: Dish does not exist!")
            return
        if num < 1:
            print("❌ Add failed: Quantity cannot be less than 1!")
            return
        find_idx = linear_search(self.selected_dishes, dish)
        if find_idx != -1:
            self.selected_dishes[find_idx] = (dish, self.selected_dishes[find_idx][1] + num)
            print(f"✅ Dish [{dish.name}] updated! Current quantity: {self.selected_dishes[find_idx][1]}")
            return
        self.selected_dishes.append((dish, num))
        print(f"✅ Dish [{dish.name}] ×{num} added to cart!")

    def remove_dish(self, dish_idx: int, num: int = 1) -> None:
        if not isinstance(dish_idx, int) or not isinstance(num, int):
            print("❌ Remove failed: Index and quantity must be integer!")
            return
        if len(self.selected_dishes) == 0:
            print("❌ Remove failed: Cart is empty!")
            return
        if dish_idx < 1 or dish_idx > len(self.selected_dishes):
            print("❌ Remove failed: Dish not in cart!")
            return
        if num < 1:
            print("❌ Remove failed: Quantity cannot be less than 1!")
            return
        dish, current_num = self.selected_dishes[dish_idx - 1]
        if num >= current_num:
            self.selected_dishes.pop(dish_idx - 1)
            print(f"✅ Dish [{dish.name}] removed from cart!")
        else:
            self.selected_dishes[dish_idx - 1] = (dish, current_num - num)
            print(f"✅ Dish [{dish.name}] reduced! Current quantity: {current_num - num}")

    def calculate_total(self) -> float:
        """计算折扣后总价：移除冗余判断 + 浮点数精度控制"""
        if len(self.selected_dishes) == 0:
            return 0.0
        total = 0.0
        discount = self.user.get_discount()
        for dish, num in self.selected_dishes:
            # 💡 修复：Teacher和Student共享student_price，Normal使用retail_price
            unit_price = dish.student_price if isinstance(self.user, (Student, Teacher)) else dish.retail_price
            total += round(unit_price, 2) * num * discount
        return round(total, 2)

    def show_cart(self) -> None:
        print("\n===== 🛒 My Cart =====")
        if not self.selected_dishes:
            print("  Cart is empty!")
            return
        total = self.calculate_total()
        for idx, (dish, num) in enumerate(self.selected_dishes, 1):
            # 💡 修复：统一通过多态获取正确的单价属性
            unit_price = round(dish.student_price if isinstance(self.user, (Student, Teacher)) else dish.retail_price, 2)
            discount_price = round(unit_price * self.user.get_discount(), 2)
            subtotal = round(discount_price * num, 2)
            print(f"  {idx}. {dish.name:12} ×{num:2} | Unit Price: ${discount_price:5.2f} | Subtotal: ${subtotal:6.2f}")
        print(f"  ————————————————————")
        print(f"  💰 Discounted Total: ${total:.2f}")

    def clear_cart(self) -> None:
        """清空购物车"""
        self.selected_dishes = []
        print("✅ Cart cleared!")

class Order:
    PENDING = "Pending"
    MAKING = "Being Made"
    COMPLETED = "Completed"

    def __init__(self, user: User, cart: Cart):
        self.order_id: str = str(uuid.uuid4())[:8]
        self.user_phone: str = user.phone          
        self.total_amount: float = cart.calculate_total()  
        self.status: str = self.PENDING             
        self.cart_detail: List[Tuple[Dish, int]] = copy.deepcopy(cart.selected_dishes)

    def update_status(self, new_status: str) -> None:
        status_list = [self.PENDING, self.MAKING, self.COMPLETED]
        if new_status not in status_list:
            print("❌ Status update failed: Invalid status!")
            return
        current_idx = status_list.index(self.status)
        new_idx = status_list.index(new_status)
        if new_idx == current_idx + 1:
            self.status = new_status
            print(f"✅ Order [{self.order_id}] status updated to: {self.status}")
        else:
            if current_idx < 2:
                print(f"❌ Status update failed! Current: [{self.status}], only allow: [{status_list[current_idx+1]}]")
            else:
                print("❌ Order is already completed! No more status updates.")

    def show_order_detail(self) -> None:
        print(f"\n===== 📄 Order Details [{self.order_id}] =====")
        print(f"  📞 User Phone: {self.user_phone}")
        print(f"  📊 Order Status: {self.status}")
        print(f"  💰 Total Amount: ${self.total_amount:.2f}")
        print(f"  📦 Dish Details:")
        if not self.cart_detail:
            print("    No dishes in this order!")
            return
        for dish, num in self.cart_detail:
            print(f"    · {dish.name} ×{num}")
