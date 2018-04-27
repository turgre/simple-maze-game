maze = [["_", "_", "_", "#"],
        ["_", "#", "_", "_"],
        ["_", "#", "#", "_"]]

start_row = 2
start_col = 0

end_row = 2
end_col = 3


def get_maze_space_contents(row, col):
    if row == end_row and col == end_col:
        return "E"
    elif row == start_row and col == start_col:
        return "S"
    else:
        return maze[row][col]


def pretty_print_maze(player_row, player_col):
    for row_index in range(len(maze)):
        pretty_row = ""
        for col_index in range(len(maze[row_index])):
            if row_index == player_row and col_index == player_col:
                pretty_row += "P "
            else:
                pretty_row += get_maze_space_contents(row_index, col_index) + " "
        print(pretty_row)


def is_valid_move(player_row, player_col, direction):
    next_row = player_row
    next_col = player_col

    if direction == "up":
        next_row -= 1
    elif direction == "down":
        next_row += 1
    elif direction == "left":
        next_col -= 1
    elif direction == "right":
        next_col += 1

    # Make sure player will be on the board.
    if next_row < 0 or next_row >= len(maze):
        return False
    if next_col < 0 or next_col >= len(maze[next_row]):
        return False

    # Make sure player will not be on a wall.
    next_space_content = get_maze_space_contents(next_row, next_col)
    if next_space_content == "#":
        return False
    else:
        return True
