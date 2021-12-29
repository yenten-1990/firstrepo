from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
	empid=models.IntegerField(primary_key=True)
	empname=models.CharField(max_length=20)
	empdesignation=models.CharField(max_length=25)
	empdepartment=models.CharField(max_length=50)
	empage=models.IntegerField()
	empbloodgroup=models.CharField(max_length=50)
	empemailid=models.CharField(unique=True,max_length=50)
	class Meta:
		verbose_name="EmployeeDetails"
		verbose_name_plural="EmployeeDetails"

	def __str__(self):
		return self.empname + " "+ str(self.empid)+ " " + self.empdesignation + " " + self.empdepartment + " " + str(self.empage) + " " + self.empbloodgroup
