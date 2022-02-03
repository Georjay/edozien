from django.forms import ModelForm
from .models import Post, PostCategory, Event, EventCategory, Message
from django import forms

class create_postForm(ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset = PostCategory.objects.all(),
        widget = forms.CheckboxSelectMultiple, required=True
    )
    class Meta:
        model = Post
        fields = [ 
            'title',
            'sub_title',
            'body',
            'image',
            'category'
        ]

class create_eventForm(ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset = EventCategory.objects.all(),
        widget = forms.CheckboxSelectMultiple, required=True
    )
    class Meta:
        model = Event
        fields = [ 
            'title',
            'body',
            'image',
            'category'
        ]
