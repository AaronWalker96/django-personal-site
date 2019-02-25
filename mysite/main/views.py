from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def homepage(request):
    return render(request=request, 
                  template_name="main/home.html",
                  context={"articles": Article.objects.all})

def about(request):
    return render(request=request, 
                  template_name="main/about.html")

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'main/article_detail.html', {'article':article})