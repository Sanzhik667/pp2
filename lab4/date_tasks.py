#1
from datetime import date
"""today=date.today()
past_time=today.replace(day = today.day-5)
print("В числовом виде:")
print(past_time)
past_time_name=past_time.strftime("%A")
print("Название дня недели:")
print(past_time_name)"""
#2
"""today_number=date.today()
yesterday_number=today_number.replace(day=today_number.day-1)
tomorrow_number=today_number.replace(day=today_number.day+1)
today=today_number.strftime("%A")
yesterday=yesterday_number.strftime("%A")
tomorrow=tomorrow_number.strftime("%A")
print("Today is "+today)
print("Yesterday is "+yesterday)
print("Tomorrow is "+tomorrow)"""
#3
"""import datetime
dt = datetime.datetime.today().replace(microsecond=0)
print()
print(dt)
print()
"""
#4
"""from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
date1 = datetime.strptime('2024-02-17 01:00:00', '%Y-%m-%d %H:%M:%S')
#Current date
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()
"""

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)