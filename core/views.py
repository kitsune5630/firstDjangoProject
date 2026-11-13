from django.shortcuts import render
from .models import UserModel
from django.http import HttpResponseRedirect, HttpResponseNotFound


# Create your views here.
def index(request):
    users = UserModel.objects.all()
    data = {"users": users}
    return render(request, 'index.html', data=data)

def create(request):
    if request.method == "POST":
        user = UserModel()
        user.name = request.POST.get("name")
        user.password = request.POST.get("password")
        user.save()
    return HttpResponseRedirect("/")

def edit(request, id):
    try:
        user = UserModel.objects.get(id=id)

        if request.method == "POST":
            user.name = request.POST.get("name")
            user.password = request.POST.get("password")
            user.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"user": user})
    except UserModel.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")

def delete(request, id):
    try:
        user = UserModel.objects.get(id=id)
        user.delete()
        return HttpResponseRedirect("/")
    except UserModel.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")

