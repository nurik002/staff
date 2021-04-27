from django import forms

from main.models import StaffModel


class StaffForms(forms.ModelForm):
    class Meta:
        model = StaffModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'})
        }
