from email import message
from django.db import models
from django.urls import reverse 
# Create your models here.

class Provincess(models.Model):
    # province_id = models.IntegerField(null=True)
    province_name = models.CharField(max_length=200)
    province_image = models.ImageField( null=True, upload_to= "database_images/")
    province_description= models.TextField()

    def __str__ (self):
        return self.province_name

class Destinations(models.Model):
    province_id = models.ForeignKey(Provincess, on_delete=models.CASCADE, null=True)
    destination_name  = models.CharField(max_length=200)
    destination_image = models.ImageField(null=True, upload_to= "database_images/")
    destination_description  = models.TextField()
    
   
    def __str__ (self):
        return self.destination_name 


class bookings(models.Model):
    full_name = models.CharField(max_length=200)
    phone_num = models.IntegerField()
    email_address = models.EmailField()
    departure_date = models.DateField(max_length=200)
    arrival_date = models.DateField(max_length=200)
    destination_booking = models.CharField(max_length=500,null=True)
    destination= models.ForeignKey(Destinations, on_delete=models.CASCADE,null=True)

    def __str__ (self):
        return self.full_name



class testimonials(models.Model):
    name = models.CharField(max_length=200)
    testimmonial = models.TextField(null=True)

    def __str__ (self):
        return self.name
