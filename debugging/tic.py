#!/usr/bin/python3

def print_board(board):
    """
    Imprime el tablero de Tic-Tac-Toe.
    
    Parámetros:
    board (list): El tablero representado como una lista de listas.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Verifica si hay un ganador en el tablero.

    Parámetros:
    board (list): El tablero representado como una lista de listas.

    Retorna:
    bool: True si hay un ganador, False en caso contrario.
    """
    # Verifica filas
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Verifica columnas
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Verifica diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_tie(board):
    """
    Verifica si hay un empate en el juego (todas las casillas llenas y sin ganador).

    Parámetros:
    board (list): El tablero representado como una lista de listas.

    Retorna:
    bool: True si el juego ha terminado en empate, False en caso contrario.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Inicia el juego de Tic-Tac-Toe entre dos jugadores que alternan turnos.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)

        # Validar la entrada del usuario para filas y columnas
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter a number between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            # Verificar si hay un ganador después del movimiento
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break
            # Verificar si hay empate (tablero lleno sin ganador)
            if check_tie(board):
                print_board(board)
                print("It's a tie!")
                break
            # Cambiar de jugador
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
