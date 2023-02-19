from django.shortcuts import render, redirect
from mysite.constants import API_BASEPATH
import requests, json

# Create your views here.
def Dashboard(request):
    if request.method == 'GET':
        try:
            url = API_BASEPATH + "user/"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f"Bearer {request.session['access_token']}"
            }
            response = json.loads(requests.request("GET", url, headers=headers).text)
            return render(request, 'common_app/dashboard.html', {'response' : response})
        except:
            return redirect('sign-in')
        