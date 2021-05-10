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
GOAL_STATE = ['K', 'L']
INITIAL_STATE = ('A', 6, 0)
STATE_SPACE = {'A' : [('B', 5, 1), ('C', 5, 2), ('D', 2, 4)],
               'B' : [('A', 6, 1), ('E', 4, 4), ('F', 5, 5)],
               'C' : [('A', 6, 2), ('E', 4, 1)],
               'D' : [('A', 6, 4), ('H', 1, 1), ('I', 2, 4), ('J', 1, 2)],
               'E' : [('B', 5, 4), ('C', 5, 1), ('G', 4, 2), ('H', 1, 3)],
               'F' : [('B', 5, 5), ('G', 4, 1)],
               'G' : [('F', 5, 1), ('E', 4, 2), ('K', 0, 6)],
               'H' : [('D', 2, 1), ('E', 4, 3), ('K', 0, 6), ('L', 0, 5)],
               'I' : [('D', 2, 4), ('L', 0, 3)],
               'J' : [('D', 2, 2)],
               'K' : [('G', 4, 6), ('H', 1, 6)],
               'L': [('H', 1, 5), ('I', 2, 3)]
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
