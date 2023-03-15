from datetime import date, timedelta, datetime
import holidays

workingDays = []
startDate = datetime(2023, 1, 1)
for i in range(0, 365):
    nextDay = startDate + timedelta(days=i)
    if (nextDay.weekday() < 5):
        workingDays.append(nextDay.strftime('%Y%m%d'))

print(workingDays)
