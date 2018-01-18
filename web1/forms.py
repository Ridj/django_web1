from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    # The simplest version of a  ModelForm consists of a nested Meta
    # class telling Django which model to base the form on and which
    # fields to include in the form.
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}