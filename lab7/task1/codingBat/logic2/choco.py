def make_chocolate(small, big, goal):
    # Calculate the maximum number of kilos we can cover with the big bars
    max_big_kilos = big * 5
    
    # Calculate the remaining goal after using big bars
    remaining_goal = goal - min(goal // 5, big) * 5
    
    # Calculate the number of small bars needed
    small_needed = remaining_goal
    
    # Check if there are enough small bars
    if small_needed <= small:
        return small_needed
    else:
        return -1