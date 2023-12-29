from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
import os
import pandas as pd
from buscador.utils import procesar_consulta 
from buscador.utils import generar_recomendacion

ruta_csv = os.path.join(settings.BASE_DIR, 'buscador', 'data', 'librosTopicEmbeddings.csv')
libros_df = pd.read_csv(ruta_csv)



def hello(request):
    return HttpResponse("Hello World!")

def index(request):
    return render(request, 'buscador/index.html')

def buscar(request):
    consulta = request.GET.get('consulta', '')
    genero = request.GET.get('genero', '')
    resultado = procesar_consulta(consulta, genero, libros_df)
    return JsonResponse(resultado, safe=False)

def libro_detalle(request, isbn):
    libro = libros_df[libros_df['ISBN'] == int(isbn)].iloc[0].to_dict()
    
    print(libro)
    recomendaciones = generar_recomendacion(libro, libros_df)
    libro = {k.replace(' ', '_'): v for k, v in libro.items()}
    
    
    
    return render(request, 'buscador/libro_detalle.html', {
        'libro': libro,
        'recomendaciones': recomendaciones})
    