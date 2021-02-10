import position
class move:
    def __init__(self, old: position, new: position):
        self.old = old
        self.new = new

    def __init__(self, old, x, y):
        self.old = old
        self.new = position.position(old.getx() + x, old.gety() + y)

    def xshift(self):
        return self.new.getx() - self.old.getx()

    def yshift(self):
        return self.new.gety() - self.old.gety()

    def getold(self):
        return self.old

    def getnew(self):
        return self.new

    def text(self) -> str:
        return self.old.text() + "->" + self.new.text()