def solution(coin, cards):
    n = len(cards)
    target = n + 1

    hand = set(cards[:n // 3])
    candidate = set()

    idx = n // 3
    round_count = 1

    def remove_pair_from_hand():
        for card in list(hand):
            pair = target - card
            if pair in hand:
                hand.remove(card)
                hand.remove(pair)
                return True
        return False

    def remove_pair_hand_candidate():
        for card in list(hand):
            pair = target - card
            if pair in candidate:
                hand.remove(card)
                candidate.remove(pair)
                return True
        return False

    def remove_pair_from_candidate():
        for card in list(candidate):
            pair = target - card
            if pair in candidate:
                candidate.remove(card)
                candidate.remove(pair)
                return True
        return False

    while idx < n:
        candidate.add(cards[idx])
        candidate.add(cards[idx + 1])
        idx += 2

        if remove_pair_from_hand():
            round_count += 1

        elif coin >= 1 and remove_pair_hand_candidate():
            coin -= 1
            round_count += 1

        elif coin >= 2 and remove_pair_from_candidate():
            coin -= 2
            round_count += 1

        else:
            break

    return round_count