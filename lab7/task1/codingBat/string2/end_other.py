def end_other(a, b):
  s = a.lower()
  t = b.lower()
  if s.endswith(t) or t.endswith(s):
    return True
  return False
