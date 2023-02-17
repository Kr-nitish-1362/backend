from django.shortcuts import render, redirect
import requests, json
from mysite.constants import API_BASEPATH

def UserRegisterForm(request):
    if request.method == 'GET':
        return render(request,'register.html')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        url = API_BASEPATH + "register/"
        payload={
            'first_name' : first_name,
            'last_name' : last_name,
            'email' : email,
            'password' : password,
            'password2' : password2,
        }
        apiResult = json.loads(requests.request("POST", url, data=payload).text)
        return redirect("sign-in")

def UserLoginForm(request):
    if request.method == 'GET':
        return render(request,'login.html')
