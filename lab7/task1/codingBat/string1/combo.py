def combo_string(a, b):
  min = ""
  max = ""
  if(len(a) > len(b)):
    min = b
    max = a
  else:
    min = a
    max = b
  return min + max + min