from django.contrib import admin
from .models import User,ServiceProvider,Service,Comment,Booking

# Register your models here.
admin.site.register(User)
admin.site.register(ServiceProvider)
admin.site.register(Service)
admin.site.register(Comment)
admin.site.register(Booking)
