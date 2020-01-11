from django.shortcuts import render, redirect
from .forms import UserEnrollmentForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserEnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserEnrollmentForm()
    return render(request, 'users/enrollment.html', {'form':form, 'title': 'Enrollment'})


def home(request):
    return render(request, 'posts/home.html')