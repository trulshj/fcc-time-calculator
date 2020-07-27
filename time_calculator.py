def add_time(start, duration, start_weekday=None):

  start_time, period = start.split(" ")
  start_hour, start_minute = [int(t) for t in start_time.split(":")]
  dur_hour, dur_minute = [int(d) for d in duration.split(":")]

  end_hour = start_hour + dur_hour
  end_minute = start_minute + dur_minute
  
  weekdays = ['Monday',
              'Tuesday', 
              'Wednesday',
              'Thursday',
              'Friday',
              'Saturday',
              'Sunday'
              ]
  
  days = (end_hour + (end_minute // 60)) // 24 + 1

  if start_weekday:
    start_day_idx = weekdays.index(start_weekday.title())
    new_day_idx = (start_day_idx + days % 7) % 7
    new_weekday = weekdays[new_day_idx]

  new_hour = end_hour % 12 + end_minute // 60
  new_minute = (str(end_minute % 60)).rjust(2, '0')

  # Figure out what period the new time is in
  if (end_hour // 12) % 2 == 1 or new_hour == 12:
    if period == "AM":
      period = "PM"
    elif period == "PM":
      period = "AM"

  new_time = f"{new_hour}:{new_minute} {period}"

  if start_weekday:
    if days == 2:
      new_time += "(next day)"
    else:
      new_time += f", {new_weekday}"

  if days > 1:
    new_time += f" ({days} days later)"

  return new_time