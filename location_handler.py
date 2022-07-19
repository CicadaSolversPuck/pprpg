class Location:
    x = 0
    y = 0

    def __str__(self):
        return f'({self.x}, {self.y})'

    def set_coordinates(self, x, y):
        self.x, self.y = x, y

    def move(self, direction, magnitude=1):
        # up
        if direction == 0:
            y += magnitude
        # down
        elif direction == 1:
            y -= magnitude

        # left
        elif direction == 2:
            x -= magnitude

        # right
        elif direction == 3:
            x += magnitude
