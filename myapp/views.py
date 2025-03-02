from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import Booking
from .models import Service

from .models import Designer
from .models import Stylist
# Create your views here.

def home(request):
    dict_designers={
        'designers':Designer.objects.all()
    }
    return render(request, 'home.html',dict_designers)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def booking(request):
    if request.method == 'POST':
        form = Booking(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking was successful!')
            return redirect('booking')
    else:
        form = Booking()
    return render(request, 'booking.html', {'form': form})

def hiring(request):
    return render(request, 'hiring.html')

def event(request):
    return render(request, 'events.html')

def services(request):
    dict_service={
        'service':Service.objects.all()
    }
    
    return render(request, 'services.html',dict_service)


def designers(request):
    stylists = Stylist.objects.all()
    return render(request, 'designers.html', {'stylists': stylists})
    
def apply(request):
    if request.method == 'POST':
        # Process form data here
        # name = request.POST.get('name')
        # phone = request.POST.get('phone')
        # Save the data or perform other actions
        return HttpResponse("Application submitted successfully!")
    return redirect('contact')  # Redirect back to the hiring page if GET request


