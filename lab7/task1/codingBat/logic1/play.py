def squirrel_play(temp, is_summer):
  if is_summer and 100 >= temp >= 60:
    return True
  elif 90 >= temp >= 60:
    return True
  return False