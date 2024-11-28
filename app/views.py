from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from app.models import *

def insert_country(request):
    cono=int(input("Enter the Country number: "))
    cona=input("Enter the Country name: ")
    CONO=Country.objects.get_or_create(capno=cono)
    CONA=Country.objects.get_or_create(cona)
    if CONA[1]:
        return HttpResponse("Country is newely created")
    else:
        return HttpResponse("Country already exists")
    
def insert_capital(request):
    cpno=int(input("Enter the Capital number: "))
    cpna=input("Enter the Capital name: ")
    CPNO=Capital.objects.get_or_create(capno=cpno)
    CPNA=Capital.objects.get_or_create(capname=cpna)
    if CPNA[1]:
        return HttpResponse("Capital is newely created")
    else:
        return HttpResponse("Capital already exists")