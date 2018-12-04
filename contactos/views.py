# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def contactos(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('asunto'):
            errors.append('Por favor introduce el asunto.')
        if not request.POST.get('mensaje'):
            errors.append('Por favor introduce un mensaje.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Por favor introduce una direccion de e-mail valida.')
        if not errors:
            send_mail(
                request.POST['asunto'],
                request.POST['mensaje'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'], )

            return HttpResponseRedirect('/contactos/gracias/')
    return render(request, 'formulario_contactos.html', {'errors': errors,
        'asunto': request.POST.get('asunto'),
        'mensaje': request.POST.get('mensaje'),
        'email': request.POST.get('email'),
    })