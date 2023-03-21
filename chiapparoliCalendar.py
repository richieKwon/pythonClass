from datetime import date, timedelta, datetime
import holidays

FYstartDate = datetime(2023, 4, 1)
FYendDate = datetime(2024, 4, 1)
it_holidays = holidays.country_holidays('IT')


everyDaysList = [FYstartDate+timedelta(j)
                 for j in range(0, (FYendDate - FYstartDate).days)]

workingDaysList = [FYstartDate+timedelta(i) for i in range(0, (FYendDate - FYstartDate).days)
                   if (FYstartDate+timedelta(i)).weekday() < 5]

FYitalyHolidaysList = [everyDaysList[k] for k in range(0, len(everyDaysList))
                       if everyDaysList[k] in it_holidays]

FYshutdownPeriods = []

chiapparoliCalendarList = [date.strftime('%Y%m%d') for date in list(
    sorted(set(workingDaysList) - set(FYitalyHolidaysList)-set(FYshutdownPeriods))
)]

print(chiapparoliCalendarList)
