import position
class move:
    def __init__(self, old: position, new: position, t: bool):
        self.old = old
        self.new = new
        self.t = t

    def __init__(self, old: position, x: int, y: int, t: bool):
        self.old = old
        self.new = position.position(old.getx() + x, old.gety() + y)
        self.t = t

    def xshift(self):
        return self.new.getx() - self.old.getx()

    def yshift(self):
        return self.new.gety() - self.old.gety()

    def getold(self):
        return self.old

    def getnew(self):
        return self.new

    def gett(self):
        return self.t

    def text(self) -> str:
        return self.old.text() + "->" + self.new.text() + str(self.t)