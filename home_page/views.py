from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from . models import Customize_home_page,Customize_home_page_gallery_courses,Customize_study_with_section
from . models import myCarousel, Message_From_Principle,Message_From_Alumni,About_ETC

# Create your views here.
"""
class ModelView(TemplateView):
    template_name = "home_index.html"
    def get_context_data(self, **kwargs):
        context=context=super(ModelView,self).get_context_data(**kwargs)
        context.update({
            'upperHome_page':Customize_home_page.objects.all(),
            'carousel':myCarousel.objects.all(),
        })
        return context
    
"""

def home(request):
    upperHome_page = Customize_home_page.objects.all()
    carousel = myCarousel.objects.all()
    come_study_with_us = Customize_study_with_section.objects.all()
    gallery=Customize_home_page_gallery_courses.objects.all()
    alumini = Message_From_Alumni.objects.all()
    return render(request, "home_index.html", {'upperHomePage':upperHome_page,'carousel':carousel,'studyWithUs':come_study_with_us, 'gallery':gallery, "alumini":alumini})



def findCourse(request):
    course = Customize_home_page_gallery_courses.objects.all()
    if request.method == "POST":
        course_name = request.POST['course_name'] 
        course_level = request.POST['course_name']
        course_search = course.objects.get(course=course_name)
        course_level_search = course.objects.get(course=course_level)
        if course_search and course_level_search:
            print("printed")
         
    return render(request, "home_index.html",{'course':course})

def message_from_principal(request):
    upperHome_page = Customize_home_page.objects.all()
    message = Message_From_Principle.objects.all()
    return render(request,"principle_message.html",{ "principal_message":message, 'upperHomePage':upperHome_page })    

def about(request):
    upperHome_page = Customize_home_page.objects.all()
    etc_about=About_ETC.objects.all()
    return render(request,"about.html",{ 'upperHomePage':upperHome_page,"about":etc_about })    


