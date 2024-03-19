def lucky_sum(a, b, c):
  sum = 0
  for i in a, b , c:
    if i == 13:
      return sum
    sum += i
  return sum