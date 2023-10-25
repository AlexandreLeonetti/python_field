#simulate how many dices it takes  to reach a certain score.
# how many throw does it takes to be sure to land a 6 on  six faced dice.
import random

def simulate_dice_rolls(num_rolls):
    # Initialize a counter for the number of times a 6 is rolled
    six_count = 0

    for _ in range(num_rolls):
        # Simulate a dice roll (random number between 1 and 6)
        roll = random.randint(1, 6)
        
        # Check if the roll is a 6
        if roll == 6:
            six_count += 1

    # Calculate the probability of rolling a 6
    probability = six_count / num_rolls

    return probability

# Number of dice rolls to simulate
num_rolls = 100000

# Simulate the dice rolls and calculate the probability
probability_of_six = simulate_dice_rolls(num_rolls)

print(f"Simulated probability of rolling a 6 in {num_rolls} rolls: {probability_of_six:.4f}")


