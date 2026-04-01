def print_chessboard():
    # Chess pieces (Unicode)
    pieces = {
        'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟',
        'r': '♖', 'n': '♘', 'b': '♗', 'q': '♕', 'k': '♔', 'p': '♙'
    }
    
    # Initial position
    rows = [
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ['P'] * 8,
        ['.'] * 8,
        ['.'] * 8,
        ['.'] * 8,
        ['.'] * 8,
        ['p'] * 8,
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    ]
    
    # Print with coordinates
    print("   a  b  c  d  e  f  g  h")
    for i, row in enumerate(rows):
        print(f"{8-i}  {'  '.join(pieces.get(piece, piece) for piece in row)}  {8-i}")
    print("   a  b  c  d  e  f  g  h")

def print_pattern_board():
    print("\nPattern Board:")
    print("   a  b  c  d  e  f  g  h")
    for i in range(8):
        row = ""
        for j in range(8):
            if (i + j) % 2 == 0:
                row += "██"
            else:
                row += "░░"
        print(f"{8-i} {row} {8-i}")
    print("   a  b  c  d  e  f  g  h")

if __name__ == "__main__":
    print("Chess Board with Pieces:")
    print_chessboard()
    print_pattern_board()