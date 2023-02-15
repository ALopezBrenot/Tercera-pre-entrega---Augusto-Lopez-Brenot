from django import forms

class ProfesionalesFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.EmailField()
    matricula = forms.IntegerField()
    profesion = forms.CharField()

class TesteosFormulario(forms.Form):

    DNI_pac = forms.IntegerField()
    estado = forms.BooleanField()
    resultado = forms.CharField(max_length=20)
    profesional = forms.CharField(max_length=50)
    fecha = forms.DateField()