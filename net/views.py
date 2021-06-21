from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import create_postForm, create_eventForm
from django.contrib import messages
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
    Video,
    )


def home(request):
    posts = Post.objects.order_by('-date_posted')[:6]
    events = Event.objects.order_by('-date_posted')[:6]

    # New way of sendind data from the front-end into the database
    if request.method == "POST":
        data = request.POST
        
        form = Message.objects.create(
            name = data['name'],
            email = data['email'],
            subject = data['subject'],
            body = data['message']
        )
        messages.success(request, 'Message sent to Chiké')

    context = {
        'posts': posts,
        'events': events,
    }
    template = 'net/home.html'

    return render(request,  template, context)


class PostListView(ListView):
    model = Post
    template_name = 'net/blog-post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context ['recent_posts'] = Post.objects.order_by('-date_posted')[:5]
        context ['all_categories'] = PostCategory.objects.all()
        return context


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
    # succes
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
    ordering = ['-id']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inbox_messages = Message.objects.all()
        context ['all_messages'] = inbox_messages.count()
        context ['unread_messages'] = inbox_messages.filter(is_read="False").count()
        context ['read_messages'] = inbox_messages.filter(is_read="True").count()
        return context


class MessageDetailView(LoginRequiredMixin, DetailView):
    # This method is written to make the .is_read field change from False to True.
    # Don't forget, this is still a class-based view
    def get(self, request, pk):
        message = Message.objects.get(id=pk)
        message.is_read=True
        message.save()
        template = 'net/inbox-detail.html'
        return render(request, template, locals())


class BioListView(ListView):
    model = Video
    template_name = 'net/bio.html'
    context_object_name = 'videos'
