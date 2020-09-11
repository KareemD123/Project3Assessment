from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView
from .models import Widget
from .forms import WidgetForm
# Define the home view


def home(request):
    widget = Widget.objects.all
    form = WidgetForm()
    return render(request, 'index.html', {'form': form, 'widget': widget})
# Create your views here.


class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'
    success_url = '/'


def add_widget(request, widget_id):
    # create the ModelForm using the data in request.POST
    form = WidgetForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_widget = form.save(commit=False)
        new_widget.widget_id = widget_id
        new_widget.save()
    return redirect('index', {'form': form})


class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'
