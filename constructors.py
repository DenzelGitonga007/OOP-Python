# Initialize the class
class Car:
    # Initialize the constructor
    def __init__(self, model, price):
        self.model = model #correctly assigns the model parameter to the object
        self.price = price
    # Use the str method
    def __str__(self):
        return "{} is worth {}".format(self.model, self.price)
# Create an instance of the class(object)
mercedes = Car("Kompressor", 3000000)
print("{} is worth {}".format(mercedes.model, mercedes.price))
print(mercedes) # If you print without the constructor method, it ought to use the str method

