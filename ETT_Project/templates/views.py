from django.shortcuts import render,redirect
from .models import Enrollment,Employee,TrainingProgram


# Create your views here.
def index(request):
    return render(request,'index.html')


def get_Employees(request):
    employees=Employee.objects.all()
    return render(request,'employees.html',{'employees':employees})

def add_Employee(request):
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        department=request.POST['department']
        designation=request.POST['designation']

        employee=Employee.objects.create(name=name,email=email,department=department,designation=designation)
        employee.save()
        
        return redirect('employees')
    else:
        return render(request,'add_employee.html')

def get_Training(request):
    trainees=TrainingProgram.objects.all()
    return render(request,'training.html',{'trainees':trainees})

def add_Training(request):
    if(request.method=='POST'):
        title=request.POST['title']
        description=request.POST['description']
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        trainer_name=request.POST['trainer_name']

        training=TrainingProgram.objects.create(title=title,description=description,start_date=start_date,end_date=end_date,trainer_name=trainer_name)
        training.save()
        
        return redirect('training')
    else:
        return render(request,'add_training.html')