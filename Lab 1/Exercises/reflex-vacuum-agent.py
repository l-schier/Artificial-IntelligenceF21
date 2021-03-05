A = 'A'
B = 'B'

environment = {
    A: 'Dirty',
    B: 'Dirty',
    'Current': A
}

def REFLEX_VACUUM_AGENT(loc_st):
    if loc_st[1] == 'Dirty':
        return 'Suck'
    if loc_st[0] == A:
        return 'Right'
    if loc_st[0] == B:
        return 'Left'

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

def run(n, make_agent):
    print('Current                    New')
    print('location   status  action  location    status')
    for i in range(1,n):
        (location, status) = sensors()
        print('{:12s}{:8s}'.format(location, status), end='')
        action = make_agent(sensors())
        actuators(action)
        (location, status) = sensors()
        print('{:8s}{:12s}{:8s}'.format(action, location, status))

run(10, REFLEX_VACUUM_AGENT)