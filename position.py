class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, position):
            return self.x == other.x and self.y == other.y
        return False

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def updatepos(self, x, y):
        self.x = x
        self.y = y

    def text(self)->str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"