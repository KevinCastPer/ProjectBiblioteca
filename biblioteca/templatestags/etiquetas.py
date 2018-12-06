import datetime
import re
from django import template

register = template.Library()

class NodoFechaActual3(template.Node):
    def __init__(self, formato_cadena, var_nombre):
        self.formato_cadena = str(formato_cadena)
        self.var_nombre = var_nombre

    def render(self, context):
        ahora = datetime.datetime.now()
        context[self.var_nombre] = ahora.strftime(self.formato_cadena)
        return ''

@register.tag(name="traer_fecha_actual")
def traer_fecha_actual(parser, token):
    # Esta versión usa expresiones regulares para analizar el contenido de la etiqueta.
    try:
        # Dividir por None == dividir por espacios.
        tag_nombre, arg = token.contents.split(None, 1)
    except ValueError:
        msg = '%r La etiqueta requiere un simple argumento'% token.contents[0]
        raise template.TemplateSyntaxError(msg)

    m = re.search(r'(.*?) as (\w+)', arg)
    if m:
        fmt, var_nombre = m.groups()
    else:
        msg = '%r Argumentos no validos para la etiqueta' % tag_nombre
        raise template.TemplateSyntaxError(msg)
    if not (fmt[0] == fmt[­1] and fmt[0] in (""", """)):
        msg = '%r Los argumentos deben de ir entre comillas' % tag_nombre
        raise template.TemplateSyntaxError(msg)
    return NodoFechaActual3(fmt[1:­1], var_nombre)
