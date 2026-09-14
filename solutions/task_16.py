from collections import deque
def month_calendar(start_weekday, days):
    n = 0
    day = deque(range(1,days+1))
    for _ in range(start_weekday):
        day.appendleft(" ")
        n+=1
    calendare_list = list(day)
    weeks = []
    for i in range(0, len(calendare_list),7):
        week_chunk = calendare_list[i:i+7]
        formatted_days = [f"{d:>2}" for d in week_chunk]
        week_string = " ".join(formatted_days).rstrip()
        weeks.append(week_string)
    return "\n".join(weeks)