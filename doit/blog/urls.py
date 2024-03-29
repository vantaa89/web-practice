"""
URL configuration for do_it_django_prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),      # FBV: 숫자가 뒤에 오는 경우, views.py의 single_post_page(request, pk)를 호출
    # path('', views.index),                        # FBV: views.py에 정의된 index() 함수를 호출
    
]
