
#### Environment 

import random

def draw_card():
    card = random.randint(1, 13)
    return min(card, 10)

def draw_hand():
    return [draw_card(), draw_card()]

def usable_ace(hand):
    return 1 in hand and sum(hand) + 10 <= 21

def sum_hand(hand):
    if usable_ace(hand):
        return sum(hand) + 10
    return sum(hand)

def is_bust(hand):
    return sum_hand(hand) > 21

def score(hand):
    return 0 if is_bust(hand) else sum_hand(hand)

def dealer_policy(hand):
    while sum_hand(hand) < 17:
        hand.append(draw_card())
    return hand

def step(player_hand, dealer_hand, action):
    if action == 1:  #hit
        player_hand.append(draw_card())
        if is_bust(player_hand):
            return player_hand, dealer_hand, -1, True
        return player_hand, dealer_hand, 0, False
    else:  #stick
        dealer_hand = dealer_policy(dealer_hand)
        
        player_score = score(player_hand)
        dealer_score = score(dealer_hand)
        
        if dealer_score > 21 or player_score > dealer_score:
            return player_hand, dealer_hand, 1, True
        elif player_score < dealer_score:
            return player_hand, dealer_hand, -1, True
        else:
            return player_hand, dealer_hand, 0, True
    