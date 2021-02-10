import ChessBoard, position, move
from pieces import ChessPiece, Pawn

position1 = position.position(1, 1)
position2 = position.position(0, 0)
position3 = position.position(2, 7)
position4 = position.position(1, 3)
board1 = ChessBoard.ChessBoard()
pawn1 = Pawn.Pawn(1, position1) #1, 1 side 1
pawn2 = Pawn.Pawn(-1, position2) #0, 2 side -1
pawn3 = Pawn.Pawn(1, position3)
board1.addpiece(pawn1)
board1.addpiece(pawn2)
board1.addpiece(pawn3)
board1.printboard()
pawn1moves = pawn1.validmoves(board1)
print("Pawn1 moves")
for m in pawn1moves:
    print(m.text())
pawn2moves = pawn2.validmoves(board1)
print("Pawn2 moves")
for m in pawn2moves:
    print(m.text())
pawn3moves = pawn3.validmoves(board1)
print("Pawn3 moves")
for m in pawn3moves:
    print(m.text())