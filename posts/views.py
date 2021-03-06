from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = "blog_posts"
    ordering = ['-post_date']
    paginate_by = 3

class PostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    fields = ['post_title', 'post_text']

    def form_valid(self,form):
        form.instance.post_author = self.request.user
        return super().form_valid(form)
