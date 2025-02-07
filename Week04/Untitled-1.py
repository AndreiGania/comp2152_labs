"""
ANDREI GANIA
Assignment: #1
"""

# Function to find the key with the minimum value
def key_of_min(d):
    return min(d, key=d.get)

# Function to find the key with the maximum value
def key_of_max(d):
    return max(d, key=d.get)

def main():
    # Define variables
    gym_member = "Alex Alliton"  # String
    preferred_weight_kg = 20.5  # Float
    highest_reps = 25  # Int
    membership_active = True  # Boolean

    # Dictionary containing workout stats
    workout_stats = {
        "Alex": (30, 45, 20),
        "Jamie": (20, 30, 30),
        "Taylor": (20, 60, 45)
    }

    # Calculate total minutes for each friend
    totals = {friend + "_Total": sum(workoutMins) for friend, workoutMins in workout_stats.items()}

    # Print total minutes for each friend
    for friend, total in totals.items():
        print(f"{friend}: {total} minutes")

    # 2D list representation of workout stats
    workout_list = [list(workout_stats[friend]) for friend in workout_stats]

    print("\nWorkout List:", workout_list)

    # Extracting minutes for yoga and running for all friends
    yoga_running = [activity[:2] for activity in workout_list]
    print("\nMinutes for yoga and running for all friends:", yoga_running)

    # Extracting minutes for weightlifting for the last two friends
    weightlifting_last_two = [activity[2] for activity in workout_list[-2:]]
    print("Minutes for weightlifting for the last two friends:", weightlifting_last_two)

    # Get user input for a friend's name
    friend_name = input("\nEnter a friend's name: ").capitalize()

    # Check if the friend's name exists in the dictionary
    if friend_name in workout_stats:
        # Retrieve and print the friend's workout details
        yoga, running, weightlifting = workout_stats[friend_name]
        total_minutes = sum(workout_stats[friend_name])
        
        print(f"\n{friend_name}'s workout minutes:")
        print(f"  Yoga: {yoga} minutes")
        print(f"  Running: {running} minutes")
        print(f"  Weightlifting: {weightlifting} minutes")
        print(f"  Total: {total_minutes} minutes")
    else:
        print(f"\nFriend {friend_name} not found in the records.")

    # Wait for user input before displaying highest and lowest total workout minutes
    input("\nPress Enter to View Highest and Lowest Total Workout Minutes...")

    # Calculate total workout minutes for each friend
    total_minutes_dict = {friend: sum(minutes) for friend, minutes in workout_stats.items()}

    # Find the friend with the highest and lowest total workout minutes
    friend_max = key_of_max(total_minutes_dict)
    friend_min = key_of_min(total_minutes_dict)

    # Print the results
    print("\nWorkout Summary:")
    print(f"🏆 Friend with the highest total workout minutes: {friend_max} ({total_minutes_dict[friend_max]} minutes)")
    print(f"🔻 Friend with the lowest total workout minutes: {friend_min} ({total_minutes_dict[friend_min]} minutes)")

if __name__ == "__main__":
    main()
