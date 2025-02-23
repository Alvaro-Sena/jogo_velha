import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Retorna o estado inicial do tabuleiro
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Retorna o jogador que tem a proxima jogada no tabuleiro
    """
    
    # Contador de jogadas
    count_X, count_O = 0, 0
    
    # Verificando o tabuleiro e contando as jogadas
    for rows in board:
        for cell in rows:
            if cell == X:
                count_X += 1
            elif cell == O:
                count_O += 1
                
    # Escolhendo a vez do jogador
    if not terminal(board) and count_X == count_O:
        return X
    elif count_X > count_O:
        return O

def actions(board):
    """
    Retorna o conjunto de todas as ações possíveis (i, j) disponíveis no tabuleiro
    """
    
    # Criando um conjunto de posições disponíveis
    places = set()
    
    # Verificando posições disponíveis
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                places.add((i, j))
    return places

def result(board, action):
    """
    Retorna o tabuleiro resultante após realizar o movimento (i, j)
    """
    
    # Verificando se a ação é válida:
    if action not in actions(board):
        raise ValueError("Ação inválida.")
    elif terminal(board):
        raise ValueError("Jogo encerrado.")
    
    modified_board = copy.deepcopy(board)
    # Atualizando o estado do tabuleiro
    modified_board[action[0]][action[1]] = player(board)
    return modified_board

def winner(board):
    """
    Retorna o vencedor do jogo, se houver um
    """
    
    # Verificando as células do tabuleiro
    if board[0][0] == board[0][1] == board[0][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[1][0] == board[1][1] == board[1][2] != None:
        if board[1][0] == X:
            return X
        else:
            return O
    elif board[2][0] == board[2][1] == board[2][2] != None:
        if board[2][0] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][0] == board[2][0] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][1] == board[1][1] == board[2][1] != None:
        if board[0][1] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][2] == board[2][2] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][1] == board[2][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][1] == board[2][0] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    else:
        return None

def terminal(board):
    """
    Retorna True se o jogo terminou, False caso contrário
    """
    
    # Verificando se todas as células estão preenchidas
    if winner(board) != None:
        return True
    
    # Verificando se ainda há células vazias
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

def utility(board):
    """
    Retorna 1 se X venceu o jogo, -1 se O venceu, 0 caso contrário
    """

    # Retornando quem é o vencedor
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Retorna a ação ótima para o jogador atual no tabuleiro.
    """

    # Se o tabuleiro estiver vazio, retorna o canto.
    if board == [[EMPTY]*3]*3:
        return (0, 0)
    
    if player(board) == X:
        v = float("-inf")
        selected_action = None
        for action in actions(board):
            minValueResult = minValue(result(board, action))
            if minValueResult > v:
                v = minValueResult
                selected_action = action
    elif player(board) == O:
        v = float("inf")
        selected_action = None
        for action in actions(board):
            maxValueResult = maxValue(result(board, action))
            if maxValueResult < v:
                v = maxValueResult
                selected_action = action
    return selected_action

def maxValue(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v
