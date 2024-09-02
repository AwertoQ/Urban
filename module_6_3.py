class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def flu(self, dy):
        self.y_distance += dy
        return self.y_distance

class Pegasus(Horse, Eagle):
    sound = 'I train, eat, sleep, and repeat'
    def move(self, dx, dy):
        super().run(dx)
        super().flu(dy)

    def get_pos(self):
        pos = (self.x_distance, self.y_distance)
        return pos

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()