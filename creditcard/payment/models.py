from django.db import models

# Create your models here.
class CDetails(models.Model):
	cardno = models.CharField(max_length=20)
	holdername = models.CharField(max_length=20)
	validthru = models.CharField(max_length=20)
	cvv = models.CharField(max_length=20)
