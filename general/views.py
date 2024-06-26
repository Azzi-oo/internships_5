from django.shortcuts import render
from general.models import Post


def base(request):
    return render(request, 'base.html')


def posts_list(request):
    posts = Post.objects.filter(is_published=True)
    return render(request, 'posts_list.html', {'posts': posts})
