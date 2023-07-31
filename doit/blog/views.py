from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    # render함수를 이용해 templates 폴더의 blog/index.html을 표시해줌
    posts = Post.objects.all().order_by('-pk')
    return render(
        request,
        'blog/index.html', 
        {
            "posts": posts,
        }
    )