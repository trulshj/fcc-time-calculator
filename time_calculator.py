def add_time(start, duration, start_weekday=None):

    start_time, period = start.split(" ")
    start_hour, start_minute = [int(t) for t in start_time.split(":")]
    dur_hour, dur_minute = [int(d) for d in duration.split(":")]

    # Calculate the total hours and minutes
    end_hour = start_hour + dur_hour
    end_minute = start_minute + dur_minute

    # Calculate how many days forward we've gone
    days = (end_hour + (end_minute // 60)) // 24

    # Calculate the new time to show on the clock
    new_hour = end_hour % 12 + end_minute // 60
    new_minute = (str(end_minute % 60)).rjust(2, '0')

    # Figure out what period the new time is in
    end_period = period
    if (end_hour // 12) % 2 == 1 or new_hour == 12:
        if period == "AM":
            end_period = "PM"
        elif period == "PM":
            end_period = "AM"
            # Add a day since we passed midnight
            days += 1


    weekdays = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday'
    ]

    # Figure out which day we land on after traveling forward in time
    if start_weekday:
        start_day_idx = weekdays.index(start_weekday.title())
        new_day_idx = (start_day_idx + days % 7) % 7
        new_weekday = weekdays[new_day_idx]

    # Structure the output
    new_time = f"{new_hour}:{new_minute} {end_period}"

    if start_weekday:
        new_time += f", {new_weekday}"

    if days == 1 and (period != end_period or end_period == "AM"):
        new_time += " (next day)"

    elif days > 1:
        new_time += f" ({days} days later)"

    return new_time
