from django.shortcuts import render

def userrequests(request):
    return render(request, 'requests.html')
