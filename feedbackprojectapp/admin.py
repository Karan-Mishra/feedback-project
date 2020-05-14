from django.contrib import admin

# Register your models here.
from .models import StudentRegistration,FacultyDatabase,SubjectDatabase,DepartmentDatabase, Question, FeedbackForm, FeedbackAnswers

admin.site.register(StudentRegistration)
admin.site.register(FacultyDatabase)
admin.site.register(SubjectDatabase)
admin.site.register(DepartmentDatabase)
admin.site.register(Question)
admin.site.register(FeedbackForm)
admin.site.register(FeedbackAnswers)