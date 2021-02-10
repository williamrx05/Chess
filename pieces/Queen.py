from pieces import ChessPiece, Rook, Bishop
import ChessBoard, move, position

class Queen(ChessPiece.ChessPiece):
    def __init__(self, side, pos):
        super().__init__("Q", side, pos, 9)

    def ismovevalid(self, m: move, chessboard: ChessBoard) -> bool:
        temprook = Rook.Rook(self.side, self.pos)
        tempbishop = Bishop.Bishop(self.side, self.pos)
        return temprook.ismovevalid(m, chessboard) or tempbishop.ismovevalid(m, chessboard)

    def validmoves(self, chessboard: ChessBoard) -> [move]:
        moves = []
        temprook = Rook.Rook(self.side, self.pos)
        tempbishop = Bishop.Bishop(self.side, self.pos)
        moves.extend(temprook.validmoves(chessboard))
        moves.extend(tempbishop.validmoves(chessboard))
        return moves