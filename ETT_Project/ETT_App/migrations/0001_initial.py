# Generated by Django 5.2 on 2025-04-15 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('department', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('trainer_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('enrolled', 'Enrolled'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='enrolled', max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ETT_App.employee')),
                ('training_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ETT_App.trainingprogram')),
            ],
        ),
    ]
