import datetime
import re

# def get_last_name(full_name):
#     last_name = full_name.split(' ')[0]
#     return last_name
#
# print(get_last_name('Иванов Иван Иванович'))

# time_in = datetime.datetime.now()
# time_out = time_in + datetime.timedelta(days=3)
# seconds = int((time_out - time_in).total_seconds() / 60)
#
#
# print(time_in)
# print(time_out)
# print(seconds)

from django.http import HttpResponse


def multiply(request):
    number = request.GET.get('number')
    multiplier = request.GET('multiplier')

    try:
        result = int(number) * int(multiplier)
        html = f"<html><body>{number}*{multiplier}={result}</body></html>"
    except (ValueError, TypeError):
        html = f"<html><body>Invalid input.</body></html>"

    return HttpResponse(html)