class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0, distance=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.DISTANCE = distance

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        if self.PARENT_NODE != None:
            return 'Current state: ' + str(self.PARENT_NODE.STATE) + ' State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH) + ' - Distance: ' + str(self.DISTANCE)
        return ' State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH) + ' - Distance: ' + str(self.DISTANCE)

'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = GET_CHEAPEST(fringe)
        VISITED.append(node.STATE[0])
        if node.STATE[0] == GOAL_STATE[0] or node.STATE[0] == GOAL_STATE[1]:
            return node.path()
        
        children = EXPAND(node)
        
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        if s.STATE[0] not in VISITED:

            s.PARENT_NODE = node
            s.DEPTH = node.DEPTH + 1
            s.DISTANCE = node.DISTANCE + child[2]
            successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    queue.append(node)
    return queue



'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for li in list:
        queue.append(li)
    return queue



'''
Removes and returns the first element from fringe
'''
def REMOVE_FIRST(queue):
    return queue.pop(0)

'''
Removes and returns the cheapest element from fringe
'''
def GET_CHEAPEST(queue):
    lowest = None
    for entry in queue:
        if lowest == None:
            lowest = entry
        elif (entry.STATE[1] + entry.DISTANCE) < (lowest.STATE[1] + lowest.DISTANCE):
            lowest = entry
    queue.pop(queue.index(lowest))
    return lowest
'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state[0]]

# location, h
GOAL_STATE = [('A', 'Clean', 'Clean'), ('B', 'Clean', 'Clean')]
INITIAL_STATE = (('A', 'Dirty', 'Dirty'), 0, 1)
STATE_SPACE = {('A', 'Dirty', 'Dirty'): [(('A', 'Clean', 'Dirty'), 0, 1), (('B', 'Dirty', 'Dirty'), 0, 1)],
               ('A', 'Clean', 'Dirty'): [(('B', 'Clean', 'Dirty'), 0, 1)],
               ('A', 'Dirty', 'Clean'): [(('A', 'Dirty', 'Clean'), 0, 1), (('A', 'Clean', 'Clean'), 0, 1), (('B', 'Dirty', 'Clean'), 0, 1)],
               ('B', 'Dirty', 'Dirty'): [(('A', 'Dirty', 'Dirty'), 0, 1), (('B', 'Dirty', 'Dirty'), 0, 1), (('B', 'Dirty', 'Clean'), 0, 1)],
               ('B', 'Clean', 'Dirty'): [(('A', 'Clean', 'Dirty'), 0, 1), (('B', 'Clean', 'Clean'), 0, 1), (('B', 'Clean', 'Dirty'), 0, 1)],
               ('B', 'Dirty', 'Clean'): [(('A', 'Dirty', 'Clean'), 0, 1), (('B', 'Dirty', 'Clean'), 0, 1)],
               }

VISITED = []


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
