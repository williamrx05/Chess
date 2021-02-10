class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def updatepos(self, x, y):
        self.x = x
        self.y = y

    def text(self)->str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"