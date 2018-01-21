from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """A topic the user is learning about"""
    # Model —a parent class included in Django that defines the basic
    # functionality of a model.
    text = models.CharField(max_length=200)
    # CharField when you want to store a small amount of text, such as
    # a name, a title, or a city.
    date_added = models.DateTimeField(auto_now_add=True)
    # DateTimeField —a piece of data that will record a date and time.
    owner = models.ForeignKey(User, on_delete=None)
    # We add an owner field to  Topic , which establishes a foreign key
    # relationship to the User model

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=None)
    # A foreign key is a database term; it’s a reference to another
    # record in the database.  This is the code that connects each entry
    # to a specific topic.  Each topic is assigned a key, or ID, when
    # it’s created.  When Django needs to establish a connection between
    # two pieces of data, it uses the key associated with each piece of
    # information.  We’ll use these connections shortly to retrieve all
    # the entries associated with a certain topic.
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Meta holds extra information for managing a model; here it
        # allows us to set a special attribute telling Django to use
        # Entries when it needs to refer to more than one entry.
        # Getting Started with Django 409 (Without this, Django would
        # refer to multiple entries as Entrys.)
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text
        # Finally, the  __str__() method tells Django which information
        # to show when it refers to individual entries.  Because an
        # entry can be a long body of text, we tell Django to show just
        # the first 50 characters of text.  We also add an ellipsis to
        # clarify that we’re not always displaying the entire entry.
