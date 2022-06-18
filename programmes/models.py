from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Programmes_Offered(models.Model):
    
    def validate_year(value):
        mydate = date.today().year
        if value < mydate or value > mydate+2:
            raise ValidationError(u'%s is not a valid year!'% value)
    
    Hospitality = "Hospitality"
    Computing = "Computing"
    Business = "Business"
    
    school = [
    (Hospitality, "Hospitality"),
    (Computing, "Computing"),
    (Business, "Business"),
    ]
    
    KNEC = "KNEC"
    KASNEB = "KASNEB"
    NITA = "NITA"
    ICDL = "ICDL"
    optional_examinational_body="East Technical Institute"
    
   
    examination_by = [
    (KNEC, "KNEC"),
    (KASNEB, "KASNEB"),
    (NITA, "NITA"),
    (ICDL, "ICDL"),
    (optional_examinational_body,"East Technical Institute"),
    ]
    
    school=models.CharField(max_length=50, choices=school, default=Hospitality)
    programme_name=models.CharField(max_length=250)
    programme_duration=models.CharField(max_length=200, default="1 year")
    programme_requirements=models.TextField(max_length=200, default="KCSE Grade C")
    Intake_from=models.DateField()
    Intake_to=models.DateField()
    examination_body = models.CharField(max_length=50, choices=examination_by, default="East Technical Institute")
    vacancy = models.BooleanField(default=False)
    apply_button = models.CharField(max_length=200, default="Apply")
    

class ApplicationForm(models.Model):
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    
    MARITAL_STATUS = (
        ('Married','Married'),
        ('Single','Single'),
        ('Divorced','Divorced'),
        ('Other','Other'),
    )
    RELIGION_STATUS = (
        ('Christian','Christian'),
        ('Muslim','Muslim'),
        ('Hindu','Hindu'),
        ('None Religion','None Religion'),
    )
    
    KENYA_COUNTIES = (
        ('Mombasa','Mombasa'),
        ('Nairobi','Nairobi'),('Tharaka Nithi','Tharaka Nithi'),
        ('Meru','Meru'),('Isiolo','Isiolo'),('Nyeri','Nyeri'),
        ('Embu','Embu'),('Kirinyaga','Kirinyaga'),('Kitui','Kitui'),
        ('Nakuru','Nakuru'),
    )
    
    applicant_first_name = models.CharField(max_length=50)
    applicant_middle_name = models.CharField(max_length=50)
    applicant_last_name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER,max_length=6)
    dob = models.DateField()
    marital_status = models.CharField(choices=MARITAL_STATUS,max_length=8)
    religion = models.CharField(choices=RELIGION_STATUS,max_length=50)
    nationality = models.CharField(max_length=50)
    idno = models.PositiveIntegerField()
    mobile_number = models.PositiveIntegerField()
    home_district = models.CharField(max_length=50)
    applicant_email = models.EmailField()
    postal_address = models.PositiveIntegerField()
    postal_code = models.PositiveIntegerField()
    town = models.CharField(max_length=50)
    county = models.CharField(choices=KENYA_COUNTIES,max_length=50)
    applicant_parent = models.CharField(max_length=50)
    applicant_parent_number = models.PositiveIntegerField()
    course_applied = models.CharField(max_length=50)
    
    def __str__(self):
        return self.applicant_first_name
    
    

"""
class User(AbstractUser):
    
    gender = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    
    student_email = models.EmailField()
    student_first_name = models.CharField(max_length=3)
    student_last_name = models.CharField(max_length=3)
    password = models.CharField(max_length=256)
    repeat_password  = models.CharField(max_length=256)    
    student_gender = models.CharField(choices=gender,max_length=6)
    
 """   

