from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

from .models import Login
from .forms import LoginForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("details")
    else:
        form = LoginForm()
        
    context = {"form": form}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))
    # context = {}
    # template = loader.get_template("index.html");
    # return HttpResponse(template.render(context, request));

# def login(request):
#     email = request.POST["email"]
#     password = request.POST["password"]

#     if "@" not in email:
#         print("Invalid email")
    
#     Login.objects.create(email=)
#     context = {"useremail": email, "userpassword": password}
#     template = loader.get_template("home.html")
#     return HttpResponse(template.render(context, request))

# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)

#         if form.is_valid():
#             form.save()
#         else:
#             print("Invalid form")
#     else:
#         form = LoginForm()



def details(request):
    detailsList = Login.objects.all()
    context = {"details": detailsList}
    template = loader.get_template("details.html")
    return HttpResponse(template.render(context, request))