from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class HomePage(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = "blog_posts"

class PostView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'