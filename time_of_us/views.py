from django.shortcuts import render_to_response
from adoni.settings import TIME_ZONE
import os
import time
import datetime


def time_of_us(request):
    os.environ["TZ"] = TIME_ZONE
    time.tzset()
    d1 = datetime.datetime.now()
    d2 = datetime.datetime(2013,5,30,0,0,0)
    delta_time = d1-d2
    day = delta_time.days
    hour = delta_time.seconds/3600
    minute = (delta_time.seconds % 3600)/60
    second = delta_time.seconds % 60
    return render_to_response(
        'welcome.html',
        {
            'day':day,
            'hour':hour,
            'minute':minute,
            'second':second
        }
    )