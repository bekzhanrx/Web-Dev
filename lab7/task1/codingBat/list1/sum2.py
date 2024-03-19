def sum2(nums):
  s = 0
  for i in range(len(nums)):
    if i < 2:
      s += nums[i]
  return s