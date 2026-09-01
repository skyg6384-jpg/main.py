# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

# --------------------
# multiple inheritance
# --------------------

class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()

# ----------------------
# multilevel inheritance
# ----------------------

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):

    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Deer(Prey):
    pass

class Snake(Predator):
    pass

class Mouse(Prey, Predator):
    pass

deer = Deer("Bugs")
snake = Snake("Tony")
mouse = Mouse("Nemo")

deer.eat()
snake.eat()
mouse.eat()

deer.sleep()
snake.sleep()
mouse.sleep()

deer.flee()
snake.hunt()
mouse.hunt()
mouse.flee()