from pieces import ChessPiece
import ChessBoard, move, position

class Pawn(ChessPiece.ChessPiece):
    def __init__(self, side, pos):
        super().__init__("P", side, pos, 1)

    def ismovevalid(self, m: move, chessboard: ChessBoard) -> bool:
        if not chessboard.inbounds(m.getnew()):
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

    def validmoves(self, chessboard: ChessBoard) -> [move]:
        moves = []
        t = (self.pos.gety() == 1 and self.side == -1) or (self.pos.gety() == 6 and self.side == 1)
        changes = ["Q", "H", "B", "R"]
        left = []
        right = []
        onestep = []
        for change in changes:
            left.append(move.move(self.pos, -1, self.side, t, change))
        for change in changes:
            right.append(move.move(self.pos, 1, self.side, t, change))
        for change in changes:
            onestep.append(move.move(self.pos, 0, self.side, t, change))
        twostep = move.move(self.pos, 0, 2*self.side, False, "None")
        for i in range(3):
            if self.ismovevalid(left[i], chessboard):
                moves.append(left[i])
            if self.ismovevalid(right[i], chessboard):
                moves.append(right[i])
            if self.ismovevalid(onestep[i], chessboard):
                moves.append(onestep[i])
        if self.ismovevalid(twostep, chessboard):
            moves.append(twostep)
        return moves
