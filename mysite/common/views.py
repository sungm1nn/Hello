from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages, auth
# from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password

# Create your views here.
def signup(request):
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form':form})

@login_required(login_url='common:login')
def info(request):
    return render(request, 'common/info.html')

# @login_required(login_url='common:login')
# def changepw(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('index')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'common/changepw.html', {'form': form})

def changepw(request):
  if request.method == "POST":
    user = request.user
    origin_password = request.POST["origin_password"]
    if check_password(origin_password, user.password):
      new_password = request.POST["new_password"]
      confirm_password = request.POST["confirm_password"]
      if new_password == confirm_password:
        user.set_password(new_password)
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('index')
      else:
        messages.error(request, 'Password not same')
    else:
      messages.error(request, 'Password not correct')
    return render(request, 'common/changepw.html')
  else:
    return render(request, 'common/changepw.html')