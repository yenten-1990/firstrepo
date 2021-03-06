# Generated by Django 4.0 on 2021-12-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=20)),
                ('empdesignation', models.CharField(max_length=25)),
                ('empdepartment', models.CharField(max_length=50)),
                ('empage', models.IntegerField()),
                ('empbloodgroup', models.CharField(max_length=50)),
                ('empemailid', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'EmployeeDetails',
                'verbose_name_plural': 'EmployeeDetails',
            },
        ),
    ]
