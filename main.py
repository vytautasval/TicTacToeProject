import random

def main():
    map = [["#","#","#"], ["#","#","#"], ["#","#","#"]]


    while not (p_win_conditions(map) or b_win_conditions(map) or no_spots_left(map)):

        x_bot = random.randint(0, 2)
        y_bot = random.randint(0, 2)
        x = int(input("x: "))
        y = int(input("y: "))

        player_movement(x, y, map)
        bot_movement(x_bot, y_bot, map)
        print_map(map)

    else:
        if p_win_conditions(map) == True:
            print("Player won.")
            quit()
        elif b_win_conditions(map) == True:
            print("Bot won.")
            quit()
        else:
            print("No one won.")
            quit()

def print_map(map):
    for _ in map:
        for i in _:
            print(i, end=" ")
        print()

def player_movement(x, y, map):
    if any("#" in sublist for sublist in map):
        while map[y][x] != "#":
            x = int(input("x: "))
            y = int(input("y: "))
        else:
            map[y][x] = "o"

    return map[y][x]

def bot_movement(x_bot, y_bot, map):
    if any("#" in sublist for sublist in map):
        while map[y_bot][x_bot] != "#":
            x_bot = random.randint(0, 2)
            y_bot = random.randint(0, 2)
        else:
            map[y_bot][x_bot] = "x"

    return map[y_bot][x_bot]

def p_win_conditions(map):
    player_win = [(map[0][0] == "o" and map[0][1] == "o" and map[0][2] == "o"),
    (map[1][0] == "o" and map[1][1] == "o" and map[1][2] == "o"),
    (map[2][0] == "o" and map[2][1] == "o" and map[2][2] == "o"),
    (map[0][0] == "o" and map[1][0] == "o" and map[2][0] == "o"),
    (map[0][1] == "o" and map[1][1] == "o" and map[2][1] == "o"),
    (map[0][2] == "o" and map[1][2] == "o" and map[2][2] == "o"),
    (map[0][0] == "o" and map[1][1] == "o" and map[2][2] == "o"),
    (map[0][2] == "o" and map[1][1] == "o" and map[2][0] == "o")
    ]
    for p in player_win:
        if p == True:
            return True
    return False

def b_win_conditions(map):
    bot_win = [(map[0][0] == "x" and map[0][1] == "x" and map[0][2] == "x"),
    (map[1][0] == "x" and map[1][1] == "x" and map[1][2] == "x"),
    (map[2][0] == "x" and map[2][1] == "x" and map[2][2] == "x"),
    (map[0][0] == "x" and map[1][0] == "x" and map[2][0] == "x"),
    (map[0][1] == "x" and map[1][1] == "x" and map[2][1] == "x"),
    (map[0][2] == "x" and map[1][2] == "x" and map[2][2] == "x"),
    (map[0][0] == "x" and map[1][1] == "x" and map[2][2] == "x"),
    (map[0][2] == "x" and map[1][1] == "x" and map[2][0] == "x")
    ]
    for b in bot_win:
        if b == True:
            return True
    return False

def no_spots_left(map):
    for _ in map:
        for i in _:
            if i == "#":
                return False
    return True

main()