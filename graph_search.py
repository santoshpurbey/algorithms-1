from Queue import Queue

def breadth_first_search(graph, start_node_id):
    start_node = graph.get_node(start_node_id)
    start_node.visited = True

    q = Queue()
    q.put(start_node)

    while not q.empty():
        node = q.get()
        for neighbour in node.neighbours:
            if not neighbour.visited:
                neighbour.visited = True
                q.put(neighbour)

class Node:
    def __init__(self, id):
        self.id = id
        self.visited = False
        self.neighbours = [] 

class Graph:
    def __init__(self, l):
        self.nodes = {}

        def add_node_if_required(id):
            if not self.nodes.has_key(id):
                self.nodes[id] = Node(id)
            return self.nodes[id]

        for e in l:
            node1 = add_node_if_required(e[0])
            node2 = add_node_if_required(e[1])
            node1.neighbours.append(node2)
            node2.neighbours.append(node1)

    def get_node(self, id):
        return self.nodes[id]

    def get_outgoing(self, from_id):
        return self.nodes[from_id].neighbours