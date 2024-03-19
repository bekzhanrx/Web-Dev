def front_times(str, n):
  f = 3
  if len(str) < 3:
    f = len(str)
  fs = str[:f]
  result = ""
  for i in range(n):
    result += fs
  return result