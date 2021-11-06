# from datetime import datetime, timedelta

# def date_range(start, end):
#     delta = end - start  # as timedelta
#     days = [start + timedelta(days=i) for i in range(delta.days + 1)]
#     return days
# #2021-10-24 00:00:00.000
# #2021-10-24 00:00:00.000
# start_date = datetime(2008, 8, 1)
# end_date = datetime(2008, 8, 1)
    
# print(date_range(start_date, end_date)) 

from datetime import date, timedelta
import datetime

# sdate = date(2019,3,21)   # start date
# edate = date(2019,3,25)   # end date

sdate = datetime.datetime.strptime('2021-10-21', "%Y-%m-%d")   # start date
edate = datetime.datetime.strptime('2021-10-25', "%Y-%m-%d")   # end date

def dates_bwn_twodates(start_date, end_date):
    for n in range(int ((end_date - start_date).days +1)):
        yield start_date + timedelta(n)
print([str(d).split(" ")[0] for d in dates_bwn_twodates(sdate,edate)])



# from datetime import datetime
# print(datetime.strptime('2021-10-24', '%Y-%m-%d'))