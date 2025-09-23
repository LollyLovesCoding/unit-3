team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

# Elif executes code if the if block above it is False and doesn't execute. If instead the if statement is executed, the elif statement will be overlooked and not executed. The elif block can be repeatedly used an infinite amount of times.
# Else is executing code if both the if and elif statements above it doesn't get executed. For example, in line 17, the console will print a tie if the team_a_points isn't greater than team_b_points and the team_b_points isn't great than team_a_points.

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
if team_b_points > team_a_points:
    # Changing this elif statement to an if statement executes this if statement no matter what happens above it, but the else statement below executes if this if statement is False.
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
elif team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")
    # This is printed as the output because although team_a_wins is initialized as one less than team_b_wins, since the code was executed for team_a winning, the number of points for team_a_wins is increased by 1.
