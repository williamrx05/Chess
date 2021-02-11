import position
class move:
    # def __init__(self, old: position, x: int, y: int, t: bool):
    #     self.old = old
    #     self.new = position.position(old.getx() + x, old.gety() + y)
    #     self.t = t

    def __init__(self, *args):
        if len(args) == 5:
            self.old = args[0]
            self.new = position.position(args[0].getx() + args[1], args[0].gety() + args[2])
            self.t = args[3]
        elif len(args) == 4:
            self.old = args[0]
            self.new = args[1]
            self.t = args[2]
        if self.t:
            self.name = args[len(args) - 1]
        else:
            self.name = "None"

    def getname(self) -> str:
        return self.name

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