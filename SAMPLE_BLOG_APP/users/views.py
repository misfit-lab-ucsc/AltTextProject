from django.shortcuts import render , redirect
# for forms for register
# from django.contrib.auth.forms import UserCreationForm
# add flash for alerts
from django.contrib import messages
# types of messages
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Register view for new user
def register(request,*args, **kwargs):
    # check if request is post and then validate otherwise then take them to same page and erase data entered
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # check if form valid
        if form.is_valid():
            # save the user
            form.save(*args, **kwargs)
            # grab username
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has now been created! You are now able to Log in!')
            # redirect user after message to login page
            return redirect('login')
    else:
        form = UserRegisterForm()
    #create form pass to template
    return render(request,'users/register.html',{'form':form})

# profile view so that our user can see their own profile
# user must be logged in to access page
@login_required
def profile(request):
    # when submit form and possibly pass new data
    if request.method == 'POST':
        # put information of current login user do this by passing instance
        # use request.post to pass post data
        u_form = UserUpdateForm(request.POST,instance=request.user)
        # profile form we are getting additional data file data with request the user image
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        # checking if both forms are valid
        if u_form.is_valid() and p_form.is_valid():
            # save the data
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated')
            # redirect user after message 
            return redirect('profile')
    else:
        # not post request
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {'u_form' : u_form,
               'p_form' : p_form}
    return render(request,'users/profile.html',context)
