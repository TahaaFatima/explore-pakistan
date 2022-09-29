from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Destinations,Provincess,testimonials,bookings
from django.core.mail import send_mail
def home(request):
    province_data=Provincess.objects.all()
    context={
        'province_data_info':province_data,
    }
    
    return render(request, 'home.html',context)

    
def about_us(request):

    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact.html')

def faqs(request):

    return render(request, 'faqs.html')

def thanks(request):

    return render(request, 'thanks.html')


def testimonals(request):
    feedback=testimonials.objects.all()
    data={
        'feedback':feedback

    }
    return render(request, 'home.html',data)



def details(request,detail_id):
    detail_data = Destinations.objects.filter(province_id=detail_id)
    context = {
       'detail_data' :  detail_data
    }
    return render(request, 'destinations.html',context)

def form(request,form_id):
    form_data =get_object_or_404(Destinations,id=form_id)
    context = {
       'form_data' :  form_data
    }
    return render(request, 'form.html',context)


def savetestimonial(request):
    if request.method=="POST":
        name=request.POST.get('name')
        testimmonial=request.POST.get('testimmonial')
        testimostore=testimonials(name=name,testimmonial=testimmonial)
        testimostore.save()
    return render(request, 'thanks.html')

def booking(request):

    if request.method=="POST":
        destination=request.POST.get('dest')
        name=request.POST.get('name')
        Phone=request.POST.get('phone')
        email=request.POST.get('email')
        Departure=request.POST.get('checkin')
        arrival=request.POST.get('checkout')
        store=bookings(destination_booking= destination,full_name=name,phone_num=Phone,email_address=email,departure_date=Departure,arrival_date=arrival)
        store.save()
    send_mail(
    'Booking For:'+destination, #subject
    'Name:  '+ name+'                 departure_date:  '+ Departure + '                    arrival date:  '+ arrival, #msg
    email,   #from email
    ['explorepakistan1234@gmail.com'], #to email
)  
    return render(request, 'submit.html',)
