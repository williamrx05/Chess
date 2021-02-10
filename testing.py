import ChessBoard, position, move
from pieces import ChessPiece, Pawn, King, Knight, Bishop, Rook

position1 = position.position(1, 1)
position2 = position.position(0, 1)
position3 = position.position(2, 6)
position4 = position.position(1, 3)
position5 = position.position(0, 0)
position6 = position.position(4, 4)
position7 = position.position(2, 5)
position8 = position.position(3, 5)
position9 = position.position(0, 5)
board1 = ChessBoard.ChessBoard()
pawn1 = Pawn.Pawn(1, position1)
pawn2 = Pawn.Pawn(-1, position2)
pawn3 = Pawn.Pawn(1, position3)
king1 = King.King(1, position5)
king2 = King.King(1, position6)
knight1 = Knight.Knight(1, position7)
bishop1 = Bishop.Bishop(-1, position8)
rook1 = Rook.Rook(-1, position9)
board1.addpiece(pawn1)
board1.addpiece(pawn2)
board1.addpiece(pawn3)
board1.addpiece(king1)
board1.addpiece(king2)
board1.addpiece(knight1)
board1.addpiece(bishop1)
board1.addpiece(rook1)
board1.printboard()
print("Rook1 moves")
rook1moves = rook1.validmoves(board1)
for m in rook1moves:
    print(m.text())

#pawn1moves = pawn1.validmoves(board1)
# print("Pawn1 moves")
# for m in pawn1moves:
#     print(m.text())
# pawn2moves = pawn2.validmoves(board1)
# print("Pawn2 moves")
# for m in pawn2moves:
#     print(m.text())
# pawn3moves = pawn3.validmoves(board1)
# print("Pawn3 moves")
# for m in pawn3moves:
#     print(m.text())
# print("King1 moves")
# king1moves = king1.validmoves(board1)
# for m in king1moves:
#     print(m.text())
# print("King2 moves")
# king2moves = king2.validmoves(board1)
# for m in king2moves:
#     print(m.text())
# print("Knight1 moves")
# knight1moves = knight1.validmoves(board1)
# for m in knight1moves:
#     print(m.text())
# print("Bishop1 moves")
# bishop1moves = bishop1.validmoves(board1)
# for m in bishop1moves:
#     print(m.text())