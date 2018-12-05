# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

class FormularioContactos(forms.Form):
    asunto = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Tu correo electronico')
    mensaje = forms.CharField(widget=forms.Textarea)

    """
    El sistema de formularios de Django, automáticamente busca cualquier método
    que empiece con clean_ y termine con el nombre del campo. Si cualquiera de estos
    métodos existe, este será llamado durante la validación.
    """
    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        num_palabras = len(mensaje.split())
        if num_palabras < 4:
            raise forms.ValidationError("¡Se requieren mínimo 4 palabras!")
        return mensaje
