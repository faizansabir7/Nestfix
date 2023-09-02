from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    certificate = models.FileField(upload_to='media/certificates', blank=True, null=True)
    phno=models.TextField(blank=True)
    def is_service_provider(self):
        return hasattr(self, 'sp')


class Service(models.Model):
    name=models.CharField(max_length=64)
    icon=models.TextField(blank=True,null=True)
    desc=models.TextField(blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return f"{self.name}"
    

class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='sp')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    district=models.TextField()
    city=models.TextField()
    def __str__(self):
        return f"{self.service.name} {self.user.username}"

class Comment(models.Model):
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)  
    sp=  models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    rate=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} about {self.sp}:  {self.comment}"
    
class Booking(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)  
    sp=  models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    viewed_at = models.DateTimeField(blank=True, null=True)
    district=models.TextField()
    city=models.TextField()
    complete=models.BooleanField(default=False)
    

    def cancel(self):
        self.delete()
    def __str__(self):
        self.formatted_dt = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
        return f"{self.user.username} booked for {self.sp} on {self.formatted_dt} "    
   
    

