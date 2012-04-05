import copy
from Queue import Queue
INF = 500

def solve(maze):
    lista_de_lista = map(list, maze)

    queue = Queue()
    queue.put( (find_begin(maze) , 0 ) )
    
    while not queue.empty():
        atual, distancia = queue.get()
        r,c= atual

        if r < 0 or r >= len(maze) or c < 0 or c >= len(maze[0]):
            continue

        if maze[r][c] == '#':
            continue

        if maze[r][c] == 'x': 
            return distancia

        lista_de_lista[r][c] = '#'

        queue.put(((r,c-1),distancia+1)) 
        queue.put(((r,c+1),distancia+1)) 
        queue.put(((r-1,c),distancia+1)) 
        queue.put(((r+1,c),distancia+1)) 

    return INF    

def find_char(maze, char):
    for i, line in enumerate(maze):
        if char in line:
            return (i, line.index(char))
    
def find_begin(maze):
    return find_char(maze, '.')
           
    
