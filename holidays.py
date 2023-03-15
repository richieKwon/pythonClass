from datetime import date, timedelta, datetime
import holidays

uk_holidays = holidays.country_holidays('GB', subdiv='England')
it_holidays = holidays.country_holidays('IT')

dateList = []
startDate = datetime(2023, 1, 1)
for i in range(0, 365):
    nextDay = startDate + timedelta(days=i)
    dateList.append(nextDay)

holidayList = []
for j in range(0, len(dateList)):
    if (dateList[j] in it_holidays):
        holidayList.append(dateList[j].strftime('%Y%m%d'))
print(holidayList)
