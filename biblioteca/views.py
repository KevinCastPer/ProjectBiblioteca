# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from biblioteca.models import Libro, Editor, Autor
from django.views.generic import TemplateView, ListView, DetailView
from django.utils import timezone

def formulario_buscar(request):
    return render(request, 'formulario_buscar.html')

def buscar(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Por favor introduce un término de búsqueda.')
        elif len(q) > 20:
            errors.append('Por favor introduce un término de búsqueda menor a 20 caracteres.')
        else:
            libros = Libro.objects.filter(titulo__icontains=q)
            return render(request, 'resultados.html', {'libros': libros, 'query': q})

    return render(request, 'formulario_buscar.html', {'errors': errors})


class VistaAcercaDe(TemplateView):
    template_name = 'acerca_de.html'

class ListaEditores(ListView):
    model = Editor
    context_object_name = 'lista_editores'

class DetallesEditor(DetailView):
    model = Editor
    context_object_name = 'editor'
    queryset = Editor.objects.all()

    def get_context_data(self, **kwargs):
        # Llama primero a la implementación para traer un contexto
        context = super(DetallesEditor, self).get_context_data(**kwargs)
        # Agrega un QuerySet para obtener todos los libros
        context['lista_libros'] = Libro.objects.all()
        return context

# class LibrosRecientes(ListView):
#     queryset = Libro.objects.order_by('­-fecha_publicacion')
#     context_object_name = 'libros_recientes'

class LibroAcme(ListView):
    context_object_name = 'lista_libros_acme'
    queryset = Libro.objects.filter(editor__nombre='Editores Acme')
    template_name = 'biblioteca/lista_libros_acme.html'

class ListaLibrosEditores(ListView):
    template_name = 'biblioteca/lista_libros_por_editores.html'

    def get_queryset(self):
        self.editor = get_object_or_404(Editor, nombre=self.args[0])
        return Libro.objects.filter(editor=self.editor)

    def get_context_data(self, **kwargs):
        # Llama primero a la implementación para traer el contexto
        context = super(ListaLibrosEditores, self).get_context_data(**kwargs)
        # Se agrega el editor
        context['editor'] = self.editor
        return context

class VistaDetallesAutor(DetailView):
    queryset = Autor.objects.all()

    def get_object(self):
        # LLama a la superclase
        objeto = super(VistaDetallesAutor, self).get_object()
        # Graba la fecha de el último acceso
        objeto.ultimo_acceso = timezone.now()
        objeto.save()
        # Retorna el objeto
        return objeto
