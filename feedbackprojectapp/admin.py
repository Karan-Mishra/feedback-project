from django.contrib import admin

# Register your models here.
from .models import StudentRegistration,FacultyDatabase,SubjectDatabase,DepartmentDatabase

admin.site.register(StudentRegistration)
admin.site.register(FacultyDatabase)
admin.site.register(SubjectDatabase)
admin.site.register(DepartmentDatabase)