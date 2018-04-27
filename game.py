import maze

def move(player_row, player_col, direction):
    """Return and new row and column for the player based on 1) the direction
    the player wishes to move and 2) if that space is a valid space for the
    player to be in the maze.
    """

    # Do not change player loc if move is invalid
    if not maze.is_valid_move(player_row, player_col, direction):
        return [player_row, player_col]

    # Otherwise, return new player location
    if direction == "up":
        return [player_row - 1, player_col]
    elif direction == "down":
        return [player_row + 1, player_col]
    elif direction == "left":
        return [player_row, player_col - 1]
    elif direction == "right":
        return [player_row, player_col + 1]

def play_game():
    """Starts the maze game.
    """

    print("Welcome to the maze.")
    print("Move the P to the E space.")

    player_row = maze.start_row
    player_col = maze.start_col

    while player_row != maze.end_row or player_col != maze.end_col:
        maze.pretty_print_maze(player_row, player_col)

        direction = input("Enter your move:")
        new_player_loc = move(player_row, player_col, direction)
        player_row = new_player_loc[0]
        player_col = new_player_loc[1]
    print("You made it out of the maze!")

if __name__ == "__main__":
    play_game()
