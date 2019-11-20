from django.shortcuts import render
from django.http import HttpResponse
from payment.models import CDetails

# Create your views here.
def home(request):
	return render(request,'home.html')
def addpay(request):
	return render(request,'addpay.html')
def onaddpay(request):
	c=CDetails(request.POST['cardno'],request.POST['cardno'],request.POST['cardholdername'],request.POST['validthru'],request.POST['cvv'])
	c.save()
	return render(request,'success.html',{'msg':'Payment SUCCESSFULLY completed with the addded card'})
def existpay(request):
	c=CDetails.objects.all()
	return render(request,'existpay.html',{'cards':c})
def final(request):
	return render(request,'success.html',{'msg':'Payment SUCCESSFULLY completed with the selected card'})
