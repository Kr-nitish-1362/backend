from django.shortcuts import render, redirect
import requests, json
from mysite.constants import API_BASEPATH

def UserRegisterForm(request):
    if request.method == 'GET':
        return render(request,'user_management_app/register.html')

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
        return render(request,'user_management_app/login.html')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        headers = {
            'Content-Type': 'application/json',
        }

        url = API_BASEPATH + "login/"
        payload=json.dumps({
            'email' : email,
            'password' : password,
        })
        
        response = json.loads(requests.request("POST", url, data=payload, headers=headers).text)

        if 'access_token' and 'refresh_token' in response:
            request.session["access_token"] = response['access_token']
            request.session["refresh_token"] = response['refresh_token']
            return redirect('dashboard')
        else:
            return render(request,'user_management_app/login.html', {'error': response['error']})
            
def UserLogout(request):
    if request.method == 'GET':
        del request.session['access_token']
        del request.session['refresh_token']
        return redirect('sign-in')

def UpdateUserProfie(request):
    if request.method == 'GET':
        try:
            url = API_BASEPATH + "user/"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f"Bearer {request.session['access_token']}"
            }

            response = json.loads(requests.request("GET", url, headers=headers).text)
            return render(request, 'user_management_app/updateprofile.html', {'response' :  response})
        except:
            return redirect('/')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')

        try:
            url = API_BASEPATH + "user/"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f"Bearer {request.session['access_token']}"
            }
            
            payload=json.dumps({
                'first_name' : first_name,
                'last_name' : last_name,
                'email' : email,
                'address' : address
            })

            response = json.loads(requests.request("PATCH", url, data=payload, headers=headers).text)
            return redirect('dashboard')
        except:
            return redirect('/')

def DeleteUserProfile(request):
    try:
        url = API_BASEPATH + "user/"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {request.session['access_token']}"
        }

        response = json.loads(requests.request("DELETE", url, headers=headers).text)
        return redirect('sign-up')
    except:
        return redirect('dashboard')