from django.db import models

# Create your models here.


class Booking(models.Model):
    SERVICE_CHOICES = [
        ('consultation', 'Consultation'),
        ('follow_up', 'Follow-Up Appointment'),
        ('therapy', 'Therapy Session'),
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

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=5, choices=TIME_CHOICES)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.appointment_date} at {self.appointment_time}"


    
class Service(models.Model):

    title = models.CharField(max_length=100)  # This field should be defined
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
   


    def __str__(self):
        return self.title
    

    
    

    
class Designer(models.Model):

    img_designers= models.ImageField(upload_to='designers')
    d_name=models.CharField(max_length=100)
    d_spec=models.TextField()
    d_desc = models.TextField()
   
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.

class Stylist(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='stylists/')  # Ensure media files are properly handled

    def __str__(self):
        return self.name
