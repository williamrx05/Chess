import ChessBoard, ChessGame, position, move
from pieces import ChessPiece, Pawn, King, Knight, Bishop, Rook, Queen
from chessbot import value

game = ChessGame.ChessGame()
game.startgame()
print("State end value: " + value(game.getboard()))