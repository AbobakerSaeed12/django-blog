from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'template.html')

def blogposts(request):
    return render(request, 'blogposts.html')