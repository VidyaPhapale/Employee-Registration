from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=100)
    Email_id=models.CharField(max_length=100)
    Contact_No=models.CharField(max_length=100)
    Location=models.TextField(max_length=100,null=True)
    Image=models.ImageField(null=True) 
    
    
    
    
    
    def __str__(self):
        return self.name
        
     



