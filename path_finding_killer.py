from string import ascii_uppercase
import sys


def create(src):
    i = 0
    lines = src.split("\n")

    maze = list()

    for line in lines:
        ls = []
        if len(line) is not 0:
            maze.append([c for c in line])

    return maze


def find_player(maze, ID):
    for x in range(1, len(maze)-1):
        for y in range(1, len(maze[x])-1):
            if maze[x][y] is ID:
                return x, y

    return 0, 0


# def __find_map(maze, node, dir, data):
#     x = node[0] + dir[0]
#     y = node[1] + dir[1]
#     if maze[x][y] is " ":
#         step.append((x, y))
#         maze[x][y] = "."
#     elif (maze[x][y] is "o") or (maze[x][y] is "!"):
#         return (x, y), data


def find_map(maze, player, ID):
    data = list()
    step = list()
    step.append(player)
    data.append(step)
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while len(step) > 0:
        step = []
        for i in data[len(data)-1]:
            for dir in directions:
                x = i[0] + dir[0]
                y = i[1] + dir[1]
                if maze[x][y] is " ":
                    step.append((x, y))
                    maze[x][y] = "."
                elif (maze[x][y] is "o") or (maze[x][y] is "!"):
                    return (x, y), data
                elif maze[x][y] in ascii_uppercase and maze[x][y] is not ID:
                    if len(data) % 2 == 0:
                        sys.stderr.write(str(maze[x][y])+"\n")
                        return (x, y), data
        if len(step) > 0:
            data.append(step)

    return (data[len(data)-1][0][0], data[len(data)-1][0][1]), data


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


def path_finding(maze, ID):
    player = find_player(maze, ID)

    target, map = find_map(maze, player, ID)
    # sys.stderr.write("target" + str(target[0])+ "," + str(target[1]) +"\n")
    path = find_path(target, map)

    dir = find_dir(path)

    return dir, target, maze
