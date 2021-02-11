import ChessGame, ChessBoard, move, position
import random

def decision(probability):
    return random.random() < probability

game = ChessGame.ChessGame()
depth_max = 3
depth_min = 3
def result(s: ChessGame.ChessGame, m: move):
    memo = {}
    tb = s.getboard().__deepcopy__(memo)
    tg = ChessGame.ChessGame(tb)
    tg.makemove(m, True)
    return tg

def value(b: ChessBoard.ChessBoard):
    value = 0
    for x in range(8):
        for y in range(8):
            piece = b.pieceat(position.position(x, y))
            if piece:
                value += piece.getvalue() * piece.getside()
    return value

def max_value(s: ChessGame.ChessGame, d: int=depth_max):
    v = -9999
    d -= 1
    current = None
    memo = {}
    tb = s.getboard().__deepcopy__(memo)
    tg = ChessGame.ChessGame(tb)
    if s.getboard().ischeckmate(-1) or s.getboard().ischeckmate(1) or d == 0:
        return value(s.getboard())
    for action in tg.allmoves(1):
        prev = v
        v = max(v, min_value(result(tg, action), d))
        if not prev == v or not current:
            current = action
        if decision(0.2) and prev == v:
            current = action
    if d == depth_max - 1:
        game.makemove(current, True)
    return v


def min_value(s: ChessGame.ChessGame, d: int=depth_min):
    v = 9999
    d -= 1
    current = None
    memo = {}
    tb = s.getboard().__deepcopy__(memo)
    tg = ChessGame.ChessGame(tb)
    if s.getboard().ischeckmate(-1) or s.getboard().ischeckmate(1) or d == 0:
        return value(s.getboard())
    for action in tg.allmoves(-1):
        prev = v
        v = min(v, max_value(result(tg, action), d))
        if not prev == v or not current:
            current = action
        if decision(0.2) and prev == v:
            current = action
    if d == depth_min - 1:
        game.makemove(current, True)
    return v

for i in range(20):
    memo = {}
    tb = game.getboard().__deepcopy__(memo)
    tg = ChessGame.ChessGame(tb)
    side: int
    if i % 2 == 0:
        side = -1
    else:
        side = 1
    current = None
    while current == None:
        for action in tg.allmoves(side):
            if decision(0.1):
                current = action
    game.makemove(current, True)
    game.printboard()



while True:
    max_value(game)
    game.printboard()
    min_value(game)
    game.printboard()