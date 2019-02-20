#!/usr/bin/env python3

import sys
import path_finding
import time


def get_massage(expect):
    receive = input()
    ID = "unknow"
    while expect not in receive:
        receive = input()

    if expect is "YOU":
        ID = receive[len(receive)-1]

    receive = input()
    return True, ID

def get_maze():
    maze = ""
    receive = input()
    while "MAZE" not in receive:
        receive = input()


    while True:
        receive = input()
        if len(receive) == 0:
            break

        maze += receive
        maze += "\n"

    return maze

def record_maze(src):
    f= open("guru99.txt","w+")
    f.write(src)
    f.close()

def move_mouse(dir):
    print("MOVE " + dir + "\n")

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

def main():
    ID = "unknow"
    res = get_massage("HELLO")
    if res[0] is True:
        print("I AM NSON97\n")

    res = get_massage("YOU")
    if res[0] is True:
        ID = res[1]
        print("OK\n")


    direction = list()
    maze_txt = get_maze()
    maze = create(maze_txt)
    start = time.time()
    direction, target, maze = path_finding.path_finding(maze, ID)
    end = time.time()


    i = 0
    while True:

        sys.stderr.write(str(end-start)+"\n")
        # sys.stderr.write(str(len(direction))+"\n"+str(i)+"\n")
        move_mouse(direction[i])
        i += 1

        maze_txt = get_maze()
        maze = create(maze_txt)

        # sys.stderr.write(maze[target[0]][target[1]]+"\n")
        if maze[target[0]][target[1]] not in ["o", "!"] :
            direction = []
            start = time.time()
            direction, target, _ = path_finding.path_finding(maze, ID)
            i = 0



    # move_mouse("RIGHT")
    # move_mouse("DOWN")
    # move_mouse("LEFT")




if __name__ == "__main__":
    main()
