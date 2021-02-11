import ChessGame, ChessBoard, move, position

def result(b: ChessBoard.ChessBoard, m: move):
    memo = {}
    temp = b.__deepcopy__(memo)
    temp.movepiece(m, True)
    return temp

def value(b: ChessBoard.ChessBoard):
    value = 0
    for x in range(8):
        for y in range(8):
            piece = b.pieceat(position.position(x, y))
            if piece:
                value += piece.getvalue() * piece.getside()
    return value

