from datetime import *
from dateutil.relativedelta import relativedelta


today = date.today()
# 本日
print(today)
# 50日前
print(today + relativedelta(days = -50))
# 2か月後
print(today + relativedelta(months = -2))
# 3か月と10日後
print(today + relativedelta(days = 10, months= 3))

