def string_match(a, b):
  c = 0
  for i in range(min(len(a), len(b)) - 1):
    if(a[i] == b[i] and a[i+1] == b[i+1]):
      c += 1
  return c
