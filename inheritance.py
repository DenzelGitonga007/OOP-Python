# Initialize the parent class
class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price
# Initialize a sibling
class Dodge(Car):
    pass # empty class
class Subaru(Car):
    pass # empty class


# Creating the objects
challenger = Dodge("Dodge Challeger", 3500000)
forester = Subaru("Subaru Forester", 2500000)
print(str(challenger.model) + " " + str(challenger.price))
print(str(forester.model) + " " + str(forester.price))