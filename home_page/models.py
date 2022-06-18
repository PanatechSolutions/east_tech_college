from django.db import models

# Create your models here.


#Customizing home page

class Customize_home_page(models.Model):
    
    Certificate = "Certificate"
    Diploma ="Diploma"
    Degree = "Degree"
    
    level_of_education = [
        (Certificate, "Certificate"),
    (Diploma, "Diploma"),
    (Degree, "Degree"),
    ]
    
    opening_time = models.CharField(max_length=20, default="8am")
    closing_time = models.CharField(max_length=20, default="4pm")
    office_venue = models.CharField(max_length=150, default="Ushirika Plaza, Chuka")
    ETC_mail = models.CharField(max_length=200, default="easttechnicalcollege@gmail.com")
    ETC_phone = models.CharField(max_length=20, default="0792094889")    
    school_logo = models.ImageField(upload_to="Site Images", default="easttech logo.jfif")
    
    
class myCarousel(models.Model):
    carousel_message = models.CharField(max_length=200, default="Value Added Education")
    carousel_second_message = models.CharField(max_length=200, default="Join us Now")
    carousel_button = models.CharField(max_length=20, default="Apply")
    home_carousel_pics = models.ImageField(upload_to="Site Carousels", default="easttech logo.jfif")    
    
class Customize_home_page_gallery_courses(models.Model):
    Certificate = "Certificate"
    Diploma ="Diploma"
    Degree = "Degree"

    level_of_education = [
    (Certificate, "Certificate"),
    (Diploma, "Diploma"),
    (Degree, "Degree"),
    ]
    
    Hospitality = "Hospitality"
    Computing = "Computing"
    Business = "Business"
    
    school = [
    (Hospitality, "Hospitality"),
    (Computing, "Computing"),
    (Business, "Business"),
    ]
    
    edu_level=models.CharField(max_length=50, choices=level_of_education, default=Certificate)
    
    course=models.TextField(max_length=200,  default="Hotel Management")
    
    edu_school=models.CharField(max_length=50, choices=school, default=Hospitality)
    
    course_duration = models.CharField(max_length=10, default="1 year")
    
    course_require = models.CharField(max_length=200, default="KCSE Mean Grade C")
        
    gallery_pics = models.ImageField(upload_to="Site Gallery", default="easttech logo.jfif")
    
    button_text = models.CharField(max_length=50, default="Apply now")
    
    
class Customize_study_with_section(models.Model):
    reason_pics = models.ImageField(upload_to="Reason Gallery", default="easttech logo.jfif")
    picture_label = models.TextField(max_length=200, default="As a East Technical College, we boasts of a number of reasons to why join us.")
    major_reason = models.TextField(max_length=200, default="Quality Knowledge")
    minor_details = models.TextField(max_length=500, default="Learn from the best Instructors")
    
class Message_From_Principle(models.Model):
    Incharge_designation = models.CharField(max_length=50, default="PRINCIPAL")
    Incharge_pic = models.ImageField(upload_to="In charge", default="easttech logo.jfif")
    Incharge_name = models.CharField(max_length=50, default="PRINCIPAL")
    message_title = models.CharField(max_length=200, default="Welcome to East Technical College")
    Incharge_message = models.TextField(max_length=600, default="Welcome to East Technical College")
    


class Message_From_Alumni(models.Model):
    Alumni_designation = models.CharField(max_length=50, default="Business Manager")
    Alumni_pic = models.ImageField(upload_to="Alumini", default="easttech logo.jfif")
    Alumni_name = models.CharField(max_length=50, default="Ananymous")
    Alumni_message = models.TextField(max_length=600, default="East Technical College is the place to be")



class About_ETC(models.Model):
    About_gallery_pic = models.ImageField(upload_to="About us", default="easttech logo.jfif")
    About_title = models.CharField(max_length=50, default="ABOUT EAST TECHNICAL COLLEGE")
    About_pic = models.ImageField(upload_to="About us", default="easttech logo.jfif")
    About_message = models.TextField(max_length=600, default="East Technical College is the place to be")
    About_update = models.CharField(max_length=50, default="4 hours")


