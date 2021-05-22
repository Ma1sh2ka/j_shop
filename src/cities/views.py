from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

CODES = {
    "AAL": "Aalborg, Denmark",
    "ANX": "Andenes, Norway",
    "ARN": "Stockholm, Sweden",
    "AEY": "Akyreyri, Iceland"
}

def cities(request, code):
    citycountry = CODES.get(code, 'Not Found')
    ctx = {
        'code': code,
        'citycountry': citycountry,
    }
    return render(request, template_name='cities.html', context=ctx)

def home(request):
    return render(request, template_name='homepage.html', context={})