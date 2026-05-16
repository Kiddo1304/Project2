##### Exploring Starts

import random
from collections import defaultdict
from blackjack_env import *

# generate one full episode
def generate_episode(policy):
    player = draw_hand()
    dealer = draw_hand()
    
    episode = []
    
    while True:
        state = (sum_hand(player), dealer[0], usable_ace(player))
        
        # random action if state not seen
        if state not in policy:
            action = random.choice([0, 1])  # 0 = stick, 1 = hit
        else:
            action = policy[state]
            
        episode.append((state, action))
        
        player, dealer, reward, done = step(player, dealer, action)
        
        if done:
            return episode, reward
        
# Monte Carlo Exploring Stars
def monte_carlo_es(episodes = 100000):
    Q = defaultdict(lambda: [0, 0])  #Q[state] = [stick_value, hit_value]
    returns = defaultdict(list)
    policy = {}
    
    for _ in range(episodes):
        episode, reward = generate_episode(policy)
        
        visited = set()
        
        for state, action in episode:
            if (state, action) not in visited:
                visited.add((state, action))
                
                returns[(state, action)].append(reward)
                
                #Average return
                Q[state][action] = sum(returns[(state, action)]) / len(returns[(state, action)])
                
                #improve policy
                if Q[state][0] > Q[state][1]:
                    policy[state] = 0  #stick
                else:
                    policy[state] = 1  #hit
    
    return policy, Q