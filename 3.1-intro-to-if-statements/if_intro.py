robot_location = 130
ball_location = 135
goal_location = 120
have_ball = False

# The purpose of indenting in an if statement is to indicate to the computer that the code should only be run if the condition is true.
# We can tell if a code is enclosed in an if branch if it starts at a different indent line than other code (4 spaces indented).

# The operators += and -= is a simpler way of adding or subtracting a certain number to a variable.
# For example, robot_location += 5 adds 5 to the current robot_location variable, increasing it by 5.

if robot_location < ball_location:
    # Checks if the robot location is smaller than the ball location
    print("Almost at the ball")

if robot_location > goal_location:
    # Checks if the robot location is greater than the goal location
    print("You are beyond the goal.")

if robot_location == goal_location:
    # Checks if the robot is at the goal
    print("The robot is at the goal.")

robot_location += 5

if robot_location == goal_location:
    # Checks again if the robot is at the goal after moving it forward
    print("At the goal.")

if robot_location == ball_location:
    # Checks again if the robot is at the goal and makes it pick up the ball
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

if robot_location < goal_location:
    # Checks if the robot location is smaller than the goal location
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    # Checks if the robot is at the goal and has a ball
    print("You scored a goal!")
    have_ball = False
