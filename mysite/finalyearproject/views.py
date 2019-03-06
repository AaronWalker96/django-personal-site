from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
# Create your views here.
def homepage(request):
    #return render(request, "finalyearproject/home.html")
    response = requests.get('https://api.github.com/users/aaronwalker96/repos')
    repoInfo = response.json
    return render(request, 'finalyearproject/home.html', {
        'repoInfo': repoInfo
    })
    #return HttpResponse("Howdy")