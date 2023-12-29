# Utiliza una imagen base con Miniconda ya instalado
FROM continuumio/miniconda3

# Copia tu archivo environment.yml al contenedor
COPY environment.yml /tmp/environment.yml
COPY ./Servidor /Servidor


# Actualiza Conda y crea el entorno a partir de tu archivo
RUN conda update -n base -c defaults conda && \
    conda env create -f /tmp/environment.yml 

# Activa el entorno Conda
RUN echo "source activate buscadorLibros" > ~/.bashrc
ENV PATH /opt/conda/envs/buscadorLibros/bin:$PATH
RUN python -m spacy download es_core_news_sm

# Exponer el puerto 8000 para el servidor web
EXPOSE 8000


WORKDIR /Servidor

# Comando para ejecutar tu aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
