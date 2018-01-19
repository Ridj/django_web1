from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    # The simplest version of a  ModelForm consists of a nested Meta
    # class telling Django which model to base the form on and which
    # fields to include in the form.
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        # A widget is an HTML form element, such as a single-line text
        # box, multi-line text area, or drop-down list.  By including
        # the widgets attribute you can override Django’s default widget
        # choices.  By telling Django to use a  forms.Textarea element,
        # we’re customizing the input widget for the field 'text' so the
        # text area will be 80 columns wide instead of the default 40.
