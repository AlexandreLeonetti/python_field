import collections
# write a program that search through a matrix maze
   #basic algo :
"""
   past path is colored grey
   fences are black
   last element is marked "End"
   else search(L), search(right), Search(up), search(down)
    on a x y axis it translates as :
    jsearch(x-1), search (x+1), search(y-1), search(x+1)
"""

_maze = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
]

print("maze")

"""
#type white, black, start, visited, end.
class node:
    def __init__(self, color=None):
        self.type=color
"""
coords = collections.namedtuple("coords",("x","y"))
start = coords(0,0)
end   = coords(9,9)


def maz(maze,s,e):
    path = []

    #helper function performs recursion
    def helper(cur):# helper function takes one node
        # each node is defined by coords
        #eliminate wrong cases : black, and out bound (both column and lines)
        if not (((0<=cur.x<len(maze)) and (0<=cur.y<len(maze[cur.x]))) and maze[cur.x][cur.y]==0):
            return False

        #advance and mark path as black (1)
        path.append(cur)
        maze[cur.x][cur.y] = 1
        if cur == e:
            return True

        if any(map(helper, (coords(cur.x-1,cur.y),
                            coords(cur.x+1,cur.y),
                            coords(cur.x,cur.y-1),
                            coords(cur.x,cur.y+1)))):
            return True
        #print(path)
        del path[-1]
        return False




    if not helper(s): #call of helper inside if
        return []# no path found 

    return path



print(maz(_maze,start,end))






