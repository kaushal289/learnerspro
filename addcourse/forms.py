from django import forms 
from addcourse.models import *

class Courseform(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

