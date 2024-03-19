def centered_average(nums):
    nums.remove(min(nums))
    nums.remove(max(nums))
    total = sum(nums)
    average = total // len(nums)
    
    return average