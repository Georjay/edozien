from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    UserPostListView,
    PostUpdateView,
    PostDeleteView,
    EventListView,
    UserEventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    MessageListView,
    MessageDetailView,
    BioListView,
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', PostListView.as_view(), name='blog-posts'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('events/', EventListView.as_view(), name='events'),
    path('events/<str:username>/', UserEventListView.as_view(), name='user-events'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/create/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('inbox/', MessageListView.as_view(), name='inbox'),
    path('inbox/<int:pk>/', MessageDetailView.as_view(), name='inbox-detail'),
    path('about/', BioListView.as_view(), name='about-me'),
]