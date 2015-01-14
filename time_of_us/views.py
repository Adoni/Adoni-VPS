from django.shortcuts import render_to_response
from adoni.settings import TIME_ZONE
import os
import time

def time_of_us(request):
    os.environ["TZ"] = TIME_ZONE
    time.tzset()
    return render_to_response(
        'welcome.html',
        {
            'day':100,
            'hour':10,
            'minute':30,
            'second':10
        }
    )