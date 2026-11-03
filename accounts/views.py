from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def account_view(request):
    # return HttpResponse("<h3>Welcome to the accounts section</h3>")
    return render(
        request,
        template_name='accounts.html'
    )