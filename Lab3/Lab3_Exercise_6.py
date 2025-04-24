class Car:
    def __init__(self, make, pos):
        self.make = make
        self.pos = pos

    def moving_distance(self, pos):
        self.pos += pos

    def show_pos(self):
        print(self.make , "current position : ", self.pos)

bmw = Car("BMW", 0)
bmw.show_pos()
bmw.moving_distance(15)
bmw.show_pos()