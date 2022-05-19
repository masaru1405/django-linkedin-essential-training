from django import forms
from .models import Note
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ('title', 'text')
    labels = {
      'text': 'Write your text here:',
      'title': 'Write a nice title here:'
    }
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
      'text': forms.Textarea(attrs={'class': 'form-control my-5'})
    }

  """ def clean_title(self):
    title = self.cleaned_data['title']
    if 'Django' not in title:
      raise ValidationError('We only accept notes about Django!')
    return title """