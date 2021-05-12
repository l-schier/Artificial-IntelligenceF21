import numpy as np
from numpy.core.numeric import Infinity
from numpy.lib.function_base import append

"""
Hidden Markov Model using Viterbi algorithm to find most
likely sequence of hidden states.

The problem is to find out the most likely sequence of states
of the weather (hot, cold) from a describtion of the number
of ice cream eaten by a boy in the summer.
"""


def main():
    np.set_printoptions(suppress=True)

    states = np.array(["initial", "hot", "cold", "final"])

    # To simulate starting from index 1, we add a dummy value at index 0
    observationss = [
        [None, 3, 1, 3],
        [None, 3, 3, 1, 1, 2, 2, 3, 1, 3],
        [None, 3, 3, 1, 1, 2, 3, 3, 1, 2]
    ]

    # Markov transition matrix
    # transitions[start, end]
    transitions = np.array([[.0, .8, .2, .0],  # Initial state
                            [.0, .6, .3, .1],  # Hot state
                            [.0, .4, .5, .1],  # Cold state
                            [.0, .0, .0, .0],  # Final state
                            ])

    # P(v|q)
    # emission[state, observation]
    emissions = np.array([[.0, .0, .0, .0],  # Initial state
                          [.0, .2, .4, .4],  # Hot state
                          [.0, .5, .4, .1],  # Cold state
                          [.0, .0, .0, .0],  # Final state
                          ])

    for observations in observationss:
        print("Observations: {}".format(' '.join(map(str, observations[1:]))))

        probability = compute_forward(states, observations, transitions, emissions)
        print("Probability: {}".format(probability))

        path = compute_viterbi(states, observations, transitions, emissions)
        print("Path: {}".format(' '.join(path)))

        print('')


def inclusive_range(a, b):
    return range(a, b + 1)


def compute_forward(states, observations, transitions, emissions):
    # number of states - subtract two because "initial" and "final" doesn't count.
    big_n = len(states) - 2

    # number of observations - subtract one, because a dummy "None" is added on index 0.
    big_t = len(observations) - 1

    # final state
    f = big_n + 1

    # probability matrix - all values initialized to 5, as 0 has meaning in the matrix
    forward = np.ones((big_n + 2, big_t + 1)) * 5
    for s in range(1, big_n):
        forward[s,1] = transitions[0,s] * emissions[s,observations[1]]
    for t in range(2, big_t):
        for s in range(1, big_n):
            for sS in range(1, big_n):
                forward[s,t] += forward[sS, t - 1] * transitions[sS, s] * emissions[s, observations[t]]
    for s in range(1, big_n):
        forward[f, big_t] += forward[s, big_t] * transitions[s, f]
    return forward[f, big_t]
    


def compute_viterbi(states, observations, transitions, emissions):
    # number of states - subtract two because "initial" and "final" doesn't count.
    big_n = len(states) - 2

    # number of observations - subtract one, because a dummy "None" is added on index 0.
    big_t = len(observations) - 1

    # final state
    f = big_n + 1

    # probability matrix - all values initialized to 5, as 0 is valid value in matrix
    viterbi = np.ones((big_n + 2, big_t + 1)) * 5

    # Must be of type int, otherwise it is tricky to use its elements to index
    # the states
    # all values initialized to 5, as 0 is valid value in matrix
    backpointers = np.ones((big_n + 2, big_t + 1), dtype=int) * 5
    
    for s in range(1, big_n):
        viterbi[s, 1] = transitions[0, s] * emissions[s, observations[1]]
        backpointers[s, 1] = 0
    for t in range(2, big_t):
        for s in range(1, big_n):
            maxViter = -Infinity
            for ss in range(1, big_n):
                temp = viterbi[ss, t - 1] * transitions[ss, s] * emissions[s, observations[t]]
                if temp > maxViter:
                    maxViter = temp
            backArgmax = []
            for ss in range(1, big_n):
                backArgmax.append(viterbi[ss, t - 1] * transitions[ss, s])
            viterbi[s, t] = maxViter
            backpointers[s, t] = argmax(backArgmax)
    maxViter = -Infinity
    for s in range(1, big_n):
        temp = viterbi[s, big_t] * transitions[s, f]
        if temp > maxViter:
            maxViter = temp
    backArgmax = []
    for s in range(1, big_n):
        backArgmax.append(viterbi[s, big_t] * transitions[s, f])
    
    viterbi[f, big_t] = maxViter
    backpointers[f, big_t] = argmax(backArgmax)
    
    out = []
    ff = backpointers[f, big_t]
    for t in range(1, big_t):
        out.append(states[backpointers[ff, t]])
    out.append(states[backpointers[f, big_t]])
    return out

def argmax(sequence):
    # Note: You could use np.argmax(sequence), but only if sequence is a list.
    # If it is a generator, first convert it: np.argmax(list(sequence))

    # Since we loop from 1 to big_n, the result of argmax is between
    # 0 and big_n - 1. However, 0 is the initial state, the actual
    # states start from 1, so we add 1.
    return 1 + max(enumerate(sequence), key=lambda x: x[1])[0]


if __name__ == '__main__':
    main()
