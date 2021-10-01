from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('important/' , views.important , name='important'),
    path('officemail' , views.officemail , name='officemail'),
    path('advertisment' , views.advertisment , name='advertisment'),
    path('event' , views.event , name='event'),
    path('invitation' , views.invitation , name='invitation'),
    path('formsfillups' , views.formsfillups , name='formsfillups'),
]
