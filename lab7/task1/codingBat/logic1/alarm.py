def alarm_clock(day, vacation):
  if 5 >= day >= 1:
    if vacation:
      return "10:00"
    else:
      return "7:00"
  else:
    if vacation:
      return "off"
    else:
      return "10:00"