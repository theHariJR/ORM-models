from django.db import models

# Create your models here.

class Country(models.Model):
    capno=models.IntegerField(primary_key=True)
    coname=models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.coname + " " + str(self.capno)

class Capital(models.Model):
    capno=models.OneToOneField(Country,on_delete=models.CASCADE)
    capname=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.capname