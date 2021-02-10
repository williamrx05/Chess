import position, move

class ChessPiece:
    def __init__(self, name: str, side: int, pos: position, value: int):
        self.name = name
        self.side = side
        self.pos = pos
        self.value = value

    def setpos(self, pos: position):
        self.pos = pos

    def setside(self, side: int):
        self.side = side

    def ismovevalid(self, m, chessboard) -> bool:
        pass

    def validmoves(self, chessboard) -> [move]:
        pass

    def getvalue(self):
        return self.value

    def getpos(self):
        return self.pos

    def getname(self):
        return self.name

    def getside(self):
        return self.side
