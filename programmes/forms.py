from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import ApplicationForm
from django.urls import reverse_lazy
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Reset
### from .models import Post


class Student_Application_Form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('programmes')
        self.helper.form_method = "GET"
        self.helper.add_input(Reset('clear','Clear Form Content'))
        self.helper.add_input(Submit('submit','Submit Application'))
        
 
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
    )
    
    applicant_first_name = forms.CharField(widget=forms.TextInput(attrs={
        'hx-get': reverse_lazy('programmes'),
        'hx-trigger': 'keyup'
    }))
    applicant_middle_name = forms.CharField()
    applicant_last_name = forms.CharField()
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date','max':datetime.now().date()}))
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS, widget=forms.RadioSelect())
    religion = forms.ChoiceField(choices=RELIGION_STATUS, widget=forms.RadioSelect())
    nationality = forms.CharField()
    idno = forms.IntegerField()
    mobile_number = forms.IntegerField()
    home_district = forms.CharField()
    applicant_email = forms.EmailField()
    postal_address = forms.IntegerField()
    postal_code = forms.IntegerField()
    town = forms.CharField()
    county = forms.ChoiceField(choices=KENYA_COUNTIES)
    applicant_parent = forms.CharField()
    applicant_parent_number = forms.IntegerField()
    course_applied = forms.CharField()



# form for students to fill in database

class StudentFillForm(ModelForm):
    class Meta:
        model = ApplicationForm
        fields = "__all__"
        Widgets = {
            'applicant_first_name': forms.TextInput(attrs={'class':'form-control','placehoder':'Name'}),
            'applicant_middle_name': forms.TextInput(attrs={'class':'form-control'}),
            'applicant_last_name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control'})
            
        }