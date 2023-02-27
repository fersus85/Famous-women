from django import forms
from django.core.exceptions import ValidationError

from .models import *


# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label='Title')
#     slug = forms.SlugField(max_length=255, label='URL')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Article')
#     is_published = forms.BooleanField(label='published', initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', empty_label='Category not chosen')


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'category not chosen'

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError
        return title
