from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, ListView, DetailView
from blog.models import Post

# Create your views here.
class PostListView(ListView):
    models = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['__all__']
    success_url  = reverse_lazy('blog:all')

class PostDetailView(DetailView):
    models = Post

class PostUpdateView(UpdateView):
    models = Post
    fields = ['__all__']
    success_url  = reverse_lazy('blog:all')

class PostDeleteView(UpdateView):
    models = Post
    fields = ['__all__']
    success_url  = reverse_lazy('blog:all')