# finds the lowest, highest and average
def get_stats(stats_list):

    # sort the lists
    stats_list.sort()

    # find the lowest, highest and average scores...
    lowest_score = stats_list[0]
    highest_score = stats_list[-1]
    average_score = sum(stats_list) / len(stats_list)

    return [lowest_score, highest_score, average_score]

# create lists to hold user and computer scores
user_scores = [10, 0, 13, 7, 10, 11]
comp_scores = [10, 11, 0, 0, 10, 11]

# Loop six times - for testing purposes, ask the user to enter the
# score for the user and the computer for each round
# for item in range(0, 6):
#   user_points = int(input("Enter the user score: "))
#   comp_points = int(input("Enter the computer score: "))

    # add user and computer scores to our lists!
#   user_scores.append(user_score)
#   comp_scores.append(comp_score)

# calculate  the lowest,highest and average
# score and display them.

user_stats = get_stats(user_scores)
comp_stats = get_stats(comp_scores)


print("📊📊📊 Game Statistics 📊📊📊 ")
print(f"User - Lowest score: {user_stats[0]}\t"
      f"Highest score: {user_stats[1]}\t"
      f"Averagew score: {user_stats[2]}\t")

print(f"Computer - Lowest score: {comp_stats[0]}\t"
      f"Highest score: {comp_stats[1]}\t"
      f"Averagew score: {comp_stats[2]}\t")

print("low: ", user_stats[0])
print("high ", user_stats[1])
print("average ", user_stats[2])

