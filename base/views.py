from django.shortcuts import render
from .services import get_categories
from .forms import MessageForm
# Create your views here.

def home(request):
    context = {}
    cats  = get_categories()
    context['cats'] = cats
    return render(request,'Base/home.html' , context)

def contact(request):
    context = {}
    form = MessageForm()
    context['form'] = form
    if request.method == 'POST':
        form = MessageForm(request.POST)
        print('here')
        if form.is_valid():
            form.save()
    return render(request,'Base/contact.html' , context)
