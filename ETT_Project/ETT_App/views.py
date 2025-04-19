from django.shortcuts import render,redirect
from .models import Enrollment,Employee,TrainingProgram


# Create your views here.
def dashboard(request):
    total_employee=Employee.objects.all().count()
    total_training=TrainingProgram.objects.all().count()
    total_enrollment=Enrollment.objects.all().count()
    total_enrolled=Enrollment.objects.filter(status='enrolled').count()
    total_in_progress=Enrollment.objects.filter(status='in_progress').count()
    total_completed=Enrollment.objects.filter(status='completed').count()

    display={
        "total_employee":total_employee,
        "total_training":total_training,
        "total_enrollment":total_enrollment,
        "total_enrolled":total_enrolled,
        "total_in_progress":total_in_progress,
        "total_completed":total_completed,
    }

    return render(request,"dashboard.html",{"display":display})


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


def get_Enrollment(request):
    trainees=TrainingProgram.objects.all()
    employees=Employee.objects.all()
    if(request.method=="POST"):
        choice=request.POST['status']
        if choice == "all":
            enrollment = Enrollment.objects.all()
        else:
            enrollment = Enrollment.objects.filter(status=choice)
    else:
        enrollment=Enrollment.objects.all()
    return render(request,'enrollment.html',{'trainees':trainees,'employees':employees,'enrollments':enrollment})

def add_Enrollment(request):

    if(request.method=='POST'):
        employee_id=request.POST['employee']
        program_id=request.POST['training_program']
        status=request.POST['status']

        employee = Employee.objects.get(id=employee_id)
        program = TrainingProgram.objects.get(id=program_id)

        enrollment=Enrollment.objects.create(employee=employee,training_program=program,status=status)
        enrollment.save()
        
        return redirect('enrollment')
    else:
        trainees=TrainingProgram.objects.all()
        employees=Employee.objects.all()
        status=Enrollment.STATUS_CHOICES
        
        return render(request,'add_enrollment.html',{'trainees':trainees,'employees':employees,'status_choices': status})
