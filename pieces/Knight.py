from pieces import ChessPiece
import ChessBoard, move, position

class Knight(ChessPiece.ChessPiece):
    def __init__(self, side, pos):
        super().__init__("H", side, pos, 3)

    def ismovevalid(self, m, chessboard) -> bool:
        if not chessboard.inbounds(m.getnew()):
            return False
        if (abs(m.xshift()) == 2 and abs(m.yshift()) == 1) or (abs(m.xshift()) == 1 and abs(m.yshift()) == 2):
            temp = chessboard.pieceat(m.getnew())
            return not temp
        return False

    def validmoves(self, chessboard) -> [move]:
        moves = []
        ul = move.move(self.pos, -1, 2, False, "None")
        ur = move.move(self.pos, 1, 2, False, "None")
        ru = move.move(self.pos, 2, 1, False, "None")
        rd = move.move(self.pos, 2, -1, False, "None")
        dr = move.move(self.pos, 1, -2, False, "None")
        dl = move.move(self.pos, -1, -2, False, "None")
        ld = move.move(self.pos, -2, -1, False, "None")
        lu = move.move(self.pos, -2, 1, False, "None")
        if self.ismovevalid(ul, chessboard):
            moves.append(ul)
        if self.ismovevalid(ur, chessboard):
            moves.append(ur)
        if self.ismovevalid(ru, chessboard):
            moves.append(ru)
        if self.ismovevalid(rd, chessboard):
            moves.append(rd)
        if self.ismovevalid(dr, chessboard):
            moves.append(dr)
        if self.ismovevalid(dl, chessboard):
            moves.append(dl)
        if self.ismovevalid(ld, chessboard):
            moves.append(ld)
        if self.ismovevalid(lu, chessboard):
            moves.append(lu)
        return moves
