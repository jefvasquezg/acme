from constant import weekdays, defaults
from models import day

list_days = [day.Day(weekdays.Monday, defaults.workweek_morning, defaults.workweek_noon, defaults.workweek_nights, []),
             day.Day(weekdays.Tuesday, defaults.workweek_morning, defaults.workweek_noon, defaults.workweek_nights, []),
             day.Day(weekdays.Wednesday, defaults.workweek_morning, defaults.workweek_noon, defaults.workweek_nights, []),
             day.Day(weekdays.Thursday, defaults.workweek_morning, defaults.workweek_noon, defaults.workweek_nights, []),
             day.Day(weekdays.Friday, defaults.workweek_morning, defaults.workweek_noon, defaults.workweek_nights, []),
             day.Day(weekdays.Saturday, defaults.work_weekend_morning, defaults.work_weekend_noon,
                     defaults.work_weekend_nights, []),
             day.Day(weekdays.Sunday, defaults.work_weekend_morning, defaults.work_weekend_noon,
                     defaults.work_weekend_nights, [])]
