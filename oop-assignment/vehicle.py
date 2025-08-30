# Assignment 2: Polymorphism Challenge! 

# --- Step 1: Create a base class (Parent) ---
class Vehicle:
    """A base class for all types of vehicles."""
    
    def __init__(self, name):
        self.name = name

    def move(self):
        """A generic move method that will be overridden by child classes."""
        print(f"{self.name} is moving in a generic way.")

# --- Step 2: Create child classes that inherit from Vehicle ---

class Car(Vehicle):
    """A Car class that inherits from Vehicle."""
    
    def move(self):
        """
        Overrides the parent's move method.
        This is the Car's specific implementation.
        """
        print(f"{self.name} is Driving 🚗...")

class Plane(Vehicle):
    """A Plane class that inherits from Vehicle."""
    
    def move(self):
        """
        Overrides the parent's move method.
        This is the Plane's specific implementation.
        """
        print(f"{self.name} is Flying ✈️...")

class Boat(Vehicle):
    """A Boat class that inherits from Vehicle."""
    
    def move(self):
        """
        Overrides the parent's move method.
        This is the Boat's specific implementation.
        """
        print(f"{self.name} is Sailing ⛵️...")


# --- Step 3: Demonstrate Polymorphism ---

# Create instances (objects) of each specific vehicle class.
my_car = Car("Toyota Camry")
my_plane = Plane("Boeing 747")
my_boat = Boat("Speedboat")
generic_vehicle = Vehicle("Generic Mover") # An instance of the parent class

# Create a list containing these different objects.
# Even though they are different types, they are all 'Vehicles'.
vehicles = [my_car, my_plane, my_boat, generic_vehicle]

print("--- Demonstrating Polymorphism in a Loop ---")
# Now, we can loop through the list and call the SAME method (.move()) on each object.
# Python will automatically figure out which version of move() to run for each object.
# This is the essence of polymorphism!
for vehicle in vehicles:
    vehicle.move()

print("\n--- Individual Method Calls ---")
# You can also call the methods directly, of course.
my_plane.move()
my_car.move()