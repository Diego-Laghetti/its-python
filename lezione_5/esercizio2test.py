def blackjack_hand_total(cards: list[int]) -> int:
    total = 0
    cont = 0
    
    for card in cards:
        if card == 11:
            cont += 1
        total += card
    
    while total > 21 and cont > 0:
        total -= 10 
        cont -= 1
    
    return total

print(blackjack_hand_total([2,3,5]))