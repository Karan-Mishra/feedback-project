from django.shortcuts import render,redirect
from django.views.generic import TemplateView, UpdateView
from django.http import HttpResponseRedirect, request
from django.urls import reverse, reverse_lazy
from .models import StudentRegistration,FacultyDatabase
from .forms import StudentRegistrationForm, FacultyUpdateForm,StudentLoginForm,StudentForgotPasswordForm, StudentUpdateForm,FacultyLoginForm,FacultyForgotPasswordForm
from django.contrib import messages
from django.http.response import HttpResponse
from django.contrib.sessions.models import Session
from django.core import serializers


class IndexView(TemplateView):
    template_name = "index.html"


class StudentIndex(TemplateView):
    template_name = "studentindex.html"

    def get(self, request, *args, **kwargs):

        if not 'login' in self.request.session:
            return HttpResponseRedirect(reverse('StudentLogin'))
        else:
            return self.render_to_response(self.get_context_data(**kwargs))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['id'] = self.request.session['data']
        context['name'] = self.request.session['name']
        context['lastname'] =self.request.session['lastname']
        return context


class StudentLoginView(TemplateView):
    template_name = "studentlogin.html"

    def get(self, request, *args, **kwargs):

        if  'login' in self.request.session:
            return HttpResponseRedirect(reverse('StudentIndex'))
        else:
            return self.render_to_response(self.get_context_data(**kwargs))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loginForm'] = StudentLoginForm(self.request.POST or None)
        return context

    def post(self, request):
        context = self.get_context_data()
        if context['loginForm'].is_valid():
            roll_no = context['loginForm'].cleaned_data['rollno']
            password = context['loginForm'].cleaned_data['password']
            data = StudentRegistration.objects.get(rollno=roll_no)
            if password == data.password:
                self.request.session['login'] = 1 #for students
                self.request.session['data'] = data.pk
                self.request.session['name'] = data.firstname
                self.request.session['lastname'] = data.lastname
                return HttpResponseRedirect(reverse('StudentIndex'))
            else:
                context['loginForm'] = StudentLoginForm()
                context['messages'] = messages.add_message(request, messages.ERROR, 'Incorrect Login id or Password')
                return HttpResponseRedirect(reverse('StudentLogin'))
        else:
            return HttpResponseRedirect(reverse('StudentLogin'))





class StudentRegistrationView(TemplateView):
    template_name = "studentregistration.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["regForm"] = StudentRegistrationForm(self.request.POST or None)
        return context


    def post(self, request):
        context = self.get_context_data()
        if context["regForm"].is_valid():
            print(context["regForm"])
            context['regForm'].save()
            context['regForm'] = StudentRegistrationForm()
        return HttpResponseRedirect(reverse('StudentRegistration'))

class StudentForgotPasswordView(TemplateView):
    template_name = 'studentforgotpassword.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['studentforgotpswdForm'] = StudentForgotPasswordForm(self.request.POST or None)
        return context

    def post(self, request):
        context = self.get_context_data()
        if context['studentforgotpswdForm'].is_valid():
            roll_no = context['studentforgotpswdForm'].cleaned_data['rollno']
            password = context['studentforgotpswdForm'].cleaned_data['password']
            data = StudentRegistration.objects.get(rollno=roll_no)
            if not data:
                context['studentforgotpswdForm'] = StudentForgotPasswordForm()
                return HttpResponse('your password is not updated beacuse you are not user')
            else:
                StudentRegistration.objects.filter(rollno=roll_no).update(password=password,confirmpassword=password)
                context['messages'] = messages.add_message(request, messages.SUCCESS, 'Password updated')
                return HttpResponseRedirect(reverse('StudentLogin'))

        else:
            return HttpResponseRedirect(reverse('StudentLogin'))


class StudentView(TemplateView):
    template_name = 'studentview.html'

    def get(self, request, *args, **kwargs):
        if not 'login' in self.request.session:
            return HttpResponseRedirect(reverse('index'))
        else:
            return self.render_to_response(self.get_context_data(**kwargs))



    def get_context_data(self, **kwargs):
        data = self.request.session['data']
        context = super().get_context_data(**kwargs)
        context["studentviewForm"] = StudentRegistration.objects.filter(pk=data)
        return context



class StudentUpdateView(UpdateView):
    template_name = 'studentupdate.html'
    model = StudentRegistration
    form_class = StudentUpdateForm
    pk_url_kwarg = 'rollno'
    success_url = reverse_lazy('index')


class StudentLogout(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        del self.request.session['login']
        del self.request.session['data']
        del self.request.session['name']
        del self.request.session['lastname']
        return HttpResponseRedirect(reverse('index'))



#faculty code started from here

class FacultyIndexView(TemplateView):
    template_name = 'facultyindex.html'

    def get(self, request, *args, **kwargs):

        if not 'login' in self.request.session:
            return HttpResponseRedirect(reverse('FacultyLogin'))
        else:
            return self.render_to_response(self.get_context_data(**kwargs))

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['id'] = self.request.session['data']
        context['name'] = self.request.session['name']
        context['lastname'] = self.request.session['lastname']
        return context

class FacultyLoginView(TemplateView):
    template_name = 'facultylogin.html'

    def get(self, request, *args, **kwargs):

        if 'login' in self.request.session:
            return HttpResponseRedirect(reverse('FacultyIndex'))
        else:
            return self.render_to_response(self.get_context_data(**kwargs))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['facultyloginForm'] = FacultyLoginForm(self.request.POST or None)
        return context

    def post(self, request):
        context = self.get_context_data()
        if context['facultyloginForm'].is_valid():
            faculty_id= context['facultyloginForm'].cleaned_data['facultyid']
            password = context['facultyloginForm'].cleaned_data['password']
            data = FacultyDatabase.objects.get(facultyid=faculty_id)
            if password == data.password:
                self.request.session['login'] = 2  # for faculty
                self.request.session['data'] = data.pk
                self.request.session['name'] = data.firstname
                self.request.session['lastname'] = data.lastname
                return HttpResponseRedirect(reverse('FacultyIndex'))
            else:
                context['facultyloginForm'] = FacultyLoginForm()
                context['messages'] = messages.add_message(request, messages.ERROR, 'Incorrect Login id or Password')
                return HttpResponseRedirect(reverse('FacultyLogin'))
        else:
            return HttpResponseRedirect(reverse('FacultyLogin'))




class FacultyForgotPasswordView(TemplateView):
    template_name = 'facultyforgotpassword.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['facultyforgotpswdForm'] = FacultyForgotPasswordForm(self.request.POST or None)
        return context

    def post(self, request):
        context = self.get_context_data()
        if context['facultyforgotpswdForm'].is_valid():
            faculty_id = context['facultyforgotpswdForm'].cleaned_data['facultyid']
            password = context['facultyforgotpswdForm'].cleaned_data['password']
            data = FacultyDatabase.objects.get(facultyid=faculty_id)
            if not data:
                context['facultyforgotpswdForm'] = FacultyForgotPasswordForm()
                return HttpResponse('your password is not updated beacuse you are not user')
            else:
                FacultyDatabase.objects.filter(facultyid=faculty_id).update(password=password, confirmpassword=password)
                context['messages'] = messages.add_message(request, messages.SUCCESS, 'Password updated')
                return HttpResponseRedirect(reverse('FacultyLogin'))

        else:
            return HttpResponseRedirect(reverse('FacultyLogin'))


class FacultyView(TemplateView):
    template_name = 'facultyview.html'

    def get(self, request, *args, **kwargs):
        if not 'login' in self.request.session:
            return HttpResponseRedirect(reverse('index'))
        else:
            return self.render_to_response(self.get_context_data(**kwargs))

    def get_context_data(self, **kwargs):
        data = self.request.session['data']
        context = super().get_context_data(**kwargs)
        context["FacultytviewForm"] = FacultyDatabase.objects.filter(pk=data)
        return context


class FacultyUpdateView(UpdateView):
    template_name = 'Facultyupdate.html'
    model = FacultyDatabase
    form_class = FacultyUpdateForm
    pk_url_kwarg = 'facultyid'
    success_url = reverse_lazy('index')

class FacultyLogout(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        del self.request.session['login']
        del self.request.session['data']
        del self.request.session['name']
        del self.request.session['lastname']
        return HttpResponseRedirect(reverse('index'))