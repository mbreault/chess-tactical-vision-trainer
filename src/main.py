import chess
import random

board = chess.Board()

## empty the board
board.clear_board()

## number of pieces to place on the board
pieces = 1

## add a random piece to the board
piece_type = random.randint(1, 6)
location = random.randint(0,63)
             
board.set_piece_at(chess.Square(location), chess.Piece(piece_type, chess.WHITE))

print(chess.piece_name(piece_type), chess.square_name(location))

moves =  ([chess.square_name(move.to_square) for move in board.legal_moves])
moves.sort()


with open(r"moves.txt", "w") as fp:
    fp.writelines(" ".join(moves))