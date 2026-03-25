## COMP2090SEF_course_project
![Python](https://img.shields.io/badge/Python-3.x-red)
![Status](https://img.shields.io/badge/Status-Completed-orangered)
![Type](https://img.shields.io/badge/Project-Campus%20Ordering%20System-orange)
![Use](https://img.shields.io/badge/Usage-Free%20Use-gold) 
![Run](https://img.shields.io/badge/Install-No%20Installation%20Required-yellow)

This repository contains [task1](#i) and [task2](#o). (Click on the task you want to see)

Group member: Cao Fei(13755803), Pan HaoWen(13752390),Xin YueYing(13795420)

## <a name="i"></a>🐡:task1 contents-a self-service ordering system
（Click on the contents you want to see)
- [User Guide](#guide1)
- [How did this idea come about?](#idea)
- [The overall functionalities of the system](#function)
- [What problems can be solved?](#problem)
- [Video](#video1)


## <a name = "guide1"></a>🚀:User Guide
1. Ensure you have Python 3.x installed on your local environment.
2. Clone this repository to your machine.

3. To execute the self-service ordering system, run:
```bash
python task1/main-system.py
```



## <a name = "video1"></a>🎥:Project Demonstration


## <a name="idea"></a>🧠:How did this idea come about?
This self-service ordering system is designed to address the common problems we face in daily campus life:

1➡️The cafeteria always has long lines during peak times, and it’s a big waste of time for both students and staff.

2➡️Cashiers often make mistakes when taking orders by hand, such as mixing up orders or giving wrong dishes, and the service is always slow due to these errors.

3➡️There was no clear digital way to track orders before, so both students and cafeteria workers often felt confused and unhappy with the service.

We want to build a simple and practical system based on OOP knowledge to automate the ordering process, reduce human mistakes, and allow everyone to easily the order progress. The system is designed to be modular, scalable, and easy to maintain, which aligns with the software design principles we learned in class.

This is the real menu record of HKMU Coffee:

<details>
	<summary>➡️Click here view HKMU Coffee menu photo </summary>
	<img src="https://github.com/user-attachments/assets/ad82172b-7525-43bb-b684-20872895e23d" alt="HKMU Coffee Menu 1" width="70%">
	<img src="https://github.com/user-attachments/assets/133a84d5-2a1c-40ca-b5ce-9ce48d1e1d7c" alt="HKMU Coffee Menu 2" width="70%">
    <img src="https://github.com/user-attachments/assets/3f131bad-b09c-4a48-9ab6-e51294c8fc06" alt="HKMU Coffee Menu 3" width="70%">
</details>


## <a name="function"></a>🤔: The overall functionalities of the system
1➡️ **Abstraction** hides complex implementation details and exposes only essential features (via abstract classes/methods).
- Dish and User in base_classes,py are abstract classes with @abstractmethod(These methods define a "contract" (required behavior) for subclasses but do not implement logic themselves.).

🌟for example:
 ```shell
    from abc import ABC, abstractmethod
    class Dish(ABC):
        def __init__(self, name, student_price, teacher_price, normal_price):
            self.name = name
            self.student_price = student_price  
            self.teacher_price = teacher_price  
            self.normal_price = normal_price   

        @abstractmethod
        def get_type(self):
            pass
 ```

2➡️ **Inheritance** allows a class to reuse code from a parent class and extend its functionality.eg: In the menu_dish.py, the parent calss is Dish. and the children class are Main Course, Snack, and Drink. 

🌟for example:

![image alt](https://github.com/caofei351-ops/A-self-service-ordering-system/blob/bf5d1e309110b66c0719e8fdad8a9e12d1b72837/Inheritance.png)

3➡️ **Polymorphism** allows different subclasses to implement the same method in unique ways which makse the code more flexible and scalable.

🌟for example:

(1) get-type() for Dishes
- MainCourse.get_type() → “Main Course"
- Snack.get_type() → “Snack"
- Drink.get_type() → “Drink"

The menu system (Menu.show_menu()) calls get_type() on any Dish subclass(no need to checj the exact type:
 ```shell
    type_dishes = [d for d in self.dishes if d.get_type() == t]
 ```
(2) get_discount() for Users
- Student.get_discount() → “0.9"(10% off)
- Teacher.get_discount() → “0.9"(10% off)
- NormalUser.get_discount() →“1.0"（no discount)

The cart (Cart.calculate_total()) uses user.get_discount():
 ```shell
    discount = self.user.get_discount() # work for any user subclass
 ```

4➡️ The **encapsulation** combines data (attributes) and the methods for operating on these data into a class, and restricts direct access to the internal state through access modifiers/conventions (Prevents invalid state and centralizes validation logic).

🌟for example:
- Private/Protected Attributes: SalesRecord uses _instance to enforce the Singleton pattern (prevents direct modification).
 ```shell
    class SalesRecord:
    _instance = None 
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
 ```
- Controlled Access via Methods: Instead of directly modifying balance, users call recharge() & Instead of directly changing selected_dishes, cart uses add_dish()/remove_dish().
```shell
    class Student(User):
    def recharge(self, amount):
        if amount >= 0:  # Validation logic
            self.balance += amount
        else:
            print("The amount cannot be negative!")
```
5➡️ **Singleton Pattern**:A specialized OOP pattern ensuring a class has only one instance (global access to a single object).

🌟for example:
- SalesRecord in sales_record.py implements Singleton to track total sales across the system:
```shell
    class SalesRecord:
    _instance = None  
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.total_sales = 0.0  
        return cls._instance
```
- The HKMUCoffeeSystem initializes self.sales_record = SalesRecord()—all orders share the same SalesRecord instance, so total sales are aggregated correctly.

6➡️ **Composition** uses objects of other classes as attributes to build complex functionality (Builds modular, reusable components).

🌟for example:
- Cart has-a User and Menu (depends on them to calculate totals/add dishes):
```shell
    class Cart:
    def __init__(self, user: User, menu: Menu):
        self.user: User = user        
        self.menu: Menu = menu   
```
- Order has-a copy of Cart details (uses copy.deepcopy to preserve order history):
```shell
    self.cart_detail: List[Tuple[Dish, int]] = copy.deepcopy(cart.selected_dishes)
```

## <a name="problem"></a>🦯:What problems can be solved?
The self-service Order system has successfully addressed several issues present in the old college Canteen System and offered practical implementations. Adopting Python's standard data types helps organise precise information at this stage that will be maintained after some time. This also fulfils all aspects as specified by our teacher in terms of the requirements outlined at Task 2:

1➡️Long waiting queues in peak hours
Long queues at the campus cafeteria during meal times, wasting about 10 to 20 minutes of everyone's time every day. There is also a system user interface that allows users to reserve in advance, via smartphones or computers; after the user books their own ordered food from other schools' canteens.

2➡️Frequent human errors in manual order-taking
Cashiers frequently mislabel dishes with respect to the flavours, portion sizes and customisations requested by users (e.g., providing hot pot soup without any seasonings for a spice-follower). Users can enter the menu to select dishes and set their own conditions, and everything is entered in a digital form; there will be no mistakes or misunderstandings at all during operation.

3➡️Lack of transparent order tracking for both sides
After manual order entry by user to obtain a menu selection, they will have their choices ignored until more meals are available for purchase. The system provides current order status (Pending/In progress/completed), which can be viewed by users; And display detailed content of the user and orders for management personnel to know all about this issue.

4➡️Troublesome, error-prone discount application for different groups
HKMU students and staff have a 10% dining concession; however, most clerks fail to issue the discount or miscount the total price at check-out time manually. At checkout, the system will determine whether it is a student, teacher or normal user by recognising the role; then apply discounts according to the current discount policy and calculate promptly for users.

5➡️Cafeteria’s lack of sales data for operational optimization
The cafeteria operator makes a decision based on their own observations without any evidence of sales. It leads to excess inventories of some goods and stockouts in others; as a result, considerable quantities of food are wasted due to improper handling. System's Sales record module can monitor the actual daily sales quantity and income of each dish to provide detailed information for restaurant managers to make reasonable Adjustments in terms of Menu structure and Inventory storage; Therefore, Reduce unnecessary purchases.

6➡️Difficult expansion of traditional manual dining systems
Frequenting the cafeteria daily is insufficient to assess its popularity; sales figures are unavailable for reference. The reason for this is an excessive purchase of certain raw materials due to lack of planning when ordering less-needed items in advance. The System's SalesRecord module records the actual sales volume and income per day of all dishes to provide specific Data basis for managers to Adjust menu Structure or Ingredient Procurement volumes to reduce food Wastage.

7➡️Disorganized dish and order data management (core data structure application)
Before this, the canteen used paper menus and Excel to record dishes and orders; These ways are slow in query time and operation efficiency. According to the built-in list and dictionary functions provided by Python's database construction in this study, an obvious purpose was set to meet actual business application requirements:

	●Lists: Store all the dishes' objects and cart-selected dish's object for quick lookup; Category Sorts (Filter by category): Main Course/Drink etc., which is suitable for situations where ordered, modifiable data set requires use of a set.

	● Dictionaries: Associate each separate order number with a specific instance of the order class that contains user data, dish details, payment methods, etc.; Save users' accounts in an ID-to-user object dictionary form; Perform quick lookup operations under O(1) time complexity based on these attributes. The standardised Data management approach can improve the Safety of the database and facilitate System Maintenance; Additionally, It also provides a basis for building additional Structure such As Binary Search Trees in order to quickly Retrieve information or heaps Sales-Data organization.

8➡️Unregulated user balance and sales data tracking
Manual record-keeping of users' meal balances and cafeteria's sales data is prone to errors due to typos, etc. The balance management function is included in the User class, with negative recharge checked; A SalesRecord single-instance Class was added to manage all-sale-related data at this time; Both use simple Data structures Types like Numeric Variables in Python to update and ensure the integrity of the data.



## <a name = "guide1"></a>🚀:User Guide
1. Ensure you have Python 3.x installed on your local environment.
2. Clone this repository to your machine.

3. To execute the data structure demonstration, run:
```bash
python filename.py
```

4. To execute the algorithm demonstration, run:
```bash
python filename.py
```





## <a name = "video1"></a>🎥:Project Demonstration




## <a name="o"></a>🐡:task2 contents- Circular Buffer and Search Algorithm 
(Click on the contents you want to see)
- [How is the code specifically implemented?](#code)
- [User Guide](#guide)
- [Video](#video)

## Data Structure 📊: Circular Buffer 

A Circular Buffer is a fixed-size structure that connects the end back to the beginning to form a loop. Unlike a standard queue, it allows the system to reuse memory by overwriting old data without shifting elements. This makes it ideal for handling continuous data streams in embedded systems where memory and performance are limited.

**Application Context:** This structure is a go-to choice for handling continuous data streams and managing queues efficiently. It’s especially useful in resource-constrained environments, like embedded systems, because it helps us avoid memory fragmentation while ensuring the system runs with steady, predictable performance.

**Implementation:**


## Algorithm ✅: A* (A-Star) Search Algorithm 

A* is a smart pathfinding algorithm that finds the shortest route between two points. It is much faster than Dijkstra’s algorithm because it uses a "heuristic" (an educated guess) to focus its search toward the destination rather than searching in all directions. It is the gold standard for GPS navigation and game AI.

**Application Context:** You’ll find A* everywhere—from pathfinding in video games to GPS mapping and autonomous drones. It’s the standard tool for calculating the most efficient route between a starting point and a destination, balancing speed and accuracy perfectly for real-world navigation.

**Implementation:**



## <a name = "code"></a>📁:How is the code specifically implemented?
*这里是要求的python源代码文件: Python implementation and basic test cases for the Circular Buffer data structure.
*这里是要求的python源代码文件: Python implementation and basic test cases for the A* Search Algorithm.

## <a name = "guide"></a>🚀:User Guide 

1. Ensure you have Python 3.x installed on your local environment.
2. Clone this repository to your machine.

3. To execute the data structure demonstration, run:
```bash
python filename.py
```

4. To execute the algorithm demonstration, run:
```bash
python filename.py
```

## <a name = "video"></a>🎥:Project Demonstration 
[the link to the video]
 


## <a name="update"></a>🕵️:Update
- **2026.01.29**: We formed our group and studied what Github is and how to use it.
- **2026.02.03**: We reviewed the specific requirements for the group project. At the same time we analyzed some project examples from the previous semester and Github. Finally, we chose the ordering system of HkMU coffee as our task 1.
- **2026.02.06**:The specific process of the code has been determined.
- **2026.02.06**:The specific division of labor for Task 1 has been determined.
- **2026.02.26**:The specific division of labor for Task 2 has been determined.
- **2026.02.27**The two topics of task 2 has been confirmed.
- **2026.02.28**:We finished the code for task1.
- 
  
## <a name="contact"></a>💙:Contact
If you have any questions about our project, please email us with `s1375580@live.hkmu.edu.hk`,`s1375239@live.hkmu.edu.hk`,`s1379542@live.hkmu.edu.hk`.

## <a name="x"></a>Non-Commercial Use Only Declaration
This project, A-self-service-ordering-system, is developed exclusively for educational purposes as part of the coursework for COMP2090SEF at Hong Kong Metropolitan University (HKMU).

1➡️	No Commercial Use: The software, source code and associated documentation may not be used, sold or distributed for any commercial, for-profit or revenue-generating purposes.

2➡️Attribution: Any use or modification of this work must retain the original team authorship and this non-commercial declaration.

3➡️No Warranty: The software is provided "as is" without any express or implied warranties; the team accepts no liability for any damages arising from the use of this system.

