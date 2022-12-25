from django.forms import ModelForm
from .models import Post, PostCategory, Event, EventCategory, Message
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox, ReCaptchaV3
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

class MessageCaptchaForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    # Override the __init__(...) method of the form class to define custom label and help_texts
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['captcha'].label = ''