# Using a variable inside the method
class Piglet:
    name = "dummy" # the object will have a name
    def speak(self):
        print("Oink! I am {}! Oink!".format(self.name))
# the object
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()
