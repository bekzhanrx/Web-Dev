def front3(str):
  f = 3
  if len(str) < 3:
    f = len(str)
  fr = str[:f]
  return fr + fr + fr