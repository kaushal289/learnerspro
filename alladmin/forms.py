from django import forms 
from alladmin.models import *

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"