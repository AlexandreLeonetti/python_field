def calculate_probability(num_throws, num_sides, target_number):
    # Probability of not getting the target number in one throw
    probability_not_target = 1 - (1 / num_sides)

    # Probability of not getting the target number in all throws
    probability_not_target_in_all_throws = probability_not_target ** num_throws

    # Probability of getting the target number at least once
    probability_at_least_one_target = 1 - probability_not_target_in_all_throws

    return probability_at_least_one_target

# Number of throws
num_throws = 12

# Number of sides on the die (6 for a six-sided die)
num_sides =10 

# Target number (10 for a six-sided die)
target_number = 9

# Calculate the probability of getting at least one 6 in 10 throws
probability = calculate_probability(num_throws, num_sides, target_number)

print(f"The probability of getting at least one 6 in {num_throws} throws is: {probability:.4f}")

