import os
from django.shortcuts import render
from userprofile.models import UserProfile
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from userprofile.forms import *



# Create your views here.
def show_profile(request):
    user_data = UserProfile.objects.get(user=request.user)

    context = {
        'user' : request.user,
        'picture' : user_data.picture,
        'bio' : user_data.bio,
        'role' : user_data.role,
        'saldo' : user_data.saldo,
        'form1' : ProfileForm,
        'form2' : TopUpForm,
    }
    
    return render(request, 'profile.html', context)

def edit_profile(request):
    user = request.user.userprofile
    if request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            obj = form.save(commit=False)

            if obj.picture:
                obj.save(update_fields=['picture'])

            if obj.bio:
                obj.save(update_fields=['bio'])
            

            return HttpResponse("success")
    
    # return JsonResponse({'error': True, 'errors': form.errors})

def edit_saldo(request):
    user = request.user.userprofile
    if request.POST:
        form = TopUpForm(request.POST, request.FILES, instance=user)

        print(form.is_valid())

        if form.is_valid():
            obj = form.save(commit=False)

            if obj.saldo:
                obj.save(update_fields=['saldo'])

            return HttpResponse('Saldo ditambah')

def show_json(request):
    profileobj = UserProfile.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", profileobj), content_type="application/json")