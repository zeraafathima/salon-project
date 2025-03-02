
from django import forms
from django.core.validators import RegexValidator
from datetime import datetime

class Booking(forms.Form):
    SERVICE_CHOICES = [
        ('consultation', 'Consultation'),
        ('hair cutting', 'Hair Cutting'),
        ('wedding', 'Wedding Services'),
        ('other', 'Other')
    ]
    
    TIME_CHOICES = [
        ('09:00', '9:00 AM'),
        ('10:00', '10:00 AM'),
        ('11:00', '11:00 AM'),
        ('12:00', '12:00 PM'),
        ('13:00', '1:00 PM'),
        ('14:00', '2:00 PM'),
        ('15:00', '3:00 PM'),
        ('16:00', '4:00 PM'),
    ]

    full_name = forms.CharField(
        max_length=100,
        label="Full Name",
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg mb-3', 
            'placeholder': 'Steve Joe',
            'style': 'border-radius: 8px;'
        })
    )
    
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg mb-3', 
            'placeholder': 'stevejoe@gmail.com',
            'style': 'border-radius: 8px;'
        })
    )
    
    phone_number = forms.CharField(
        max_length=15,
        label="Phone Number",
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')],
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg mb-3', 
            'placeholder': '+1234567890',
            'style': 'border-radius: 8px;'
        })
    )
    
    service_type = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        label="Type of Service",
        widget=forms.Select(attrs={
            'class': 'form-select form-control-lg mb-3', 
            'style': 'border-radius: 8px;'
        })
    )
    
    appointment_date = forms.DateField(
        label="Preferred Appointment Date",
        widget=forms.DateInput(attrs={
            'class': 'form-control form-control-lg mb-3', 
            'type': 'date',
            'min': datetime.today().strftime('%Y-%m-%d'),
            'style': 'border-radius: 8px;'
        })
    )
    
    appointment_time = forms.ChoiceField(
        choices=TIME_CHOICES,
        label="Preferred Appointment Time",
        widget=forms.Select(attrs={
            'class': 'form-select form-control-lg mb-3', 
            'style': 'border-radius: 8px;'
        })
    )
    
    notes = forms.CharField(
        label="Additional Notes",
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control form-control-lg mb-3', 
            'placeholder': 'Any special requests or information',
            'rows': 4,
            'style': 'border-radius: 8px;'
        })
    )
    
    def Booking(self):
        appointment_date = self.cleaned_data.get("appointment_date")
        if appointment_date < datetime.today().date():
            raise forms.ValidationError("Appointment date cannot be in the past.")
        if appointment_date.weekday() in [5, 6]:  # Weekends not allowed
            raise forms.ValidationError("Appointments cannot be scheduled on weekends.")
        return appointment_date

