def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.
    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # TODO: finish this function!
    return weighted_chances_heuristic(game, player)


def aggressive_heuristic(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = len(game.get_legal_moves(player))
    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return my_moves - 1.5 * opponent_moves


def defensive_heuristic(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = len(game.get_legal_moves(player))
    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return 1.5 * my_moves - opponent_moves


def maximizing_win_chances_heuristic(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = 1.0 * len(game.get_legal_moves(player))
    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    if my_moves == 0:
        return float("-inf")

    if opponent_moves == 0:
        return float("inf")

    return my_moves/opponent_moves


def minimizing_losing_chances_heuristic(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = len(game.get_legal_moves(player))
    opponent_moves = 1.0 * len(game.get_legal_moves(game.get_opponent(player)))

    if my_moves == 0:
        return float("-inf")

    if opponent_moves == 0:
        return float("inf")

    return -opponent_moves/my_moves


def chances_heuristic(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = len(game.get_legal_moves(player))
    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return my_moves*my_moves - opponent_moves*opponent_moves


def weighted_chances_heuristic(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = len(game.get_legal_moves(player))
    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return my_moves*my_moves - 1.5*opponent_moves*opponent_moves


def weighted_chances_heuristic_2(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = len(game.get_legal_moves(player))
    opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return 1.5*my_moves*my_moves - opponent_moves*opponent_moves