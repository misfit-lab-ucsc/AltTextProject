from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# register new users
def register(request,*args,**kwargs):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save(*args, **kwargs)
            messages.success(request,f'You account has now been created you are now able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    # dictionary to pass title and form to HTML to render
    context = {
        'form' : form,
        # title tag for signing up
        'title' : 'Registration',
    }
    # render
    return render(request,'users/register.html',context)

# view our profile of our users
@login_required
def profile(request):
    print('you are logged in')
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        # check either form is valid
        if u_form.is_valid() or p_form.is_valid():
            # check both
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request,'Your account has been updated')
            # update either username or image for profile
            elif u_form.is_valid():
                u_form.save()
                messages.success(request,'Your username has been updated')
            elif p_form.is_valid():
                p_form.save()
                messages.success(request,'Your profile picture has been updated')
            else:
                messages.warning(request,'Something went wrong please try again')
            
            
    else:
        # not post request
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form,
        # title tag for login
        'title' : 'Profile',
        # messages for user feedback on update
        'messages' : messages.get_messages(request)
    }
    return render(request,'users/profile.html',context)
