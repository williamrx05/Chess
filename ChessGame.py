import ChessBoard, position, move
from pieces import Pawn, Bishop, King, Knight, Queen, Rook


class ChessGame:
    def __init__(self):
        self.board = ChessBoard.ChessBoard()
        self.turn = 1
        # Add Pawns
        for i in range(8):
            self.board.addpiece(Pawn.Pawn(+1, position.position(i, 1)))
            self.board.addpiece(Pawn.Pawn(-1, position.position(i, 6)))
        # Add Rooks
        self.board.addpiece(Rook.Rook(+1, position.position(0, 0)))
        self.board.addpiece(Rook.Rook(+1, position.position(7, 0)))
        self.board.addpiece(Rook.Rook(-1, position.position(0, 7)))
        self.board.addpiece(Rook.Rook(-1, position.position(7, 7)))
        # Add Knights
        self.board.addpiece(Knight.Knight(+1, position.position(1, 0)))
        self.board.addpiece(Knight.Knight(+1, position.position(6, 0)))
        self.board.addpiece(Knight.Knight(-1, position.position(1, 7)))
        self.board.addpiece(Knight.Knight(-1, position.position(6, 7)))
        # Add Bishops
        self.board.addpiece(Bishop.Bishop(+1, position.position(2, 0)))
        self.board.addpiece(Bishop.Bishop(+1, position.position(5, 0)))
        self.board.addpiece(Bishop.Bishop(-1, position.position(2, 7)))
        self.board.addpiece(Bishop.Bishop(-1, position.position(5, 7)))
        # Add Kings
        self.board.addpiece(King.King(+1, position.position(4, 0)))
        self.board.addpiece(King.King(-1, position.position(4, 7)))
        # Add Queens
        self.board.addpiece(Queen.Queen(+1, position.position(3, 0)))
        self.board.addpiece(Queen.Queen(-1, position.position(3, 7)))

    # Game loop
    def startgame(self):
        n = 0
        self.printboard()
        print("Turn " + str(n) + ": " + str(self.turn) + "'s move")
        while True:
            cmd = input("...")
            if cmd == "q":
                print(str(self.turn) + " resigned")
                break
            else:
                if len(cmd) >= 4 and cmd[0].isdigit() and cmd[1].isdigit() and cmd[2].isdigit() and cmd[3].isdigit():
                    pos1 = position.position(int(cmd[0]), int(cmd[1]))
                    piece = self.board.pieceat(pos1)
                    if not piece:
                        print("No piece exists at ({}, {})".format(cmd[0], cmd[1]))
                    elif not piece.getside() == self.turn:
                        print("Cannot move opponent's pieces")
                    elif piece.getname() == "P" and (piece.getpos().gety() == 1 and piece.getside() == -1) or (piece.getpos().gety() == 6 and piece.getside() == 1):
                        if len(cmd) >= 5:
                            if cmd[4] == "Q" or cmd[4] == "R" or cmd[4] == "B" or cmd[4] == "H":
                                pos2 = position.position(int(cmd[2]), int(cmd[3]))
                                m = move.move(pos1, pos2, True)
                                if self.ismovevalid(m):
                                    self.makemove(m, cmd[4])
                                    self.printboard()
                                    self.switchturn()
                                    if self.board.ischeckmate(self.turn):
                                        print("Checkmate. Player {} wins.".format(-self.turn))
                                        break
                                    n += 1
                                    print(str(n) + ": " + str(self.turn))
                                else:
                                    print("Move is invalid")
                            else:
                                print("Did not specific valid type")
                        else:
                            print("Must specify Q/R/B/H")
                    else:
                        pos2 = position.position(int(cmd[2]), int(cmd[3]))
                        m = move.move(pos1, pos2, False)
                        if self.ismovevalid(m):
                            self.makemove(m)
                            self.printboard()
                            self.switchturn()
                            if self.board.ischeckmate(self.turn):
                                print("Checkmate. Player {} wins.".format(-self.turn))
                                break
                            n += 1
                            print(str(n) + ": " + str(self.turn))
                        else:
                            print("Move is invalid")
                else:
                    print("Move cannot be parsed")

    def generateboards(self, m: [move]):
        pass

    def generateboard(self, m: move):
        pass

    # Returns all possible moves for one player
    def allmoves(self, side: int) -> [move]:
        moves = []
        for x in range(8):
            for y in range(8):
                moves.extend(self.piecemoves(position.position(x, y), side))
        return moves

    # Returns all possible moves for a piece
    def piecemoves(self, pos: position, side: int = None) -> [move]:
        moves = []
        piece = self.board.pieceat(pos)
        if not piece or (side and not side == piece.getside()):
            return moves
        for m in piece.validmoves(self.board):
            if self.ismovevalid(m):
                moves.append(m)
        return moves

    # Returns whether or not a move is valid
    def ismovevalid(self, m: move) -> bool:
        return not self.board.iskingopen(m)

    # Makes a move on board
    def makemove(self, m: move, new: str = "None"):
        self.board.movepiece(m, new)

    # Switches turns
    def switchturn(self):
        self.turn *= -1

    # Prints the chessboard
    def printboard(self):
        self.board.printboard()
