from django.shortcuts import render

# Create your views here.

def admissions(request):
    return render(request,"admissions.html")

def apply_online(request):
    return render(request,"online_application.html")

def requirements(request):
    return render(request,"requirements.html")

def fees(request):
    return render(request,"fees.html")

def payment_details(request):
    return render(request,"payment_details.html")

def faqs(request):
    return render(request,"faqs.html")