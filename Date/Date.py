import time
def Date():
    e = time.time()
    f = time.localtime(e)
    hours = f.tm_hour
    day_number = f.tm_mday
    year = f.tm_year
    nummonth = f.tm_mon
    second = f.tm_sec
    minute = f.tm_min
    weekdays_temp = f.tm_wday
    weekdays = [
        "Sunday", "Monday", "Tuesday", "Wedensday", "Thursday", "Friday", "Saturday",
    ]
    weekday = weekdays[weekdays_temp]
    months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
    ]
    month = months[nummonth-1]
    if hours >=12:
        af = hours - 12
        hour = f"{af}"
    date = f"{month} {day_number} ({weekday}) {year}, {hour}:{minute}:{second}"
    return date