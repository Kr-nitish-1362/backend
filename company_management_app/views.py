from django.shortcuts import render, redirect
from mysite.constants import API_BASEPATH
import requests, json

def CompanyForm(request):
    if request.method == 'GET' and 'access_token' in request.session:
        return render(request, 'company_management_app/addcompany.html')
    else:
        return redirect('/')

    # Api call for create company
    if request.method == 'POST' and 'access_token' in request.session:
        company_name = request.POST.get('company_name')
        company_address = request.POST.get('company_address')
        gst_number = request.POST.get('gst_number')
        business_email = request.POST.get('business_email')
        company_description = request.POST.get('company_description')

        try:
            url = API_BASEPATH + "company/"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f"Bearer {request.session['access_token']}"
            }
            payload=json.dumps({
                'company_name': company_name,
                'company_address': company_address,
                'gst_number': gst_number,
                'business_email': business_email,
                'company_description': company_description,
            })

            response = json.loads(requests.request("POST", url, data=payload, headers=headers).text)
            return redirect('dashboard')
        except:
            return redirect('add-company')
    else:
        return redirect('/')

def UpdateCompanyForm(request):
    if request.method == 'GET' and 'access_token' in request.session:
        try:
            url = API_BASEPATH + "company/"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f"Bearer {request.session['access_token']}"
            }

            response = json.loads(requests.request("GET", url, headers=headers).text)
            return render(request, 'company_management_app/updatecompany.html', {'response' :  response})
        except:
            return redirect('add-company')
    else:
        return redirect('/')

    if request.method == 'POST' and 'access_token' in request.session:
        company_name = request.POST.get('company_name')
        company_address = request.POST.get('company_address')
        gst_number = request.POST.get('gst_number')
        business_email = request.POST.get('business_email')
        company_description = request.POST.get('company_description')

        try:
            url = API_BASEPATH + "company/"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f"Bearer {request.session['access_token']}"
            }
            payload=json.dumps({
                'company_name': company_name,
                'company_address': company_address,
                'gst_number': gst_number,
                'business_email': business_email,
                'company_description': company_description,
            })

            response = json.loads(requests.request("PATCH", url, data=payload, headers=headers).text)
            print(response)
            return redirect('dashboard')
        except:
            return redirect('add-company')
    else:
        redirect('/')

def DeleteCompany(request):
    try:
        url = API_BASEPATH + "company/"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {request.session['access_token']}"
        }

        response = json.loads(requests.request("DELETE", url, headers=headers).text)
        return redirect('dashboard')
    except:
        return redirect('dashboard')