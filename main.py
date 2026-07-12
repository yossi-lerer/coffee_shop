# step 1 - Describe a Menu Item
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price        

    def describe(self):
        print(f"Item: {self.name} | Price: ${self.price}")

espresso = MenuItem("Espresso", 3.5)
espresso.describe()
# step 2 - Customer Greeting
class Customer:
    def __init__(self, name, favorite_drink):
        self.name = name
        self.favorite_drink = favorite_drink
        
    def greet(self):
        print(f"Hi! I am {self.name} and I would like a {self.favorite_drink}.")

customer_alice = Customer("Alice", "Latte")
customer_alice.greet()
# step 3 - Multiple Items with a Constructor
latte = MenuItem("Latte", 4.5)
croissant = MenuItem("Croissant", 2.0)
cold_brew = MenuItem("Cold Brew", 5.0)
latte.describe()
croissant.describe()
cold_brew.describe()
# step 4 - Can the Customer Afford It?
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def can_afford(self, price):
        if self.balance >= price:
            return True
        else:
            return False
bob = Customer("Bob", 10.0)
print(bob.can_afford(8.0))
print(bob.can_afford(12.0))
# step 5 - Track Item Stock
class MenuItem:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock
    def sell(self):
        self.in_stock = False
    def restock(self):
        self.in_stock = True
    def status(self):
        if self.in_stock == True:
            return f"{self.name} is in stock."
        else:
            return f"{self.name} is sold out."
muffin = MenuItem("Muffin", 2.5, True)
print(muffin.status())
muffin.sell()
print(muffin.status())
muffin.restock()
print(muffin.status())
