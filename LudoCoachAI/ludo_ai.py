def get_best_move(board_state):
    board_state = board_state.lower()
    if "kill" in board_state:
        return "Kill opponent's token"
    elif "safe" in board_state:
        return "Move token from safe zone"
    elif "home" in board_state:
        return "Bring new token out"
    else:
        return "Move furthest token"
