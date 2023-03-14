from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post, Category

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)

    return render(request, 'core/frontpage.html', {'posts': posts})

def about(request):
    return render(request, 'core/about.html')

def category_page(request):
    category1 = Category.objects.all()
    return render(request, 'core/category_page.html', {'category': category1})

def categorydetails(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/category.html', {'category': category, 'posts': posts})



def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")