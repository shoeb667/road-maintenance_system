from django.db import models

# Create your models here.
class council_member(models.Model):
	muser_id = models.CharField(max_length=25)
	department = models.CharField(max_length=30)
	password = models.CharField(max_length=40)
class issues(models.Model):
	issue_depart = models.CharField(max_length=40)
	issue_title = models.CharField(max_length=50)
	issue_disc = models.TextField(max_length=300)
	issue_status = models.CharField(max_length=20)
	issue_remark = models.CharField(max_length=25)
	issue_by = models.CharField(max_length=25)
class contactus(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    messages = models.TextField(max_length=400)
    