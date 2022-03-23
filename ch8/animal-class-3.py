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
    def eat_leaves_from_trees(self):
        print('eating leaves')

reginald = Giraffe()
harold = Giraffe()
reginald.move()
harold.eat_leaves_from_trees()