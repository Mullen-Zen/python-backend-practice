import re
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.timezone import datetime
from django.views.generic import ListView
from hello.forms import LogMessageForm
from hello.models import LogMessage

# Create your views here.

# def home(request):
#     return render(request, "hello/home.html")

class HomeListView(ListView):
    """Renders the homepage, with a list of all past logs"""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def hello_there(request, name):
    return render(
        request,
        'hello/hellothere.html',
        {
        'name': name,
        'date': datetime.now()
        }
    )

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})
    
