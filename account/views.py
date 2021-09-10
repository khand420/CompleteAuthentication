from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,UserRegistrationForm,UserEditForm,ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages



@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section':'dashboard'})

# FOR USER LOGIN 
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],
                                      password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated'' Successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse("Invalid login")
    else:
        form=LoginForm()
    return render(request,'account/login.html',{'form':form})

# FOR USER REGISTRATION 
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form=UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})

# FOR EDITTING USER PROFILE 
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid(): #both are valited than save both the data and it will updated from the corresponding objects in the db 
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile Updated Successfully')
        else:
            messages.error(request, 'Error in Updating your Profile.')
    else:
        user_form = UserEditForm(instance=request.user) #UserEditForm- help to store the data of the built in user model
        profile_form = ProfileEditForm(instance=request.user.profile) # ProfileEditForm- to store additional porfile data which we have made in the model profile
    return render(request,'account/edit.html',{'user_form':user_form,'profile_form':profile_form})


