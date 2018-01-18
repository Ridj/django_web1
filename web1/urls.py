"""Defines URL patterns for web1 application."""
from django.conf.urls import url
from . import views

app_name = "web1"

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Some page
    url(r'page/', views.page, name='page'),

    # Show all topics.
    url(r'^topics/$', views.topics, name='topics'),
    # When Django examines a requested URL, this pattern will match any
    # URL that has the base URL followed by topics.

    # Detail page for a single topic.
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # The r tells Django to interpret the string as a raw string, and
    # the expression is contained in quotes. The second part of the
    # expression,  /(?P<topic_id>\d+)/ , matches an integer between two
    # forward slashes and stores the integer value in an argument called
    # topic_id.  The parentheses surrounding this part of the expression
    # captures the value stored in the URL; the ?P<topic_id> part stores
    # the matched value in topic_id ; and the expression \d+ matches any
    # number of digits that appear between the forward slashes.

    # Page for adding a new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
]
