from datetime import datetime, timedelta
now_utc = datetime.now()

# print(now_utc)
# print(now_utc.day)
# print(now_utc.month)
# print(now_utc.year)
# print(now_utc.hour)
# print(now_utc.minute)
# print(now_utc.second)

# # 1/1/1970 -> now()
# print(now_utc.timestamp())
# unix_time
# timestamp 

# 0 - > 12
# print(now_utc.strftime("%I:%M:%S"))
# print(now_utc.strftime("%d/%m/%Y"))

date = "20-05-2026"

current = datetime.strptime(date, "%d-%m-%Y")

date = "01-05-2026"

current2 = datetime.strptime(date, "%d-%m-%Y")
# current2.day = current2.day + 2
# 0 1 2 3 4 5 6
print(current2.weekday() )

# import arrow