from . import views
from django.urls import path

# 원래 없던 파일, 이 파일을 mysite/mysite/urls.py가 참조

urlpatterns = [
    path("", views.MainPage.as_view(), name="home"),
    path("about/", views.AboutPage.as_view(), name="about"),
    path("blog/", views.PostList.as_view(), name="blog"),
    path("blog/<slug:slug>/", views.PostDetail.as_view(), name='post_detail')
]