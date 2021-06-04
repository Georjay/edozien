from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(default='postdefault.jpg', upload_to='post_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Never delete a user. Make inactive instead.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #This method takes me to the details page of a post when created
        return reverse('post-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
