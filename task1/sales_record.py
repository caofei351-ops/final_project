class SalesRecord:
    _instance = None  

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.total_sales = 0.0  
        return cls._instance

    def add_sales(self, amount):
        self.total_sales += amount

    def get_total(self):
        return round(self.total_sales, 2)
