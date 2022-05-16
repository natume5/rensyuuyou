import datetime
import dateutil.relativedelta


today = datetime.date.today()
# 本日
print(today)
# 50日前
print(today + dateutil.relativedelta.relativedelta(days = -50))
# 2か月後
print(today + dateutil.relativedelta.relativedelta(months = -2))
# 3か月と10日後
print(today + dateutil.relativedelta.relativedelta(days = 10, months= 3))

