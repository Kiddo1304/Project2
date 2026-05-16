from montecarlo_es import monte_carlo_es
from montecarlo_control import monte_carlo_control
from blackjack_env import *
from plots import plot_policy


def q_to_policy(Q):
    policy = {}
    for state in Q:
        policy[state] = 0 if Q[state][0] > Q[state][1] else 1
    return policy

def main():
    episodes = 1000000  
    
    print ("Training Monte Carlo Exploring Starts...")
    policy_es, Q_es = monte_carlo_es(episodes)
    
    print("Training Monte Carlo Control (epsilon-greedy)...")
    Q_mc = monte_carlo_control(episodes)
    
    # plot ES policy 
    plot_policy(policy_es)
    
    # evaluate ES
    wins, draws, losses = evaluate_policy(policy_es)
    print(f"Wins: {wins}, Draws: {draws}, Losses: {losses}")
    
    total = wins + draws + losses
    win_rate = wins / total * 100
    print(f"Win Rate: {win_rate:.2f}%")
    
    # convert and evaluate MC control
    policy_mc = q_to_policy(Q_mc)
    
    wins_mc, draws_mc, losses_mc = evaluate_policy(policy_mc)
    print("\nMC Control Results:")
    print(f"Wins: {wins_mc}, Draws: {draws_mc}, Losses: {losses_mc}")
    
    total_mc = wins_mc + draws_mc + losses_mc
    win_rate_mc = wins_mc / total_mc * 100
    print(f"Win Rate: {win_rate_mc:.2f}%")
    
    print("Done")
    
def evaluate_policy(policy, episodes=10000):
    wins = 0
    draws = 0
    losses = 0

    for _ in range(episodes):
        player = draw_hand()
        dealer = draw_hand()

        while True:
            state = (sum_hand(player), dealer[0], usable_ace(player))
            action = policy.get(state, 1)  # default = hit

            player, dealer, reward, done = step(player, dealer, action)

            if done:
                if reward == 1:
                    wins += 1
                elif reward == 0:
                    draws += 1
                else:
                    losses += 1
                break

    return wins, draws, losses
    

if __name__ == "__main__":
    main()
                
                