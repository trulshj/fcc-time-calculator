def add_time(start, duration, start_day=None):

  start_time, period = start.split(" ")
  start_hour, start_minute = [int(t) for t in start_time.split(":")]
  dur_hour, dur_minute = [int(d) for d in duration.split(":")]

  end_hour = start_hour + dur_hour
  end_minute = start_minute + dur_minute
  
  days = (end_hour + (end_minute // 60)) // 24 + 1

  new_hour = end_hour % 12 + end_minute // 60
  new_minute = (str(end_minute % 60)).rjust(2, '0')

  # Figure out what period the new time is in
  if (end_hour // 12) % 2 == 1 or new_hour == 12:
    if period == "AM":
      period = "PM"
    elif period == "PM":
      period = "AM"

  new_time = f"{new_hour}:{new_minute} {period}"

  if days > 1:
    new_time += f" ({days} days later)"

  return new_time