def make_bricks(small, big, goal):
    # Calculate the maximum number of inches we can cover with the big bricks
    max_big_inches = big * 5
    
    # If the goal is greater than the max inches covered by big bricks,
    # we can use the combination of big and small bricks to reach the goal
    if goal > max_big_inches:
        # Calculate the remaining inches after using big bricks
        remaining_inches = goal - max_big_inches
    else:
        # If goal is less than or equal to max inches covered by big bricks,
        # we only need to consider the remaining inches
        remaining_inches = goal % 5
    
    # Check if the remaining inches can be covered by small bricks
    return remaining_inches <= small