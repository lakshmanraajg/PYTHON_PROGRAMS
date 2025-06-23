import calendar
from datetime import date

# c = calendar.TextCalendar(calendar.MONDAY)
# str1 = c.formatmonth(2025,6,0,0)
# print(str1)
# 
# print("MONTH: ")
# for name in calendar.month_name:
#     print(name, end = " ")
#     
# print("\nDAYS: ")
# for day in calendar.day_name:
#     print(day, end = " ")
#     
#     
# #Team meeting on first friday of every month
# print("\nTeam meeting will be on: ")
# for m in range(1,13):
#     cal = calendar.monthcalendar(2025,m)
#     weekone = cal[0]
#     weektwo = cal[1]
#     if weekone[calendar.FRIDAY] != 0:
#         meetday = weekone[calendar.FRIDAY]
#     else:
#         meetday = weektwo[calendar.FRIDAY]
#     print(calendar.month_name[m], meetday)
    
    
def bank_working_saturdays(year):
    for month in range(1, 13):
        month_name = calendar.month_name[month]
        saturdays = []
        # Go through each day of the month
        for week in calendar.monthcalendar(year, month):
            if week[calendar.SATURDAY] != 0:
                saturdays.append(week[calendar.SATURDAY])
        
        # 1st, 3rd, and 5th Saturdays (if available)
        working_saturdays = []
        if len(saturdays) >= 1:
            working_saturdays.append(saturdays[0])  # 1st Saturday
        if len(saturdays) >= 3:
            working_saturdays.append(saturdays[2])  # 3rd Saturday
        if len(saturdays) >= 5:
            working_saturdays.append(saturdays[4])  # 5th Saturday

        for day in working_saturdays:
            print(f"{month_name} {day}")
bank_working_saturdays(2025)
