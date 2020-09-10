"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # pass  # TODO
        self.vertices[vertex_id] = set()
        

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # pass  # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # pass  # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        search_tracker = {}

        for v in self.vertices:
            search_tracker[v] = 0

        q = Queue()

        search_tracker[starting_vertex] = 1
        q.enqueue(starting_vertex)

        while q.isEmpty() is not True:
            u = q.getOne(0)
            
            for v in self.get_neighbors(u):
                if search_tracker[v] == 0:
                    search_tracker[v] = 1
                    q.enqueue(v)
            
            print(u)
            q.dequeue()
            search_tracker[u] = 2

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO

        search_tracker = {}
        parent_tracker = {}

        def DFS_visit(vert):
            search_tracker[vert] = 1
            print(vert)

            for n in self.get_neighbors(vert):
                if search_tracker[n] == 0:
                    parent_tracker[n] = vert
                    DFS_visit(n)

            search_tracker[vert] = 2

        for v in self.vertices:
            search_tracker[v] = 0
            parent_tracker[v] = None

        for v in self.vertices:
            if search_tracker[v] == 0:
                DFS_visit(v)



    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # pass  # TODO

        search_tracker = {}
        parent_tracker = {}

        def DFS_visit(vert):
            search_tracker[vert] = 1
            print(vert)

            for n in self.get_neighbors(vert):
                if search_tracker[n] == 0:
                    parent_tracker[n] = vert
                    DFS_visit(n)

            search_tracker[vert] = 2

        for v in self.vertices:
            search_tracker[v] = 0
            parent_tracker[v] = None

        for v in self.vertices:
            if search_tracker[v] == 0:
                DFS_visit(v)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass  # TODO

        search_tracker = {}
        path = []
        parents = {}

        for v in self.vertices:
            search_tracker[v] = 0

        q = Queue()

        search_tracker[starting_vertex] = 1
        q.enqueue(starting_vertex)

        while q.isEmpty() is not True:
            u = q.getOne(0)
            if u == destination_vertex:
                parent = u
                while parent != -1:
                    path.insert(0, parent)
                    check = parents.get(parent)
                    if check:
                        parent = parents[parent]
                    else:
                        parent = -1
                return path
            
            for v in self.get_neighbors(u):
                if search_tracker[v] == 0:
                    search_tracker[v] = 1
                    parents[v] = u
                    q.enqueue(v)
            
            q.dequeue()
            search_tracker[u] = 2



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  # TODO

        search_tracker = {}
        parent_tracker = {}
        path = []

        def DFS_visit(vert):
            search_tracker[vert] = 1
            print(vert)

            for n in self.get_neighbors(vert):
                if search_tracker[n] == 0:
                    parent_tracker[n] = vert
                    DFS_visit(n)

            search_tracker[vert] = 2

        for v in self.vertices:
            search_tracker[v] = 0
            parent_tracker[v] = None

        for v in self.vertices:
            if v == destination_vertex:
                parent = v
                while parent != -1:
                    path.insert(0, parent)
                    check = parent_tracker.get(parent)
                    if check:
                        parent = parent_tracker[parent]
                    else:
                        parent = -1
                return path
            if search_tracker[v] == 0:
                DFS_visit(v)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # pass  # TODO
        search_tracker = {}
        parent_tracker = {}
        path = []

        def DFS_visit(vert):
            search_tracker[vert] = 1
            print(vert)

            for n in self.get_neighbors(vert):
                if search_tracker[n] == 0:
                    parent_tracker[n] = vert
                    DFS_visit(n)

            search_tracker[vert] = 2

        for v in self.vertices:
            search_tracker[v] = 0
            parent_tracker[v] = None

        for v in self.vertices:
            if v == destination_vertex:
                parent = v
                while parent != -1:
                    path.insert(0, parent)
                    check = parent_tracker.get(parent)
                    if check:
                        parent = parent_tracker[parent]
                    else:
                        parent = -1
                return path
            if search_tracker[v] == 0:
                DFS_visit(v)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
