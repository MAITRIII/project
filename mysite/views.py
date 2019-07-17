from django.shortcuts import render
import requests
from .import  views
def home(request):
    response = requests.get('http://api.ipstack.com/27.106.116.38?access_key=c68579836b599228232711da17acf749')
    geodata = response.json()
    print("here",geodata)
    return render(request, 'mysite/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })