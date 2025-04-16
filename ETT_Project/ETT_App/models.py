from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)


class TrainingProgram(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    trainer_name = models.CharField(max_length=100)


class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('enrolled', 'Enrolled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training_program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='enrolled')