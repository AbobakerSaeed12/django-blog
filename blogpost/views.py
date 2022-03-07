from django.shortcuts import render, redirect
from .models import Blogpost
import json

# Create your views here.
def blogposts(request):
    blogposts = Blogpost.objects.all()
    context = { 
        'blogposts': blogposts,
    }    
    return render(request, 'blogpost/blogposts.html', context)

def new_post(request):
    if request.method == 'GET':
        context = {
            'page_title': 'Create a New Post'
        }
        return render(request, 'blogpost/new_post.html', context)
    else:
        new_post = Blogpost.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            text=request.POST.get('text'),
        )
        new_post.save()
        return redirect(blogposts)

def singe_post(request, post_id):
    selected_post = Blogpost.objects.get(id=post_id)
    context = {
        'page_title': getattr(selected_post, 'title'),
        'post': selected_post
    }
    return render(request, 'blogpost/single_post.html', context)