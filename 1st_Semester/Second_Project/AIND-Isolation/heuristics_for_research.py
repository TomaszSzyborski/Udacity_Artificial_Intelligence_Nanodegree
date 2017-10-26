def winner_or_loser(game, player):
    """
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
    float or None
        Floar or None depending if winner/looser is identified
    """
    return float("-inf") if game.is_loser(player) else float("inf") if game.is_winner(player) else None

def get_own_and_opponent_moves(game, player):
    return (game.get_legal_moves(player), game.get_legal_moves(game.get_opponent(player)))

def aggressive_heuristic(game, player):
    won_or_lost = winner_or_loser(game, player)

    if won_or_lost is not None:
        return won_or_lost
    else:
        own_moves, opponent_moves = list(map(len, get_own_and_opponent_moves(game, player)))

    return own_moves - 1.5 * opponent_moves


def defensive_heuristic(game, player):
    won_or_lost = winner_or_loser(game, player)

    if won_or_lost is not None:
        return won_or_lost
    else:
        own_moves, opponent_moves = list(map(len, get_own_and_opponent_moves(game, player)))

    return 1.5 * own_moves - opponent_moves


def maximizing_win_chances_heuristic(game, player):
    won_or_lost = winner_or_loser(game, player)

    if won_or_lost is not None:
        return won_or_lost
    else:
        own_moves, opponent_moves = list(map(len, get_own_and_opponent_moves(game, player)))

    if own_moves == 0:
        to_return = float("-inf")
    elif opponent_moves == 0:
        to_return = float("inf")
    else:
        to_return = float(own_moves)/opponent_moves

    return to_return


def minimizing_losing_chances_heuristic(game, player):
    won_or_lost = winner_or_loser(game, player)

    if won_or_lost is not None:
        return won_or_lost
    else:
        own_moves, opponent_moves = list(map(len,get_own_and_opponent_moves(game, player)))

    if own_moves == 0:
        to_return = float("-inf")
    elif opponent_moves == 0:
        to_return = float("inf")
    else:
        to_return = -float(opponent_moves)/own_moves

    return to_return 


def chances_heuristic(game, player):
    won_or_lost = winner_or_loser(game, player)

    if won_or_lost is not None:
        return won_or_lost
    else:
        own_moves, opponent_moves = list(map(len, get_own_and_opponent_moves(game, player)))

    return own_moves * own_moves - opponent_moves * opponent_moves


def weighted_chances_heuristic(game, player):
    won_or_lost = winner_or_loser(game, player)

    if won_or_lost is not None:
        return won_or_lost
    else:
        own_moves, opponent_moves = list(map(len, get_own_and_opponent_moves(game, player)))

    return own_moves * own_moves - 1.5 * opponent_moves * opponent_moves


def weighted_chances_heuristic_v2(game, player):
    won_or_lost = winner_or_loser(game, player)

    if won_or_lost is not None:
        return won_or_lost
    else:
        own_moves, opponent_moves = list(map(len, get_own_and_opponent_moves(game, player)))
        
    return 1.5 * own_moves * own_moves - opponent_moves * opponent_moves