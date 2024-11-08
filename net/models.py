from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class PostCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Article Category"
        verbose_name_plural = "Article Categories"


class Post(models.Model):
    title = models.CharField(max_length=256)
    sub_title = models.CharField(max_length=256, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(default='postdefault.jpg', upload_to='post_pics', blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(PostCategory)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Never delete a user. Make inactive instead.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #This method takes me to the details page of a post when created
        return reverse('post-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class EventCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):

        return self.name

    class Meta:
        verbose_name = "Event Category"
        verbose_name_plural = "Event Categories"


class Event(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(default='eventdefault.jpg', upload_to='event_pics', blank=True, null=True) #blank and null adds a clear button to image field in django admin
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(EventCategory)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Never delete a user. Make inactive instead.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #This method takes me to the details page of a post when created
        return reverse('event-detail', kwargs={'pk': self.pk})

    def event_status(self):
        "Returns the status of an event."
        now = timezone.now()
        if self.date_posted > now:
            return "Upcoming"
        elif self.date_posted < now:
            return "Past"
        else:
            return "Ongoing"

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    subject = models.CharField(max_length=100)
    is_read = models.BooleanField(default=False)
    date_sent = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Inbox Message"
        verbose_name_plural = "Inbox Messages"

    def get_absolute_url(self):
        return reverse('home')
        

class MyVideo(models.Model):
    title = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"