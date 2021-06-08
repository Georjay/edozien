from django.contrib import admin
from .models import PostCategory, Post, EventCategory, Event, Message

admin.site.register(PostCategory)
admin.site.register(Post)
admin.site.register(EventCategory)
admin.site.register(Event)
admin.site.register(Message)


