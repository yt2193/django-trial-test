from django import forms
from .models import Company

class myForm(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    address = forms.CharField(max_length=50)

# modelForm api
class modelForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"


