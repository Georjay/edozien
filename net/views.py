from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import create_postForm, create_eventForm
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import (
    Post, 
    PostCategory, 
    Event, 
    EventCategory, 
    Message,
    Video
    )



class PostListView(ListView):
    model = Post
    template_name = 'net/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post
    template_name = 'net/blog-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['recent_posts'] = Post.objects.order_by('-date_posted')[:5]
        context ['all_categories'] = PostCategory.objects.all()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = create_postForm
    # fields = ['title', 'body', 'image', 'category']
    #uses the post_form.html

    def form_valid(self, form):
        #This assigns the current logged in user as the author before saving the post to avoid an integrity error
        form.instance.author = self.request.user 
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = create_postForm
    # fields = ['title', 'body', 'image', 'category']
    #uses the post_form.html

    def form_valid(self, form):
        #This assigns the current logged in user as the author before saving the post to avoid an integrity error
        form.instance.author = self.request.user 
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'
    #uses the post_confirm_delete.html


class EventListView(ListView):
    model = Event
    template_name = 'net/event.html'
    context_object_name = 'events'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['event_categories'] = EventCategory.objects.all()
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'net/event-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['recent_events'] = Event.objects.order_by('-date_posted')[:5]
        context ['event_categories'] = EventCategory.objects.all()
        return context

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = create_eventForm
    #uses the event_form.html

    def form_valid(self, form):
        #This assigns the current logged in user as the author before saving the post to avoid an integrity error
        form.instance.author = self.request.user 
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = create_eventForm
    #uses the event_form.html

    def form_valid(self, form):
        #This assigns the current logged in user as the author before saving the post to avoid an integrity error
        form.instance.author = self.request.user 
        return super().form_valid(form)

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = '/events/'
    #uses the event_confirm_delete.html

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'net/inbox.html'
    context_object_name = 'inbox'
    ordering = ['is_read']
    paginate_by = 20

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'net/inbox-detail.html'

class BioListView(ListView):
    model = Video
    template_name = 'net/bio.html'
    context_object_name = 'videos'
