from django.contrib import admin
from adminapp.models import EmployeeDetails
#Register your models here.
class EmployeeDetailsAdmin(admin.ModelAdmin):
	'''
		Admin View fir EmployeeDetails
	'''

	list_display=('empid','empname','empdesignation','empdepartment',
		'empage','empbloodgroup','empemailid')
admin.site.register(EmployeeDetails,EmployeeDetailsAdmin)
#admin.site.register(Model Class Name,Admin Class Name)