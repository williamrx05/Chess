from pieces import ChessPiece
import ChessBoard, move, position

class King(ChessPiece.ChessPiece):
    def __init__(self, side, pos):
        super().__init__("K", side, pos, 999)

    def ismovevalid(self, m, chessboard) -> bool:
        if chessboard.iskingopen(m) or not chessboard.inbounds(m.getnew()):
            return False
        if -1 <= m.xshift() <= 1 and -1 <= m.yshift() <= 1:
            temp = chessboard.pieceat(m.getnew())
            return not temp or not (temp.getside() == self.side)
        else:
            return False

    def validmoves(self, chessboard) -> [move]:
        moves = []
        right = move.move(self.pos, 1, 0, False)
        left = move.move(self.pos, -1, 0, False)
        up = move.move(self.pos, 0, 1, False)
        down = move.move(self.pos, 0, -1, False)
        topright = move.move(self.pos, 1, 1, False)
        topleft = move.move(self.pos, -1, 1, False)
        bottomright = move.move(self.pos, 1, -1, False)
        bottomleft = move.move(self.pos, -1, -1, False)
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