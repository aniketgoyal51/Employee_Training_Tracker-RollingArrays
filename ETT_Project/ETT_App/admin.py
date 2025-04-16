from django.contrib import admin

# Register your models here.
from .models import Employee,TrainingProgram,Enrollment

admin.site.register(Employee)
admin.site.register(TrainingProgram)
admin.site.register(Enrollment)