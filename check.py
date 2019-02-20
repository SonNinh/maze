import time
import sys

def create(src):
    i = 0
    lines = src.split("\n")

    maze = list()

    for line in lines:
        ls = []
        if len(line) is not 0:
            for c in line:
                ls.append(c)
            maze.append(ls)

    return maze

def find_player(maze, ID):
    for x in range(1, len(maze)-1):
        for y in range(1, len(maze[x])-1):
            if maze[x][y] is ID:
                return x, y

    return 0, 0

def find_map(maze, player):
    data = list()
    step = list()
    step.append(player)
    # print("step:", step)
    data.append(step)
    # print("data:", data)
    while len(step) > 0:
        step = []
        for i in data[len(data)-1]:

            x = i[0] + 1
            y = i[1]
            if maze[x][y] is " ":
                step.append((x, y))
                maze[x][y] = "."
            elif (maze[x][y] is "o") or (maze[x][y] is "!"):
                return (x, y), data

            x = i[0] - 1
            y = i[1]
            if maze[x][y] is " ":
                step.append((x, y))
                maze[x][y] = "."
            elif (maze[x][y] is "o") or (maze[x][y] is "!"):
                return (x, y), data

            x = i[0]
            y = i[1] + 1
            if maze[x][y] is " ":
                step.append((x, y))
                maze[x][y] = "."
            elif (maze[x][y] is "o") or (maze[x][y] is "!"):
                return (x, y), data

            x = i[0]
            y = i[1] - 1
            if maze[x][y] is " ":
                step.append((x, y))
                maze[x][y] = "."
            elif (maze[x][y] is "o") or (maze[x][y] is "!"):
                return (x, y), data

        data.append(step)

    return [0, 0], data

def find_path(target, map):
    path = list()
    path.append(target)
    current = target

    for step in reversed(map):
        for node in step:
            if node[0] == current[0] and abs(node[1] - current[1]) == 1:
                path.append(node)
                current = node
            elif node[1] == current[1] and abs(node[0] - current[0]) == 1:
                path.append(node)
                current = node

    return path

def find_dir(path):
    dir = list()
    path_rev = path[::-1]
    current = path_rev[0]

    for node in path_rev[1:]:
        if node[0] > current[0]:
            dir.append("DOWN")
        elif node[0] < current[0]:
            dir.append("UP")
        elif node[1] > current[1]:
            dir.append("RIGHT")
        elif node[1] < current[1]:
            dir.append("LEFT")

        current = node

    return dir


def path_finding():

    ID = "A"
    maze_txt = ""
    f = open(sys.argv[1]+".txt", "r")
    if f.mode == 'r':
        maze_txt = f.read()

    maze = create(maze_txt)


    player = find_player(maze, ID)


    target, map = find_map(maze, player)


    path = find_path(target, map)


    dir = find_dir(path)

    for node in path:
        maze[node[0]][node[1]] = '\x1b[4;30;43m' + ' ' + '\x1b[0m'

    for i in maze:
        for j in i:
            if j is not '\x1b[4;30;43m' + ' ' + '\x1b[0m':
                j = '\x1b[0;37;40m' + j + '\x1b[0m'
            print(j, end='')
        print()
    # print(maze_txt)
    # print("Coordination:", player)
    # print("target", target)
    # print("data:", map)
    # print("path:", path)
    # print(dir)

start = time.time()
path_finding()
print(time.time() - start)
