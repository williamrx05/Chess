from pieces import ChessPiece
import ChessBoard, move, position

class King(ChessPiece.ChessPiece):
    def __init__(self, side, pos):
        super().__init__("K", side, pos, 999)

    def getASCII(self, side: int):
        if side == 1:
            return u'\u2654'
        else:
            return u'\u265A'

    def ismovevalid(self, m, chessboard) -> bool:
        if not chessboard.inbounds(m.getnew()):
            return False
        if -1 <= m.xshift() <= 1 and -1 <= m.yshift() <= 1:
            temp = chessboard.pieceat(m.getnew())
            return not temp or not (temp.getside() == self.side)
        else:
            return False

    def validmoves(self, chessboard) -> [move]:
        moves = []
        right = move.move(self.pos, 1, 0, False, "None")
        left = move.move(self.pos, -1, 0, False, "None")
        up = move.move(self.pos, 0, 1, False, "None")
        down = move.move(self.pos, 0, -1, False, "None")
        topright = move.move(self.pos, 1, 1, False, "None")
        topleft = move.move(self.pos, -1, 1, False, "None")
        bottomright = move.move(self.pos, 1, -1, False, "None")
        bottomleft = move.move(self.pos, -1, -1, False, "None")
        if self.ismovevalid(left, chessboard):
            moves.append(left)
        if self.ismovevalid(right, chessboard):
            moves.append(right)
        if self.ismovevalid(up, chessboard):
            moves.append(up)
        if self.ismovevalid(down, chessboard):
            moves.append(down)
        if self.ismovevalid(topright, chessboard):
            moves.append(topright)
        if self.ismovevalid(topleft, chessboard):
            moves.append(topleft)
        if self.ismovevalid(bottomright, chessboard):
            moves.append(bottomright)
        if self.ismovevalid(bottomleft, chessboard):
            moves.append(bottomleft)
        return moves