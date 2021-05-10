import math

def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for s in successors_of(state):
            v = max(v, min_value(s))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for s in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    state = argmax(successors_of(state), lambda a: min_value(a))
    return state

def user_select_pile(list_of_piles):
    '''
    Given a list of piles, asks the user to select a pile and then a split.
    Then returns the new list of piles.
    '''
    print("\n    Current piles: {}".format(list_of_piles))

    i = -1
    while i < 0 or i >= len(list_of_piles) or list_of_piles[i] < 3:
        print("Which pile (from 1 to {}, must be > 2)?".format(len(list_of_piles)))
        i = -1 + int(input())

    print("Selected pile {}".format(list_of_piles[i]))

    max_split = list_of_piles[i] - 1

    j = 0
    while j < 1 or j > max_split or j == list_of_piles[i] - j:
        if list_of_piles[i] % 2 == 0:
            print(
                'How much is the first split (from 1 to {}, but not {})?'.format(
                    max_split,
                    list_of_piles[i] // 2
                )
            )
        else:
            print(
                'How much is the first split (from 1 to {})?'.format(max_split)
            )
        j = int(input())

    k = list_of_piles[i] - j

    new_list_of_piles = list_of_piles[:i] + [j, k] + list_of_piles[i + 1:]

    print("    New piles: {}".format(new_list_of_piles))

    return new_list_of_piles

def computer_select_pile(state):
    new_state = minmax_decision(state)
    return new_state

def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    splittableStack = False
    for i in state:
        if i > 2:
            splittableStack = True
    return not splittableStack

def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    if len(state) % 2 == 0:
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
        if i > 2:
            index = state.index(i)
            a = math.floor(i / 2.0)
            b = math.ceil(i / 2.0)
            if a == b:
                a -= 1
                b += 1
            while a >= 1:
                stateCopy = state[:]
                stateCopy.pop(index)
                stateCopy.append(a)
                stateCopy.append(b)
                out.append(stateCopy)
                a -= 1
                b += 1

    return out


def display(state):
    print(state)
    


def main():
    state = [15]
    #print(successors_of([15]))
    while not is_terminal(state):
        state = user_select_pile(state)
        if not is_terminal(state):
            state = computer_select_pile(state)

    print("    Final state is {}".format(state))


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
