class Thing:
    pass

class Animate(Thing):
    pass

class Animal(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')

class Mammal(Animal):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffe(Mammal):
    def __init__(self, spots):
        self.giraffe_spots = spots
    def find_food(self):
        self.move()
        print('I\'ve found leaves!')
        self.eat_food()
    def eat_leaves_from_trees(self):
        print('tear leaves from branches')
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()

ozwald = Giraffe(100)
gertrude = Giraffe(150)
print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)