from django.db import models

# Create your models here.
class Operation(models.Model):
    name= models.CharField( max_length=50),
    image=models.ImageField( upload_to='Operations',  max_length=None)
        
    opertionTypeChoice=(
       ( 'FireFighting','firefighting'),
        ('EffectiveRescues','effectiverescues'),
        ('topographyAllocatedAreas','topographyAllocatedAreas'),
    )
    
    operationType=models.CharField( max_length=50, choices=opertionTypeChoice)
    duration=models.CharField( max_length=50),
    

    def __str__(self):
        return self.name

class NationalFireAcademy(models.Model):
    image=models.ImageField( upload_to='Academy', max_length=None)
    name=models.CharField( max_length=50),
    location=models.CharField( max_length=50),
    state=models.CharField( max_length=50),
    Student=models.IntegerField(),


    def __str_(self):
        return self.name


class Staff(models.Model):
    name=models.CharField( max_length=50)
    rank=models.CharField( max_length=50)
    genderChoice=(
        ('male','Male'),
        ('female','Female')
    )
    gender=models.CharField( choices=genderChoice, default='male', max_length=50)
    staffId=models.IntegerField()
    
    def __str__(self):
        return self.name


class Stations(models.Model):
    image=models.ImageField( upload_to='Stations', max_length=None)
    name=models.CharField( max_length=50)
    head_of_station=models.ForeignKey ( Staff,  on_delete=models.CASCADE, blank=True , null=True)
    address=models.CharField( max_length=50)
    state=models.CharField( max_length=50)
    station_description=models.TextField()
    date_created= models.DateField( auto_now=False, auto_now_add=False)
    emergencyNumber=models.CharField( max_length=50)


    def __str__(self):
        return self.name
