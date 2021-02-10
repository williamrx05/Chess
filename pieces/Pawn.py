from pieces import ChessPiece
import ChessBoard, move, position

class Pawn(ChessPiece.ChessPiece):
    def __init__(self, side, pos):
        super().__init__("P", side, pos, 1)

    def ismovevalid(self, m: move, chessboard: ChessBoard) -> bool:
        if chessboard.iskingopen(m) or not chessboard.inbounds(m.getnew()):
            return False

        if m.xshift() == 0:
            if m.yshift() == self.side:
                temp = chessboard.pieceat(m.getnew())
                return not temp
            elif m.yshift() == 2*self.side and ((self.pos.gety() == 6 and self.side == -1) or (self.pos.gety() == 1 and self.side == 1)):
                onestep = position.position(self.pos.getx(), self.pos.gety() + self.side)
                temp1 = chessboard.pieceat(onestep)
                temp2 = chessboard.pieceat(m.getnew())
                return not temp1 and not temp2
        else:
            if m.yshift() == self.side and (m.xshift() == 1 or m.xshift() == -1):
                temp = chessboard.pieceat(m.getnew())
                return not not temp and temp.getside() == -self.side
        return False

    def validmoves(self, chessboard: ChessBoard) -> [list]:
        moves = []
        left = move.move(self.pos, -1, self.side)
        right = move.move(self.pos, 1, self.side)
        onestep = move.move(self.pos, 0, self.side)
        twostep = move.move(self.pos, 0, 2*self.side)
        if self.ismovevalid(left, chessboard):
            moves.append(left)
        if self.ismovevalid(right, chessboard):
            moves.append(right)
        if self.ismovevalid(onestep, chessboard):
            moves.append(onestep)
        if self.ismovevalid(twostep, chessboard):
            moves.append(twostep)
        return moves
