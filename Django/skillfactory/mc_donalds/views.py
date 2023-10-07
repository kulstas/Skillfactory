from django.shortcuts import render

# Create your views here.
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