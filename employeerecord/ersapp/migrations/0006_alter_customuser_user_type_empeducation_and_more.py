# Generated by Django 5.0.4 on 2024-05-08 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ersapp', '0005_employees_address_employees_empcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'employee')], default=1, max_length=50),
        ),
        migrations.CreateModel(
            name='empeducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CoursePG', models.CharField(default='0', max_length=200)),
                ('SchoolCollegePG', models.CharField(default='0', max_length=200)),
                ('YearPassingPG', models.CharField(default='0', max_length=200)),
                ('PercentagePG', models.CharField(default='0', max_length=200)),
                ('CourseGra', models.CharField(default='0', max_length=200)),
                ('SchoolCollegeGra', models.CharField(default='0', max_length=200)),
                ('YearPassingGra', models.CharField(default='0', max_length=200)),
                ('PercentageGra', models.CharField(default='0', max_length=200)),
                ('CourseSSC', models.CharField(default='0', max_length=200)),
                ('SchoolCollegeSSC', models.CharField(default='0', max_length=200)),
                ('YearPassingSSC', models.CharField(default='0', max_length=200)),
                ('PercentageSSC', models.CharField(default='0', max_length=200)),
                ('CourseHSC', models.CharField(default='0', max_length=200)),
                ('SchoolCollegeHSC', models.CharField(default='0', max_length=200)),
                ('YearPassingHSC', models.CharField(default='0', max_length=200)),
                ('PercentageHSC', models.CharField(default='0', max_length=200)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('empid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ersapp.employees')),
            ],
        ),
        migrations.CreateModel(
            name='empexperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employer1Name', models.CharField(default='0', max_length=200)),
                ('Employer1Designation', models.CharField(default='0', max_length=200)),
                ('Employer1CTC', models.CharField(default='0', max_length=200)),
                ('Employer1WorkDuration', models.CharField(default='0', max_length=200)),
                ('Employer2Name', models.CharField(default='0', max_length=200)),
                ('Employer2Designation', models.CharField(default='0', max_length=200)),
                ('Employer2CTC', models.CharField(default='0', max_length=200)),
                ('Employer2WorkDuration', models.CharField(default='0', max_length=200)),
                ('Employer3Name', models.CharField(default='0', max_length=200)),
                ('Employer3Designation', models.CharField(default='0', max_length=200)),
                ('Employer3CTC', models.CharField(default='0', max_length=200)),
                ('Employer3WorkDuration', models.CharField(default='0', max_length=200)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('empid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ersapp.employees')),
            ],
        ),
    ]
