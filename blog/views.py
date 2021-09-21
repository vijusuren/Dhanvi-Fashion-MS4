from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def all_blog_posts(request):
    """
    A view to return all the blog posts
    """
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog_posts.html', context)
