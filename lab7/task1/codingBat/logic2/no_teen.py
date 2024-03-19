def fix_teen(n):
    # Check if n is within the range 13..19 inclusive, excluding 15 and 16
    if 13 <= n <= 19 and n not in [15, 16]:
        return 0
    else:
        return n

def no_teen_sum(a, b, c):
    # Call fix_teen on each of the input values and sum them up
    return fix_teen(a) + fix_teen(b) + fix_teen(c)