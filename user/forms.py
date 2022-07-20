from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

class uploadtutorialform(forms.ModelForm):
    class Meta:
        model = Tutorialmodel
        fields = ['Tutorial_name','Tutorial','Tutorial_video','course']


class addQuizform(ModelForm):
    class Meta:
        model = QuesModel
        fields = ['Quiz_name','question','option1','option2','option3','option4','ans','course','tutorial']







