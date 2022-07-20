from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.



class Courses(models.Model):
    Course_name=models.CharField(max_length=30,null=False)
    slug = models.CharField(max_length=30, null=False,unique=True)
    description=models.CharField(max_length=200,null=True)
    instructor_name=models.CharField(max_length=30,null=False)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    instructor_image=models.ImageField(upload_to='Files/pics',null=True)
    thumbnail=models.ImageField(upload_to='Files/pics',null=True)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.Course_name

class Tutorialmodel(models.Model):
    Tutorial_name = models.CharField(max_length=30, null=False)
    Tutorial=models.FileField(upload_to='Files/tutorials',null=True)
    Tutorial_video=models.URLField(max_length=200,unique=True)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.Tutorial_name


class QuesModel(models.Model):
    Quiz_name=models.CharField(max_length=30,null=False)
    question = models.CharField(max_length=200, null=True)
    option1 = models.CharField(max_length=200, null=True)
    option2 = models.CharField(max_length=200, null=True)
    option3 = models.CharField(max_length=200, null=True)
    option4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    tutorial=models.ForeignKey(Tutorialmodel,on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.Quiz_name

