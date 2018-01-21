from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """The home page for Web1"""
    return render(request, 'web1/index.html')


def page(request):
    """The simple page for Web1"""
    return render(request, 'web1/page.html')


@login_required
# We apply login_required() as a decorator to the  topics() view
# function by prepending login_required with the @ symbol so Python
# knows to run the code in login_required() before the code in opics().
def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    # Query the database by asking for the Topic objects, sorted by the
    # date_added attribute.
    context = {'topics': topics}
    # A context is a dictionary in which the keys are names we’ll use in
    # the template to access the data and the values are the data we
    # need to send to the template.  In this case, there’s one key-value
    # pair, which contains the set of topics we’ll display on the page.
    return render(request, 'web1/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # The code phrases are called queries, because they query the
    # database for specific information.  When you’re writing queries
    # like these in your own projects, it’s very helpful to try them out
    # in the Django shell first.  You’ll get much quicker feed back in
    # the shell than you will by writing a view and template and then
    # checking the results in a browser.
    entries = topic.entry_set.order_by('-date_added')
    # The minus sign in front of  date_added sorts the results in
    # reverse order.
    context = {'topic': topic, 'entries': entries}
    return render(request, 'web1/topic.html', context)

# You use GET requests for pages that only read data from the server.
# You usually use POST requests when the user needs to submit
# information through a form.

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            # We can’t save the submitted information in the database
            # until we’ve checked that it’s valid.  The is_valid()
            # function checks that all required fields have been filled
            # in (all fields in a form are required by default) and that
            # the data entered matches the field types expected—for
            # example, that the length of  text is less than 200
            # characters, as we specified in models.py.
            form.save() # Writes the data from the form to the database.
            return HttpResponseRedirect(reverse('web1:topics'))
            # HttpResponseRedirect used to redirect the reader back to
            # the  topics page after they submit their topic.
            # The reverse() function determines the URL from a named
            # URL pattern, meaning that Django will generate the URL
            # when the page is requested.

    context = {'form': form}
    return render(request, 'web1/new_topic.html', context)

# Depending on the request, we’ll know whether the user is requesting
# a blank form (a GET request) or asking us to process a completed form
# (a POST request).

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    #  topic_id parameter to store the value it receives from the URL.

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process datf.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            # When we call  save() , we include the argument
            # commit=False to tell Django to create a new entry object
            # and store it in  new_entry without saving it to the
            # database yet.
            new_entry.topic = topic
            new_entry.save()
            # This saves the entry to the database with the correct
            # associated topic.
            return HttpResponseRedirect(reverse('web1:topic',
                                                args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'web1/new_entry.html', context)


def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('web1:topic',
                                                args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'web1/edit_entry.html', context)
