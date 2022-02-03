from django.contrib import admin
from .models import PostCategory, Post, EventCategory, Event, Message, MyVideo
from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(MyVideo, MyModelAdmin)
admin.site.register(PostCategory)
admin.site.register(Post)
admin.site.register(EventCategory)
admin.site.register(Event)
admin.site.register(Message)