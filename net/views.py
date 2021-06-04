from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView
)
from .models import Post, Category

def home(request):
    template = 'net/home.html'
    return render(request, template)

class PostListView(ListView):
    model = Post
    template_name = 'net/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'net/blog-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['recent_posts'] = Post.objects.order_by('-date_posted')[:5]
        context ['all_categories'] = Category.objects.all()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body', 'image', 'category']

    def form_valid(self, form):
        #This assigns the current logged in user as the author before saving the post to avoid an integrity error
        form.instance.author = self.request.user 
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'body', 'image', 'category']

    def form_valid(self, form):
        #This assigns the current logged in user as the author before saving the post to avoid an integrity error
        form.instance.author = self.request.user 
        return super().form_valid(form)