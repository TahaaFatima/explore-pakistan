from django.contrib import admin

from django.contrib import admin
from .models import Provincess, Destinations ,  bookings, testimonials
# Register your models here.
admin.site.register(Destinations)
admin.site.register(Provincess)
admin.site.register(bookings)
admin.site.register(testimonials)
