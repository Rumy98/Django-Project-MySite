from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def account_view(request):
    # return HttpResponse("<h3>Welcome to the accounts section</h3>")
    return render(
        request,
        template_name='accounts.html'
    )

def add(a,b):
    return a+b
def form_submit_view(request):
    username=request.GET.get("username")
    email=request.GET.get("email")
    print(username)
    print(email)
    return HttpResponse('<h1>Form submitted</h1>')
