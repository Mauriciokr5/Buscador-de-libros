# Buscador de Libros

## Descripción del Proyecto

Este proyecto consiste en un buscador de libros avanzado que utiliza similitud coseno con embeddings y un sistema de recomendación/relacionados implementado mediante topic modeling (LDA). El buscador genera una página web desarrollada con Django, proporcionando una interfaz interactiva y amigable para los usuarios.

## Características Principales

- **Búsqueda de Libros:** Utiliza embeddings para encontrar libros similares basados en su contenido.
- **Sistema de Recomendación:** Implementa LDA para sugerir libros relacionados.
- **Interfaz Web:** Desarrollada con Django, ofrece una experiencia de usuario intuitiva.

## Requerimientos

- Los detalles específicos de las versiones utilizadas en el desarrollo están en `environment.yml`.

## Instalación y Uso

### Uso de Docker

Para facilitar el despliegue y uso del proyecto, se incluye un Dockerfile. Siga estos pasos para construir y ejecutar el contenedor:

1. Construir la imagen del contenedor:
```
 docker build -t buscador_libros .
```
2. Ejecutar el contenedor:
```
 docker run -it -p 8000:8000 buscador_libros
```

Esto creará un servidor local en el puerto 8000 para pruebas y desarrollo.

## Recursos Adicionales

- **Códigos Preliminares:** Se incluyen scripts y notebooks que fueron útiles durante el desarrollo.
- **Métricas de Evaluación:** Gráficas de perplexity y coherence para el análisis de los modelos de topic modeling LDA.
- **Dataset de libros:** Se proporciona el dataset de libros resultante del web scrapping y algunas variaciones del mismo que se fueron creado a lo largo del desarrollo.

## Contribuciones y Soporte

Las contribuciones son bienvenidas. Si encuentra algún problema o tiene sugerencias, por favor abra un issue en el repositorio del proyecto.

