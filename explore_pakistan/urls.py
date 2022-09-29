from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name= 'home' ),
    path('about/', views.about_us, name= 'about' ),
    path('contact/', views.contact_us, name= 'contact' ),
    path('faqs/', views.faqs, name= 'faqs' ),
    path('testimonial/', views.testimonals, name= 'testimonals' ),
    path('form/<int:form_id>', views.form, name= 'form' ),
    path('thanks/', views.thanks, name= 'thanks' ),
    path('details/<int:detail_id>', views.details, name='details'),
    path('booking/', views.booking, name='booking'),
    path('savetestimonial/', views.savetestimonial, name='savetestimonial'),

]