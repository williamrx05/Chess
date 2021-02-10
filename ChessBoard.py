import move, position
from pieces import ChessPiece, Queen, King, Knight, Pawn, Rook, Bishop

class ChessBoard:
    def __init__(self):
        self.pieces = [[0 for _ in range(8)] for _ in range(8)]
        self.min = position.position(-1, -1)
        self.max = position.position(8, 8)

    def addpiece(self, piece: ChessPiece):
        if not piece:
            return False
        if self.inbounds(piece.getpos()):
            if piece.getname() == "K":
                if piece.getside() == -1:
                    self.min = piece.getpos()
                else:
                    self.max = piece.getpos()
            self.pieces[piece.getpos().gety()][piece.getpos().getx()] = piece

    def __deepcopy__(self, memodict={}):
        copy = type(self)()
        memodict[id(self)] = copy
        for x in range(8):
            for y in range(8):
                pos: position = position.position(x, y)
                piece = self.pieceat(pos)
                if piece:
                    newpiece = type(piece)(piece.getside(), pos)
                    copy.addpiece(newpiece)
        return copy

    def getking(self, side: int):
        if side == -1:
            return self.min
        else:
            return self.max

    def iskingopen(self, m: move) -> bool:
        memo = {}
        temp = self.__deepcopy__(memo)
        if temp.movepiece(m, "None"):
            side = temp.pieceat(m.getnew()).getside()
            for x in range(8):
                for y in range(8):
                    pos = position.position(x, y)
                    piece = temp.pieceat(pos)
                    if piece and not piece.getname() == "K" and piece.getside() == -side:
                        pos = piece.getpos()
                        m2 = move.move(pos, temp.getking(side), False)
                        if temp.movepiece(m2, "None"):
                            return True
        return False

    def ischeckmate(self, turn: int) -> bool:
        for x in range(8):
            for y in range(8):
                pos = position.position(x, y)
                piece = self.pieceat(pos)
                if piece and piece.getside() == turn:
                    for m2 in piece.validmoves(self):
                        if not self.iskingopen(m2):
                            return False
        return True

    def movepiece(self, m: move, new="None"):
        piece: ChessPiece = self.pieceat(m.getold())
        if not piece or not piece.ismovevalid(m, self):
            return False

        if m.gett():
            self.pieces[piece.getpos().gety()][piece.getpos().getx()] = None
            newpiece = None
            if new == "Q":
                newpiece = Queen.Queen(piece.getside(), m.getnew())
            elif new == "H":
                newpiece = Knight.Knight(piece.getside(), m.getnew())
            elif new == "R":
                newpiece = Rook.Rook(piece.getside(), m.getnew())
            else:
                newpiece = Bishop.Bishop(piece.getside(), m.getnew())
            self.pieces[m.getnew().gety()][m.getnew().getx()] = newpiece
        else:
            self.pieces[piece.getpos().gety()][piece.getpos().getx()] = None
            self.pieces[m.getnew().gety()][m.getnew().getx()] = piece
            piece.setpos(m.getnew())
            if piece.getname() == "K":
                if piece.getside() == -1:
                    self.min = piece.getpos()
                else:
                    self.max = piece.getpos()
        return True

    def getstate(self) -> int:
        return 0

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
                    print(" " + str(x) + str(y) + " ", end='')
                else:
                    s = "-" if temp.side < 0 else "+"
                    print(" " + s + temp.getname() + " ", end='')
            print("")
