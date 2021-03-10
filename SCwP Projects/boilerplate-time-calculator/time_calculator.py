def add_time(start, duration, day=None):

    time, period = start.split()
    hour, minute = map(int, time.split(':'))
    add_hour, add_minute = map(int, duration.split(':'))

    if period == "AM":
        AM = True
    elif period == "PM":
        AM = False
    else:
        return "ERROR: Wrong Time Period"

    if minute > 60 or add_minute > 60:
        return "ERROR: Minute is greater than 60"

    new_min = minute + add_minute
    if new_min > 60:
        new_min -= 60
        hour += 1

    new_hour = hour + add_hour
    num_day = 0

    while new_hour >= 12:
        new_hour -= 12

        if AM:
            AM = not AM
        else:
            AM = not AM
            num_day += 1

        if new_hour == 0:
            new_hour = 12
            break

    if AM:
        new_period = "AM"
    else:
        new_period = "PM"

    new_time = f"{new_hour}:{str(new_min).rjust(2, '0')} {new_period}"

    if day:
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday']

        curr_day = days.index(day.title())
        index = curr_day + num_day
        while index > 6:
            index -= 7

        if num_day == 1:
            new_time = f"{new_time}, {days[index]} (next day)"
        elif num_day > 1:
            new_time = f"{new_time}, {days[index]} ({num_day} days later)"
        else:
            new_time = f"{new_time}, {days[index]}"
    else:
        if num_day == 1:
            new_time = f"{new_time} (next day)"
        elif num_day > 1:
            new_time = f"{new_time} ({num_day} days later)"

    return new_time
