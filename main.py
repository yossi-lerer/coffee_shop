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