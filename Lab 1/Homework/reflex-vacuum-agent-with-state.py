from random import randint
A = 'A'
B = 'B'
C = 'C'
D = 'D'
state = {}
action = None
model = {A: None, B:None, C:None, D:None}

RULE_ACTION = {
    1: 'Suck',
    2: 'Right',
    3: 'Left',
    4: 'Down',
    5: 'Up',
    6: 'NoOp'
}
RULES = {
    (A, 'Dirty'): 1,
    (B, 'Dirty'): 1,
    (C, 'Dirty'): 1,
    (D, 'Dirty'): 1,
    (A, 'Clean'): 2,
    (B, 'Clean'): 4,
    (C, 'Clean'): 3,
    (D, 'Clean'): 5,
    (A, B, C, D, 'Clean'): 6
}

environment = {
    A: 'Dirty',
    B: 'Dirty',
    C: 'Dirty',
    D: 'Dirty',
    'Current': [A,B,C,D][randint(0,3)]
}

def interpret_input(input):
    return input

def rule_match(state, rules):
    return rules.get(tuple(state))

def update_state(state, action, percept):
    (location, status) = percept
    state = percept
    if model[A] == model[B] ==  model[C] == model[D] == 'Clean':
        state = (A, B, C, D, 'Clean')
    model[location] = status
    return state

def REFLEX_VACUUM_AGENT_WITH_STATE(percept):
    global state, action
    state = update_state(state, action, percept)
    rule = rule_match(state, RULES)
    action = RULE_ACTION[rule]
    return action

def sensors():
    location = environment['Current']
    return (location, environment[location])

def actuators(action):
    location = environment['Current']
    if action == 'Suck':
        environment[location] = 'Clean'
    elif action == 'Right' and location == A:
        environment['Current'] = B
    elif action == 'Left' and location == B:
        environment['Current'] = A
    elif action == 'Right' and location == D:
        environment['Current'] = C
    elif action == 'Left' and location == C:
        environment['Current'] = D
    elif action == 'Up' and location == C:
        environment['Current'] = B
    elif action == 'Down' and location == B:
        environment['Current'] = C
    elif action == 'Up' and location == D:
        environment['Current'] = A
    elif action == 'Down' and location == A:
        environment['Current'] = D

def run(n):
    print('Current                    New')
    print('location   status  action  location    status')
    for i in range(1,n):
        (location, status) = sensors()
        print('{:12s}{:8s}'.format(location, status), end='')
        action = REFLEX_VACUUM_AGENT_WITH_STATE(sensors())
        actuators(action)
        (location, status) = sensors()
        print('{:8s}{:12s}{:8s}'.format(action, location, status))

run(20)
    