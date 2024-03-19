def count_hi(str):
  c = 0
  for i in range(len(str)-1):
    if(str[i] == 'h' and str[i+1] == 'i'):
      c += 1
  return c