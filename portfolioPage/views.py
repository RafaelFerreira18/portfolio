from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import SendMessage
from .models import Message


def base(request):
    if request.method == 'POST':
        form = SendMessage(request.POST)

        if form.is_valid():
            form.save()
            return redirect('portfolioPage:base')
    else:
            form = SendMessage()
            
    return render(request, 'base.html', {
        'form' : form,
    })