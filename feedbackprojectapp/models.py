from django.db import models


class SubjectDatabase(models.Model):
    subject_name = models.CharField(max_length=30)
    subject_code = models.CharField(max_length=10)

    class Meta:
        db_table = 'subject'

    def __str__(self):
        return self.subject_name


class DepartmentDatabase(models.Model):
    department_name = models.CharField(max_length=30)
    department_head = models.CharField(max_length=30)

    class Meta:
        db_table ='department'

    def __str__(self):
        return self.department_name


class StudentRegistration(models.Model):
    rollno = models.IntegerField(null=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField( max_length=30)
    YEAR_CHOICES = (
        ('1', 'FIRSTYEAR'),
        ('2', 'SECONDYEAR'),
        ('3', 'THIRDYEAR'),
        ('4', 'FORTHYEAR'),
    )
    year = models.CharField(max_length=1, choices=YEAR_CHOICES, null=True)
    department = models.ForeignKey(DepartmentDatabase, on_delete=models.CASCADE, null=True)
    password = models.CharField(max_length=30, null=True)
    confirmpassword = models.CharField(max_length=30, null=True)
    mobile = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)

    class Meta:
        db_table = 'students'
        ordering =['rollno']

    def __str__(self):
        return str(self.rollno)


class FacultyDatabase(models.Model):
    facultyid=models.IntegerField(null=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    password = models.CharField(max_length=30,null=True)
    confirmpassword = models.CharField(max_length=30,null=True)
    mobile = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(DepartmentDatabase, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(SubjectDatabase, on_delete=models.CASCADE, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    YEAR_CHOICES = (
        ('1','FIRSTYEAR'),
        ('2','SECONDYEAR'),
        ('3','THIRDYEAR'),
        ('4','FORTHYEAR'),
    )
    year = models.CharField(max_length=1,choices=YEAR_CHOICES,null=True)


class Questions(models.Model):
    question_choices = (
        (1,'Strongly Agree'),
        (2,'SECONDYEAR'),
        (3,'THIRDYEAR'),
        (4,'FORTHYEAR'),
    )
    options = models.IntegerField(choices=question_choices)
    questions = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'question'
        ordering = ['updated_at']

    def __str__(self):
        return self.questions[:50]


class Feedback(models.Model):
    faculty = models.ForeignKey(FacultyDatabase, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Questions)
    student = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'feedback'
        ordering = ['updated_at']

    def __str__(self):
        return self.faculty


class Answers(models.Model):
    form_id = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    answers = models.CharField(max_length=300)
    student = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'answer'
        ordering = ['updated_at']

    def __str__(self):
        return self.form_id

