from django.shortcuts import render
from django.shortcuts import render

def index(request):
    return render(request , 'classifier/index.html')

def important(request):
    return render(request , 'classifier/important.html')

def officemail(request):
    return render(request , 'classifier/officemail.html')

def advertisment(request):
    return render(request , 'classifier/advertisment.html')

def event(request):
    return render(request , 'classifier/event.html')

def invitation(request):
    return render(request , 'classifier/invitation.html')

def formsfillups(request):
    return render(request , 'classifier/formsfillups.html')
    