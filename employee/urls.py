from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('add_employee',add_employee,name='add_employee'),
    path('delete_employee/<int:myid>/',delete_employee,name='delete_employee'),
    path('edit_employee/<int:myid>/',edit_employee,name='edit_employee'),
    path('update_employee/<int:myid>/',update_employee,name='update_employee'),

]