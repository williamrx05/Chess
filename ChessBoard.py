import move, position
from pieces import ChessPiece

class ChessBoard:
    def __init__(self):
        self.pieces = [[0 for _ in range(8)] for _ in range(8)]

    def addpiece(self, piece: ChessPiece):
        if self.inbounds(piece.getpos()):
            self.pieces[piece.getpos().gety()][piece.getpos().getx()] = piece

    def iskingopen(self, m: move) -> bool:
        return False

    def inbounds(self, pos: position):
        if 0 <= pos.gety() <= 7 and 0 <= pos.getx() <= 7:
            return True
        else:
            return False

    def pieceat(self, pos: position) -> ChessPiece:
        if self.inbounds(pos):
            return self.pieces[pos.gety()][pos.getx()]
        else:
            return None

    def printboard(self):
        for y in range(7, -1, -1):
            for x in range(8):
                pos = position.position(x, y)
                temp = self.pieceat(pos)
                if not temp:
                    print(" 0X ", end='')
                else:
                    s = "-" if temp.side < 0 else "+"
                    print(" " + s + temp.getname() + " ", end='')
            print("")
