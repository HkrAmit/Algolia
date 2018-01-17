from django.shortcuts import render
from .models import blog

# Create your views here.
def home(request):
    all=blog.objects.all()
    return render(request, 'index.html', {'post':all})
def search(request):
    return render(request, 'search.html')