from django.conf.urls import url
from aplicacion.views import AboutView
from biblioteca.views import ListaEditores, DetallesEditor, ListaLibrosEditores, VistaDetallesAutor


urlpatterns = [
    url(r'^acerca/', VistaAcercaDe.as_view()),
    url(r'^editores/$', ListaEditores.as_view(), name="lista-editores"),
    url(r'^detalles/editor/(?P<pk>[0­9]+)/$', DetallesEditor.as_view(), name='detalles-­editor' ),
    url(r'^libros/([\w­]+)/$', ListaLibrosEditores.as_view(), name='lista­-libros-­editor' ),
    url(r'^autores/(?P<pk>[0­9]+)/$', VistaDetallesAutor.as_view(), name='detalles-­autor'),
]
