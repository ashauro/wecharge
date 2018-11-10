from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm, CarUpdateForm

# Create your views here.


def show_profile(request):
    return render(request, 'profile.html')


def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        c_form = CarUpdateForm(request.POST, instance=request.user.profile.user_car)
        if u_form.is_valid() and p_form.is_valid() and c_form.is_valid():
            u_form.save()
            p_form.save()
            c_form.save()
            messages.success(request, 'Ваш профиль обновлен!')
            return redirect('Profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        c_form = CarUpdateForm(instance=request.user.profile.user_car)

    context = {
        'u_form':u_form,
        'p_form':p_form,
        'c_form':c_form,
    }
    return render(request, 'edit_profile.html', context)