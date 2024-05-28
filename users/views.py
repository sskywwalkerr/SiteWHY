from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserOurRegistration
from django.contrib.auth import logout



def register(request):
    if request.method == 'POST':
        form = UserOurRegistration(request.POST);
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('home')
    else:
        form = UserOurRegistration()
    return render(request, 'registration.html', {'form': form})

