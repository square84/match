from django.contrib.auth import get_user_model
from django.shortcuts import render,get_object_or_404
from .models import Profile
# Create your views here.
User = get_user_model()

def profile_view(request,username):
    user = get_object_or_404(User,username=username)
    profile,created = Profile.objects.get_or_create(user=user)
    context = {"profile":profile}
    return render(request,"profiles/profile_view.html",context)
