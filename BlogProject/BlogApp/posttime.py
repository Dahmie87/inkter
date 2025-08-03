# import time
# from .views import time_made


# class post_time:
#     sec = time.strftime("%S", time_made)
#     min = time.strftime("%M", time_made)
#     hour = time.strftime("%H", time_made)
#     day = time.strftime("%D", time_made)


# class curremt_time:
#     sec = time.strftime("%S", time.localtime())
#     min = time.strftime("%M", time.localtime())
#     hour = time.strftime("%H", time.localtime())
#     day = time.strftime("%D", time.localtime())


# print(curremt_time().hour)

# post_year = post_time().day[6:8]
# current_year = curremt_time().day[6:8]
# post_mon = post_time().day[0:2]
# current_mon = curremt_time().day[0:2]
# post_day = post_time().day[3:5]
# current_day = curremt_time().day[3:5]

# print(post_time().day)


# def when():
#     if post_time().day == curremt_time().day:
#         if post_time().hour != curremt_time().hour:
#             val = int(curremt_time().hour)-int(post_time().hour)
#             diff = "hour"
#         elif post_time().min != curremt_time().min:
#             val = int(curremt_time().min) - int(post_time().min)
#             diff = "min"
#         else:
#             val = int(curremt_time().sec) - int(post_time().sec)
#             diff = "sec"
#     elif post_year != current_year:
#         val = int(current_year)-int(post_year)
#         diff = 'year'
#     elif post_mon != current_mon:
#         val = int(current_mon)-int(post_mon)
#         diff = "month"
#     else:
#         val = int(current_day)-int(post_day)
#         diff = "day"
#     if val > 2:
#         diff += "s"
#     return str(val)+" "+diff+" "+"ago"


# print(when())
from datetime import datetime
current_time = datetime.now()
print(type(current_time))
