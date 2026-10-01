from django.db import models

# Create your models here.
class tblcontact(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    mobile=models.CharField(max_length=15,null=True)
    message=models.TextField(null=True)

class tblgallery(models.Model):
    title=models.CharField(max_length=50,null=True)    
    picture=models.ImageField(upload_to="static/picture/",null=True)    


class tblplacements(models.Model):
    name=models.CharField(max_length=50,null=True)
    picture=models.ImageField(upload_to="static/placement/")
    psession=models.CharField(max_length=50,null=True)
    company=models.CharField(max_length=50,null=True)
    designation=models.CharField(max_length=50,null=True)

class tblbranch(models.Model):
    name=models.CharField(max_length=100,null=True)
    no_of_seats=models.CharField(max_length=25,null=True)
    picture=models.ImageField(upload_to="static/branch/")

class tblteam(models.Model):
    name=models.CharField(max_length=50,null=True)
    designation=models.CharField(max_length=40,null=True)
    picture=models.ImageField(upload_to="static/team/")


class tblfacilities(models.Model):
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    picture=models.ImageField(upload_to="static/facilities/",null=True) 

class new(models.Model):
    title=models.TextField(null=True)
    posted_date=models.DateField(null=True)       