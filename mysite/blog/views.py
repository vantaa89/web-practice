from django.shortcuts import render

from django.views import generic
from .models import Post
# Create your views here.


class MainPage(generic.ListView):
    queryset = Post.objects.filter(post_class=1)
    template_name = 'index.html'

class AboutPage(generic.ListView):
    queryset = Post.objects.filter(post_class=2)
    template_name = 'about.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).filter(post_class=0).order_by('-created_on')
    template_name = 'blog.html'