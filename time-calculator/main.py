def add_time(start, duration, day=False):
    am_or_pm = {"AM":"PM", "PM":"AM"}
    days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


    start_hours_minutes, am_pm = start.split(" ")
    start_hours, start_minutes = start_hours_minutes.split(":")
    start_hours = int(start_hours)

    duration_hours, duration_minutes = duration.split(":")
    duration_hours = int(duration_hours)
    end_minutes = int(start_minutes) + int(duration_minutes)

    if end_minutes >= 60:
        end_minutes = end_minutes % 60
        start_hours += 1
    
    n = int((start_hours + duration_hours) / 24)
    number_of_flips = int((start_hours + duration_hours) / 12)
    end_hours = (start_hours + duration_hours) % 12
    if am_pm == "PM" and number_of_flips >= 1:
        n += 1
    if end_hours == 00:
        end_hours = 12
    if number_of_flips % 2 == 1:
        am_pm = am_or_pm[am_pm]

    new_time = f"{end_hours}:{end_minutes:02} {am_pm}"

    if day:
        new_day_index = (days_of_the_week.index(day.lower()) + n) % 7
        new_day = days_of_the_week[new_day_index]
        new_time += ", " + new_day.capitalize()

    if n == 1:
        return new_time + " " + "(next day)"
    elif n > 1:
        return new_time + " " + f"({n} days later)"
    return new_time

