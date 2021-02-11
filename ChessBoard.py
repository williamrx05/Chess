import move, position
from pieces import ChessPiece, Queen, King, Knight, Pawn, Rook, Bishop


class ChessBoard:
    def __init__(self):
        self.grid = [[0 for _ in range(8)] for _ in range(8)]
        self.min = position.position(-1, -1)
        self.max = position.position(8, 8)
        self.pieces = []

    def getpieces(self):
        return self.pieces

    def addpiece(self, piece: ChessPiece):
        if not piece:
            return False
        if self.inbounds(piece.getpos()):
            if piece.getname() == "K":
                if piece.getside() == -1:
                    self.min = piece.getpos()
                else:
                    self.max = piece.getpos()
            self.grid[piece.getpos().gety()][piece.getpos().getx()] = piece
            self.pieces.append(piece)

    def removepiece(self, pos: position):
        x = pos.getx()
        y = pos.gety()
        self.grid[y][x] = None
        for i in range(len(self.pieces)):
            if self.pieces[i] is not None and self.pieces[i].getpos() == pos:
                self.pieces[i] = None
                break


    def __deepcopy__(self, memodict={}):
        copy = type(self)()
        memodict[id(self)] = copy
        for piece in self.pieces:
            if piece is not None:
                pos = piece.getpos()
                newpiece = type(piece)(piece.getside(), pos)
                copy.addpiece(newpiece)
        # for x in range(8):
        #     for y in range(8):
        #         pos: position = position.position(x, y)
        #         piece = self.pieceat(pos)
        #         if piece:
        #             newpiece = type(piece)(piece.getside(), pos)
        #             copy.addpiece(newpiece)
        return copy

    def getking(self, side: int):
        if side == -1:
            return self.min
        else:
            return self.max

    def iskingopen(self, m: move) -> bool:
        memo = {}
        temp = self.__deepcopy__(memo)
        if temp.movepiece(m):
            side = temp.pieceat(m.getnew()).getside()
            for piece in self.pieces:
                if piece is not None:
                    pos = piece.getpos()
                    if piece.getside() == -side:
                        m2 = move.move(pos, temp.getking(side), False, "None")
                        if temp.movepiece(m2):
                            return True
            return False
            # for x in range(8):
            #     for y in range(8):
            #         pos = position.position(x, y)
            #         piece = temp.pieceat(pos)
            #         if piece and not piece.getname() == "K" and piece.getside() == -side:
            #             pos = piece.getpos()
            #             m2 = move.move(pos, temp.getking(side), False, "None")
            #             if temp.movepiece(m2):
            #                 return True
            # return False
        else:
            return True

    def ischeckmate(self, turn: int) -> bool:
        for piece in self.pieces:
            if piece and piece.getside() == turn:
                for m2 in piece.validmoves(self):
                    if not self.iskingopen(m2):
                        return False
        return True
        # for x in range(8):
        #     for y in range(8):
        #         pos = position.position(x, y)
        #         piece = self.pieceat(pos)
        #         if piece and piece.getside() == turn:
        #             for m2 in piece.validmoves(self):
        #                 if not self.iskingopen(m2):
        #                     return False
        # return True

    def movepiece(self, m: move, forced=False):
        piece: ChessPiece = self.pieceat(m.getold())
        if not forced and (not piece or not piece.ismovevalid(m, self)):
            return False
        self.removepiece(m.getnew())
        if m.gett():
            self.removepiece(m.getold())
            self.grid[piece.getpos().gety()][piece.getpos().getx()] = None
            new = m.getname()
            if new == "Q":
                newpiece = Queen.Queen(piece.getside(), m.getnew())
            elif new == "H":
                newpiece = Knight.Knight(piece.getside(), m.getnew())
            elif new == "R":
                newpiece = Rook.Rook(piece.getside(), m.getnew())
            elif new == "B":
                newpiece = Bishop.Bishop(piece.getside(), m.getnew())
            else:
                newpiece = Pawn.Pawn(piece.getside(), m.getnew()) # temporary uses only
            self.addpiece(newpiece)
        else:
            self.grid[piece.getpos().gety()][piece.getpos().getx()] = None
            self.grid[m.getnew().gety()][m.getnew().getx()] = piece
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
            return self.grid[pos.gety()][pos.getx()]
        else:
            return None

    def printboard(self):
        for y in range(7, -1, -1):
            print(str(y) + ".", end='')
            for x in range(8):
                pos = position.position(x, y)
                temp = self.pieceat(pos)
                if not temp:
                    # print(" " + str(x) + str(y) + " ", end='')
                    print(" `` ", end='')
                else:
                    s = "-" if temp.side < 0 else "+"
                    print(" " + s + temp.getname() + " ", end='')
            print("")
        print("  ", end='')
        for i in range(8):
            print(" ." + str(i) + " ", end='')
        print("")
