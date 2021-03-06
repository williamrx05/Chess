from pieces import ChessPiece
import ChessBoard, move, position

class Rook(ChessPiece.ChessPiece):
    def __init__(self, side, pos):
        super().__init__("R", side, pos, 5)

    def getASCII(self, side: int):
        if side == 1:
            return u'\u2656'
        else:
            return u'\u265C'

    def ismovevalid(self, m: move, chessboard: ChessBoard) -> bool:
        if not chessboard.inbounds(m.getnew()):
            return False
        if m.xshift() == m.yshift() == 0:
            return False
        elif m.xshift() != 0 and m.yshift() != 0:
            return False
        stepx = 0
        stepy = 0
        if m.xshift() != 0:
            stepx = int(m.xshift()/abs(m.xshift()))
        else:
            stepy = int(m.yshift()/abs(m.yshift()))
        for i in range(1, max(abs(m.xshift()), abs(m.yshift()))):
            pos = position.position(m.getold().getx() + i*stepx, m.getold().gety() + i*stepy)
            temp = chessboard.pieceat(pos)
            if not not temp:
                return False
        temp = chessboard.pieceat(m.getnew())
        return not temp or temp.getside() == -self.side

    def validmoves(self, chessboard: ChessBoard) -> [move]:
        moves = []
        for i in range(1, 9):
            m = move.move(self.pos, i, 0, False, "None")
            if self.ismovevalid(m, chessboard):
                moves.append(m)
            else:
                break
        for i in range(1, 9):
            m = move.move(self.pos, -i, 0, False, "None")
            if self.ismovevalid(m, chessboard):
                moves.append(m)
            else:
                break
        for i in range(1, 9):
            m = move.move(self.pos, 0, i, False, "None")
            if self.ismovevalid(m, chessboard):
                moves.append(m)
            else:
                break
        for i in range(1, 9):
            m = move.move(self.pos, 0, -i, False, "None")
            if self.ismovevalid(m, chessboard):
                moves.append(m)
            else:
                break
        return moves
