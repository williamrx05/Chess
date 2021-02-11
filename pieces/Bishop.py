from pieces import ChessPiece
import ChessBoard, move, position

class Bishop(ChessPiece.ChessPiece):
    def __init__(self, side, pos):
        super().__init__("B", side, pos, 3)

    def ismovevalid(self, m: move, chessboard: ChessBoard) -> bool:
        if not chessboard.inbounds(m.getnew()):
            return False
        if m.xshift() == 0 or abs(m.xshift()) != abs(m.yshift()):
            return False
        x = int(m.xshift()/abs(m.xshift()))
        y = int(m.yshift()/abs(m.yshift()))
        if abs(m.xshift()/m.yshift()) == 1:
            for i in range(1, abs(m.xshift())):
                pos = position.position(m.getold().getx() + x*i, m.getold().gety() + y*i)
                temp = chessboard.pieceat(pos)
                if not not temp:
                    return False
            temp = chessboard.pieceat(m.getnew())
            return not temp or temp.getside() == -self.side
        else:
            return False

    def validmoves(self, chessboard: ChessBoard) -> [move]:
        moves = []
        for i in range(1, 9):
            m = move.move(self.pos, i, i, False, "None")
            if self.ismovevalid(m, chessboard):
                moves.append(m)
            else:
                break
        for i in range(1, 9):
            m = move.move(self.pos, -i, i, False, "None")
            if self.ismovevalid(m, chessboard):
                moves.append(m)
            else:
                break
        for i in range(1, 9):
            m = move.move(self.pos, i, -i, False, "None")
            if self.ismovevalid(m, chessboard):
                moves.append(m)
            else:
                break
        for i in range(1, 9):
            m = move.move(self.pos, -i, -i, False, "None")
            if self.ismovevalid(m, chessboard):
                moves.append(m)
            else:
                break
        return moves
