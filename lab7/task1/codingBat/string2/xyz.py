def xyz_there(str):
  for i in range(len(str)-2):
    if str[i] == 'x' and str[i+1] == 'y' and str[i+2] == 'z' and str[i-1] != '.':
      return True
  return False