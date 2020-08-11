from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('accounts')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            if request.GET.get('next') != '':
                return redirect(request.GET.get('next'))
            else:
                return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})