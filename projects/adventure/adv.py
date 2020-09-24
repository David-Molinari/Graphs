'''
Until the Friday of the resubmit, I did not realize that the character to could
reenter a room without backtracking to it. This changes how I need to solve
the problem, but at this point I do not have time. Hopefully more time can
be given, and if needed, someone can meet with me in Support Hours.
'''

from room import Room
from player import Player
from world import World

from util import Stack, Queue

import random
from ast import literal_eval

class Graph:

    '''Represent a graph as a dictionary of vertices mapping labels to edges.'''
    def __init__(self):
        self.vertices = {}
        self.travel_tracker = {}

    def add_vertex(self, vertex_id):
        '''
        Add a vertex to the graph.
        '''
        # pass  # TODO
        self.vertices[vertex_id] = {}
        

    def add_edge(self, v1, v2):
        '''
        Add a directed edge to the graph.
        '''
        # pass  # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        '''
        Get all neighbors (edges) of a vertex.
        '''
        # pass  # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        '''
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        '''
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
        '''
        Print each vertex in depth-first order
        beginning from starting_vertex.
        '''
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


'''
I can let you know one high level way to approach this sprint is to do DFS - 
essentially moving to rooms while you can, 
and keeping track of where you went, and then once you hit a dead end, 
you backtrack until you hit a room with an unexplored room neighbor. 
You keep going while your visited is less than the # of rooms you need to explore.
'''

'''
Initiate a graph accompanied by a traversal function.
Do a dfs, keeping track of where I went.

'''

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
graph = Graph()
traversal_path = []
visited_rooms = {}
bt_stack = []

def traversal_function(current_room = player.current_room):
    global visited_rooms
    if len(visited_rooms) == 500:
        return
    if len(visited_rooms) > 0:
        if visited_rooms.get(current_room.id) == None:
            visited_rooms[current_room.id] = 1
    if graph.vertices.get(current_room.id) == None:
        current_exits = player.current_room.get_exits()
        for e in current_exits:
            if graph.vertices.get(current_room.id):
                graph.vertices[current_room.id] = {**graph.vertices[current_room.id], e: '?'}
            else:
                graph.vertices[current_room.id] = {e: '?'}
        player.travel(current_exits[0])
        graph.vertices[current_room.id][current_exits[0]] = player.current_room.id
        traversal_path.append(current_exits[0])
        bt_stack.insert(0, current_room.id)
        traversal_function(player.current_room)
    else:
        counter = 0
        for e in graph.vertices[current_room.id]:
            counter += 1
            if graph.vertices[current_room.id][e] == '?':
                player.travel(e)
                graph.vertices[current_room.id][e] = player.current_room.id
                traversal_path.append(e)
                bt_stack.insert(0, current_room.id)
                traversal_function(player.current_room)
                break
            elif len(graph.vertices[current_room.id]) == counter:
                for a in graph.vertices[current_room.id]:
                    if graph.vertices[current_room.id][a] == bt_stack[0]:
                        del bt_stack[0]
                        player.travel(a)
                        traversal_path.append(a)
                        traversal_function(player.current_room)
                        break


traversal_function()

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
    print(len(traversal_path))
    tracker = {}
    for i in range(0, 500):
        tracker[i] = i
    for i in visited_rooms:
        del tracker[i.id]
    print('Unvisited rooms below:')
    for i in tracker:
        print(i)



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
