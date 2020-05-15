"""feedbackproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from feedbackprojectapp.views import IndexView, FacultyUpdateView, StudentUpdateView ,StudentLoginView,StudentRegistrationView,StudentIndex,StudentForgotPasswordView,StudentView,\
    FacultyLoginView,FacultyIndexView,FacultyForgotPasswordView,FacultyView,StudentLogout, FacultyLogout, FeedbackView ,Feedback,FacultyfeedbackView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view(),name='index'),
    path('StudentLogin/',StudentLoginView.as_view(),name='StudentLogin'),
    path('StudentRegistration/',StudentRegistrationView.as_view(),name='StudentRegistration'),
    path('StudentIndex/',StudentIndex.as_view(),name='StudentIndex'),
    path('StudentUpdate/<int:rollno>', StudentUpdateView.as_view(), name='StudentUpdate'),
    path('StudentForgotPassword/',StudentForgotPasswordView.as_view(),name='StudentForgotPassword'),
    path('StudentView/',StudentView.as_view(),name='StudentView'),
    path('FacultyLogin/',FacultyLoginView.as_view(),name='FacultyLogin'),
    path('FacultyIndex/',FacultyIndexView.as_view(),name='FacultyIndex'),
    path('FacultyForgotPassword/',FacultyForgotPasswordView.as_view(),name='FacultyForgotPassword'),
    path('FacultyView/',FacultyView.as_view(),name='FacultyView'),
    path('faculty-update/<int:facultyid>', FacultyUpdateView.as_view(), name='faculty-update'),
    path('student-logout/',StudentLogout.as_view(),name='student-logout'),
    path('faculty-logout/',FacultyLogout.as_view(),name='faculty-logout'),
    path('feedbackform/<int:id>', FeedbackView.as_view(), name='feedbackform'),
    path('test/',Feedback.as_view(),name='test' ),
    path('facultyfeedbackview/',FacultyfeedbackView.as_view(),name='facultyfeedbackview')

]
