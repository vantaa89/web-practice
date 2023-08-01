from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# CBV
class PostList(ListView):
    model = Post
    # ListView는 설정하지 않을 시 기본으로 template_name을 모델명+"_list.html"로 설정
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post
    # DetailView는 설정하지 않을 시 기본으로 template_name을 모델명+"_detail.html"로 설정



# FBV

# def index(request):
#     # render함수를 이용해 templates 폴더의 blog/index.html을 표시해줌
#     posts = Post.objects.all().order_by('-pk')
#     return render(
#         request,
#         'blog/index.html', 
#         {
#             "posts": posts,
#         }
#     )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post
        }
    )