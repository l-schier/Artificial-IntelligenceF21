A = 'A'
B = 'B'
state = {}
action = None
model = {A: None, B:None}

RULE_ACTION = {
    1: 'Suck',
    2: 'Right',
    3: 'Left',
    4: 'NoOp'
}
RULES = {
    (A, 'Dirty'): 1,
    (B, 'Dirty'): 1,
    (A, 'Clean'): 2,
    (B, 'Clean'): 3,
    (A, B, 'Clean'): 4
}

environment = {
    A: 'Dirty',
    B: 'Dirty',
    'Current': A
}

def interpret_input(input):
    return input

def rule_match(state, rules):
    return rules.get(tuple(state))

def update_state(state, action, percept):
    (location, status) = percept
    state = percept
    if model[A] == model[B] == 'Clean':
        state = (A, B, 'Clean')
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

run(10)
    