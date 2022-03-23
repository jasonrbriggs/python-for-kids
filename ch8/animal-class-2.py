class Thing:
    pass

class Animate(Thing):
    pass

class Animal(Animate):
    def breathe(self):
        pass
    def move(self):
        pass
    def eat_food(self):
        pass

class Mammal(Animal):
    def feed_young_with_milk(self):
        pass

class Giraffe(Mammal):
    def eat_leaves_from_trees(self):
        pass

reginald = Giraffe()
reginald.move()
reginald.eat_leaves_from_trees()
harold = Giraffe()
harold.move()