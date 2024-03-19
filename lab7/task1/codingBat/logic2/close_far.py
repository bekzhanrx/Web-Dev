def close_far(a, b, c):
    # Helper function to check if two numbers are "close"
    def is_close(x, y):
        return abs(x - y) <= 1

    # Helper function to check if a number is "far"
    def is_far(x, y, z):
        return abs(x - y) >= 2 and abs(x - z) >= 2

    # Check if either b or c is close to a, while the other is far from all
    return (is_close(a, b) and is_far(a, b, c)) or (is_close(a, c) and is_far(a, c, b))