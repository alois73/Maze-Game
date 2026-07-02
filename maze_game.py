import random

size = 5

def create_maze():
    maze = [["_" for _ in range(size)] for _ in range(size)]

    maze[0][0] = "S"
    maze[size-1][size-1] = "E"

    r, c = 0, 0
    path = {(0, 0)}

    while (r, c) != (size-1, size-1):
        if random.choice([True, False]):
            if c < size - 1:
                c += 1
        else:
            if r < size - 1:
                r += 1
        path.add((r, c))

    for i in range(size):
        for j in range(size):
            if (i, j) not in path and (i, j) != (0, 0) and (i, j) != (size-1, size-1):
                if random.random() < 0.3:
                    maze[i][j] = "#"

    return maze


maze = create_maze()
player_pos = [0, 0]


def show_maze():
    for i in range(size):
        for j in range(size):
            if [i, j] == player_pos:
                print("P", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()
    print()


def move(direction):
    r, c = player_pos

    if direction == "up":
        r -= 1
    elif direction == "down":
        r += 1
    elif direction == "left":
        c -= 1
    elif direction == "right":
        c += 1
    else:
        print("Invalid move")
        return

    if r < 0 or r >= size or c < 0 or c >= size:
        print("Outside grid!")
        return

    if maze[r][c] == "#":
        print("Wall!")
        return

    player_pos[0], player_pos[1] = r, c


while True:
    show_maze()
    m = input("Move or quit: ").lower()

    if m == "quit":
        print("You quit")
        break

    move(m)

    if maze[player_pos[0]][player_pos[1]] == "E":
        show_maze()
        print("You win!")
        break