# Creating a class
class Cars:
    pass #Used to indicate an empty body.

class Cars:
    # Declaring the attributes
    model = ""
    price = 0
# Creating the objects/instances of the class
mercedes = Cars()
mercedes.model = "Kompressor"
mercedes.price = 4000000
# Print the values
print("Mercedes {} is worth {}".format(mercedes.model, mercedes.price))
