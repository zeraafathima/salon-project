from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('designers/', views.designers, name='designers'),
    path('hiring/', views.hiring, name='hiring'),
    path('event/', views.event, name='event'),
    path('booking/', views.booking, name='booking'),
    path('services/', views.services, name='services'),
     path('apply/', views.apply, name='apply'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)