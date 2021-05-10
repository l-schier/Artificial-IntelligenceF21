def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    
    # Vertical can add  and state[i] = 'X'
    for i in range(0, 7, 3):
        if state[i] == state[i+1] and state[i+1] == state[i+2]:
            return True
    # Horizontal
    for i in range(0, 3):
        if state[i] == state[i+3] and state[i+3] == state[i+6]:
            return True
    # Diagonal
    if state[0] == state[4] and state[4] == state[8]:
         return True
       
    elif state[6] == state[4] and state[4] == state[2]:
        return True

    for i in state:
        if isinstance(i, int):
            return False
    return True
        

    


def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    
    for i in range(0, 7, 3):
        if state[i] == state[i+1] and state[i+1] == state[i+2]:
            if state[i] == 'X':
                return 1
            else:
                return -1
    # Horizontal
    for i in range(0, 3):
        if state[i] == state[i+3] and state[i+3] == state[i+6]:
            if state[i] == 'X':
                return 1
            else:
                return -1
    # Diagonal
    if state[0] == state[4] and state[4] == state[8]:
        if state[0] == 'X':
            return 1
        else:
            return -1
       
    elif state[6] == state[4] and state[4] == state[2]:
        if state[6] == 'X':
            return 1
        else:
            return -1
    return 0
    


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    out = []
    for i in state:
        stateCopy = state[:]
        if isinstance(i, int):
            stateCopy[i] = 'X'
            out.append((i, stateCopy))
    return out


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
