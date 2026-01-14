def compare_hands(hand_a, hand_b):
    """
    hand_a, hand_b: (rank, tiebreakers)

    return:
        1  -> hand_a wins
       -1  -> hand_b wins
        0  -> empate
    """
    rank_a, tb_a = hand_a
    rank_b, tb_b = hand_b

    if rank_a > rank_b:
        return 1
    if rank_a < rank_b:
        return -1

    # ranks iguais → comparar tiebreakers
    if tb_a > tb_b:
        return 1
    if tb_a < tb_b:
        return -1

    return 0
