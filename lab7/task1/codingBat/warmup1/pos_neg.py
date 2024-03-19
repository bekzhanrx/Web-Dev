def pos_neg(a, b, negative):
  if negative and a < 0 and b < 0:
    return True
  elif (a < 0 and b > 0 and not negative) or (a > 0 and b < 0 and not negative):
    return True
  else:
    return False