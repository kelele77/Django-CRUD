from dataclasses import field
from msilib.schema import ListView
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views import generic

from I4G000792CZO.blog.models import Post

class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.ListView):
    model = Post
    field = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(generic.ListView):
    model = Post

class PostUpdateView(generic.ListView):
    model = Post
    field = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(generic.ListView):
    model = Post
    field = "__all__"
    success_url = reverse_lazy("blog:all")