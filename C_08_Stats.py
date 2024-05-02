# create lists to hold user and computer scores
user_scores = []
comp_scores = []

# Loop six times - for testing purposes, ask the user to enter the
# score for the user and the computer for each round
for item in range(0, 6):
    user_points = int(input("Enter the user score: "))
    comp_points = int(input("Enter the computer score: "))

    # add user score to our list of user scores!
    user_scores.append(user_score)
    comp_scores.append(comp_score)

# calculate  the lowest,highest and average
# score and display them.

# sort the lists
user_scores.sort()
comp_scores.sort()

# find the lowest, highest and average scores...
user_low = user_scores[0]
user_high = user_scores[-1]
user_average = sum(user_scores) / len(user_scores)

print("low: ", user_low)
print("high ", user_high)
print("average ", user_average)

