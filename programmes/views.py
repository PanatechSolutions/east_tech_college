from multiprocessing import context
from django.shortcuts import render
from django.views.generic import View
from home_page.models import Customize_home_page
from .models import Programmes_Offered, ApplicationForm
from .forms import Student_Application_Form
from .forms import StudentFillForm
from django.http import HttpResponseRedirect
# Create your views here.

#for pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
#end of pdf imports


import json


def mySave(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Add some lines of text
    #lines = [
    #	"This is line 1",
    #	"This is line 2",
    #	"This is line 3",
    #]

    # Designate The Model
    fname = ''
    gen = ''
    sno = ''
    logo = Customize_home_page.objects.filter().values_list('school_logo', flat=True)
    
    venues = ApplicationForm.objects.filter(religion='Christian').values()
    #print(venues.values)
    fname = venues[0]["applicant_first_name"]
    sname = venues[0]["applicant_middle_name"]
    lname = venues[0]["applicant_last_name"]
    gender = venues[0]["gender"]
    
    print(fname)
    
    for v in venues:
        print(v)
        print("\n")
    
    lines = [
        "                                   EAST TECHNICAL COLLEGE",
        "                                       ADMISSION LETTER",
        "",
        "        Name of Student :                       "+ fname+ " "+ sname+" "+lname,
        
        "This is line 3"+ gender,
    ]    

    #reli = ''
    # Create blank list
    #lines = []

    """for venue in venues:
        print(venue.religion)
        lines.append(venue.applicant_first_name)
        lines.append(venue.gender)
        lines.append(venue.marital_status)
        lines.append(venue.religion)
        lines.append(venue.mobile_number)
        lines.append(venue.postal_code)
        lines.append(" ")
        #print(lines)
        if venue.religion == "Christian":
            reli = venue.religion

    # Loop
    rowsl = len(lines)
    for l in range(0, rowsl):
        #print(lines[l])
        textob.textLine(lines[l])"""
    
    for line in lines:
        textob.textLine(line)

    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return something   HttpResponseRedirect

    return FileResponse(buf, as_attachment=True, filename="Course_Application_Letter.pdf")
            
  

def programmes(request):
    upperHome_page = Customize_home_page.objects.all()
    program = Programmes_Offered.objects.all()
    form = Student_Application_Form()
    
    submitted = False
    
    if request.method == "POST":
        form2 = StudentFillForm(request.POST)
        if form2.is_valid():
            form2.save()
            
            return HttpResponseRedirect('/programmes/programmes/?submitted=True')


            
        
    else:
        form2 = StudentFillForm
        if 'submitted' in request.GET:
            submitted = True
            mySave(request)
        
    
    form2 = StudentFillForm
    return render(request,"programmes.html",{'upperHomePage':upperHome_page,"program":program,'form':form,"form2":form2,'submitted':submitted})

def computing(request):
    upperHome_page = Customize_home_page.objects.all()
    program = Programmes_Offered.objects.all()    
    return render(request,"school_of_computing.html",{'upperHomePage':upperHome_page,"program":program})

def business(request):
    upperHome_page = Customize_home_page.objects.all()
    program = Programmes_Offered.objects.all()    
    return render(request,"business_studies.html",{'upperHomePage':upperHome_page,"program":program})

def submit_Application(request):
    if request.method == "POST":
        applicant_first_name = request.POST["applicant_first_name"]
        applicant_middle_name = request.POST["applicant_middle_name"]
        applicant_last_name = request.POST["applicant_last_name"]
        gender = request.POST["gender"]
        dob = request.POST["dob"]
        marital_status = request.POST["marital_status"]
        religion = request.POST["religion"]
        nationality = request.POST["nationality"]
        idno = request.POST["idno"]
        mobile_number = request.POST["mobile_number"]
        home_district = request.POST["home_district"]
        applicant_email = request.POST["applicant_email"]
        postal_address = request.POST["postal_address"]
        postal_code = request.POST["postal_code"]
        town = request.POST["town"]
        county = request.POST["county"]
        applicant_parent = request.POST["applicant_parent"]
        applicant_parent_number = request.POST["applicant_parent_number"]
        course_applied = request.POST["course_applied"]
        
    else:
        pass
    return render(request,"school_of_computing.html")


def Application_Letter(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Add some lines of text
    #lines = [
    #	"This is line 1",
    #	"This is line 2",
    #	"This is line 3",
    #]

    # Designate The Model
    fname = ''
    gen = ''
    sno = ''
    logo = Customize_home_page.objects.filter().values_list('school_logo', flat=True)
    
    venues = ApplicationForm.objects.filter(religion='Christian').values()
    #print(venues.values)
    fname = venues[0]["applicant_first_name"]
    sname = venues[0]["applicant_middle_name"]
    lname = venues[0]["applicant_last_name"]
    gender = venues[0]["gender"]
    
    print(fname)
    
    for v in venues:
        print(v)
        print("\n")
    
    lines = [
        "                                   EAST TECHNICAL COLLEGE",
        "                                       ADMISSION LETTER",
        "",
    	"        Name of Student :                       "+ fname+ " "+ sname+" "+lname,
    	
        "This is line 3"+ gender,
    ]    

    #reli = ''
    # Create blank list
    #lines = []

    """for venue in venues:
        print(venue.religion)
        lines.append(venue.applicant_first_name)
        lines.append(venue.gender)
        lines.append(venue.marital_status)
        lines.append(venue.religion)
        lines.append(venue.mobile_number)
        lines.append(venue.postal_code)
        lines.append(" ")
        #print(lines)
        if venue.religion == "Christian":
            reli = venue.religion

    # Loop
    rowsl = len(lines)
    for l in range(0, rowsl):
        #print(lines[l])
        textob.textLine(lines[l])"""
    
    for line in lines:
        textob.textLine(line)

    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return something

    return FileResponse(buf, as_attachment=True, filename="Course_Application_Letter.pdf")
          
