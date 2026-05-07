from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from .models import Comentario

# 1. XSS View: Mostramos contenido sin filtrar
def prueba_xss(request):
    if request.method == 'POST':
        Comentario.objects.create(
            carta_nombre="Carta XSS",
            contenido=request.POST.get('contenido')
        )
    comentarios = Comentario.objects.all()
    return render(request, 'core/xss.html', {'comentarios': comentarios})

# 2. CSRF View: Desactivamos la protección de token
# Eliminamos @csrf_exempt para que Django exija el token en cada POST
#@csrf_exempt
def prueba_csrf(request):
    if request.method == 'POST':
        # Simulación de una acción sensible, como borrar comentarios
        Comentario.objects.all().delete()
        return redirect('prueba_csrf')
    return render(request, 'core/csrf.html')

# 3. Clickjacking View: Permitimos que la página se meta en IFRAMEs
def prueba_clickjacking(request):
    response = render(request, 'core/clickjacking.html')
    # Eliminamos la protección habitual de Django para esta respuesta
    del response['X-Frame-Options']
    return response

def home(request):
    return render(request, 'core/home.html')