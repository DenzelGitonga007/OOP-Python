# Using a variable inside the method
class Piglet:
    name = "dummy" # the object will have a name
    def speak(self):
        print("Oink! I am {}! Oink!".format(self.name))
# the object
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()
# Another instance of the class
petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

# Using the return keyword instead of print
class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18 #18 years to convert to human years
# piggy is 2 year old in human years, how old is he in pig years
piggy = Piglet()
piggy.years = 2
print("Pig is {} years old.".format(piggy.pig_years()))