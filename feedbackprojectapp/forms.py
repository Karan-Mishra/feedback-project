from django import forms
from .models import StudentRegistration,FacultyDatabase, FeedbackAnswers, Question


"""
    question_choices = (
        (1,'Strongly Agree'),
        (2,'SECONDYEAR'),
        (3,'THIRDYEAR'),
        (4,'FORTHYEAR'),
    )
    options = models.IntegerField(choices=question_choices)
"""

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = '__all__'
        widgets = {
            'rollno':forms.NumberInput(attrs={'class':'form-control','placeholder':'Rollno'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Last Name'}),
            'year':forms.Select(attrs={'class':'form-control','placeholder':'Year'}),
            'department': forms.Select(attrs={'class': 'form-control ', 'placeholder': 'Department'}),
            'password': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Password'}),
            'confirmpassword': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Confirm Password'}),
            'mobile': forms.NumberInput(
                attrs={
                'class': 'form-control ',
                'placeholder': 'Mobile Number',
                'validators': 'User is already registered'
            }),
            'gender': forms.Select(attrs={'class': 'form-control ', 'placeholder': 'Select your gender'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control ',
                    'placeholder': 'Email Id',
                    'validators': 'User is already registered' }),
            'admission_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Admission_year'}),

        }
class StudentLoginForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ('rollno', 'password')
        widgets = {
            'rollno': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rollno'}),
            'password': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Password'}),
        }


class StudentForgotPasswordForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ('rollno', 'password')
        widgets = {
            'rollno': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rollno'}),
            'password': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Update Password'}),
        }


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        exclude = ('rollno',)
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Last Name'}),
            'year':forms.Select(attrs={'class':'form-control','placeholder':'Year'}),
            'department': forms.Select(attrs={'class': 'form-control ', 'placeholder': 'Department'}),
            'password': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Password'}),
            'confirmpassword': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Confirm Password'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Mobile Number'}),
            'gender': forms.Select(attrs={'class': 'form-control ', 'placeholder': 'Select your gender'}),
            'email': forms.EmailInput(attrs={'class': 'form-control ', 'placeholder': 'Email Id'}),
        }


class FacultyLoginForm(forms.ModelForm):
    class Meta:
        model = FacultyDatabase
        fields = ('facultyid', 'password')
        widgets = {
            'facultyid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rollno'}),
            'password': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Password'}),
        }


class FacultyForgotPasswordForm(forms.ModelForm):
    class Meta:
        model = FacultyDatabase
        fields = ('facultyid', 'password')
        widgets = {
            'facultyid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Faculty Id'}),
            'password': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Update Password'}),
        }


class FacultyUpdateForm(forms.ModelForm):
    class Meta:
        model = FacultyDatabase
        exclude = ('facultyid',)
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Last Name'}),
            'password': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Password'}),
            'confirmpassword': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Confirm Password'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Mobile Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control ', 'placeholder': 'Email Id'}),
            'department': forms.Select(attrs={'class': 'form-control ', 'placeholder': 'Department'}),
            'subject': forms.Select(attrs={'class': 'form-control ', 'placeholder': 'Subject'}),
            'gender': forms.Select(attrs={'class': 'form-control ', 'placeholder': 'Select your gender'}),
             'year': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Year'}),
        }


class FeedbackAnswerForm(forms.Form):

    question_choices = (
        (1,'Strongly Agree'),
        (2,'Disagree'),
        (3,'Agree'),
        (4,'Neutral'),
    )
    questions = Question.objects.all()
    for question in questions:
        locals()[str(question.id)] = forms.ChoiceField(
            widget=forms.Select(), 
            choices=question_choices,
            label = question.questions
            )


