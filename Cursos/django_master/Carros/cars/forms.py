from django import forms
from cars.models import Car


#Cria form de forma altomatica
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'