## Control (Epsilon-Greedy)

import random 
from collections import defaultdict
from blackjack_env import *

# epsilon-greedy action selection
def epsilon_greedy(Q, state, epsilon=0.1):
    if random.random() < epsilon:
        return random.choice([0, 1])  #explore
    return 0 if Q[state][0] > Q[state][1] else 1  #exploit

# generate one full episode
def generate_episode(Q, epsilon):
    player = draw_hand()
    dealer = draw_hand()
    
    episode = []
    
    while True:
        state = (sum_hand(player), dealer[0], usable_ace(player))
        
        action = epsilon_greedy(Q, state, epsilon)
        
        episode.append((state, action))
        
        player, dealer, reward, done = step(player, dealer, action)
        
        if done:
            return episode, reward
        
# Monte Carlo control
def monte_carlo_control(episodes=100000, epsilon=0.1):
    Q = defaultdict(lambda: [0, 0])
    returns = defaultdict(list)
    
    for _ in range(episodes):
        episode, reward = generate_episode(Q, epsilon)
        
        visited = set()
        
        for state, action in episode:
            if (state, action) not in visited:
                visited.add((state, action))
                
                returns[(state, action)].append(reward)
                
                #Average return
                Q[state][action] = sum(returns[(state, action)])/ len(returns[(state, action)])

    return Q