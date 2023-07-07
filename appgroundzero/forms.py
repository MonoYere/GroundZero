from django import forms
from .models import Producto



class DatePickerWidget(forms.DateInput):
    input_type = 'date'
    input_formats = ['%d-%m-%Y']  # Formato "día-mes-año"


    


class ProductoForm(forms.ModelForm):
    fch_creacion = forms.DateField(widget=DatePickerWidget)
    class Meta:
        model = Producto
        fields = '__all__'


