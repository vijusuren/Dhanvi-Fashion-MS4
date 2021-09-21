from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_posts, name='blogs'),
    path('add/', views.add_blog, name='add_blog'),
    path('detail/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
