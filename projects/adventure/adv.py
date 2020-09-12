from room import Room
from player import Player
from world import World

from util import Stack, Queue

import random
from ast import literal_eval

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # pass  # TODO
        self.vertices[vertex_id] = {}
        

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

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
backtrack = {}

graph = Graph()

current_room = player.current_room.id
starting_room = player.current_room.id

counterrr = 0

def travel_function(current_room, direction = None, old_room = None):
    current_exits = player.current_room.get_exits()
    checker = graph.vertices.get(current_room)
    print('check', checker)
    print(current_room)
    if current_room == 0 and direction is not None:
        chek = 0
        for d in graph.vertices[current_room]:
            print(graph.vertices[current_room][d])
            if type(graph.vertices[current_room][d]) == str:
                chek = 1
        if chek == 0:
            return
    if checker is None:
        graph.add_vertex(current_room)
        if direction == 'n':
            backtrack[current_room] = 's'
        if direction == 's':
            backtrack[current_room] = 'n'
        if direction == 'e':
            backtrack[current_room] = 'w'
        if direction == 'w':
            backtrack[current_room] = 'e'
        for i in current_exits:
            graph.vertices[current_room][i] = '?'
    for d in graph.vertices[current_room]:
            print(d, graph.vertices[current_room][d])
    print(type(old_room))
    if old_room != None:
        if direction == 'n':
            graph.vertices[old_room]['n'] = player.current_room.id
            graph.vertices[player.current_room.id]['s'] = old_room
        if direction == 's':
            graph.vertices[old_room]['s'] = player.current_room.id
            graph.vertices[player.current_room.id]['n'] = old_room
        if direction == 'e':
            graph.vertices[old_room]['e'] = player.current_room.id
            graph.vertices[player.current_room.id]['w'] = old_room
        if direction == 'w':
            graph.vertices[old_room]['w'] = player.current_room.id
            graph.vertices[player.current_room.id]['e'] = old_room
    counter = 0
    for d in graph.vertices[current_room]:
            print(d, graph.vertices[current_room][d])
    found = 0
    for i in graph.vertices[current_room]:
        length = len(graph.vertices[current_room])
        print('here', length)
        counter = counter + 1
        print(counter)
        print(type(graph.vertices[current_room][i]))
        print(graph.vertices[current_room][i])
        if type(graph.vertices[current_room][i]) == str and found == 0:
            counter = 0
            found = 1
            player.travel(i)
            print(player.current_room.id)
            traversal_path.append(i)
            travel_function(player.current_room.id, i, current_room)
        elif counter == length and found == 0:
            counter = 0
            found = 1
            player.travel(backtrack[current_room])
            traversal_path.append(backtrack[current_room])
            travel_function(current_room = player.current_room.id, direction = backtrack[current_room])

travel_function(current_room)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
