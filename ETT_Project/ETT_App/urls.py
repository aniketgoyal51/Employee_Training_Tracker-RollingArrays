from django.urls import path
from . import views

urlpatterns=[
    path('',views.dashboard,name='dashboard'),
    path('employees', views.get_Employees,name='employees'),
    path('add_employee',views.add_Employee,name='add_employee'),
    path('training', views.get_Training,name='training'),
    path('add_training',views.add_Training,name='add_training'),
    path('enrollment', views.get_Enrollment,name='enrollment'),
    path('add_enrollment',views.add_Enrollment,name='add_enrollment'),
]