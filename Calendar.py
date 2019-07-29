import calendar

c = calendar.TextCalendar(calendar.THURSDAY)
str = c.formatmonth(2019, 1)
print(str)

hc = calendar.HTMLCalendar(calendar.THURSDAY)
str = hc.formatmonth(2019, 1)
print(str)

# for i in c.itermonthday(2020, 1):
#     print(i)

for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

for month in range (1,13):
    mycal = calendar.monthcalendar(2019, month)
    week1 = mycal[0]
    week2 = mycal[1]
    if week1[calendar.MONDAY] !=0:
        auditday = week1[calendar.MONDAY]
    else:
        auditday = week2[calendar.MONDAY]
    print("%10s %2d" % (calendar.month_name[month], auditday))
