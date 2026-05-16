import numpy as np 
import matplotlib.pyplot as plt

def plot_policy(policy):
    grid = np.zeros((10, 10))
    
    for player in range(12, 22):
        for dealer in range (1, 11):
            state = (player, dealer, False)
            grid[player - 12, dealer - 1] = policy.get(state, 0)
            
    plt.imshow(grid)
    plt.title("Policy 0=Stick, 1=Hit")
    plt.xlabel("Dealer showing")
    plt.ylabel("Player sum")
    plt.colorbar()
    plt.show()
