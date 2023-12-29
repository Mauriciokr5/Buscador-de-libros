import pandas as pd
import spacy
import torch
import numpy as np
from sentence_transformers import SentenceTransformer, util

# Carga del modelo Spacy y SentenceTransformer
nlp = spacy.load("es_core_news_sm")
model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')

# Función para la normalización del texto
def normalizacion(cadena):
    doc = nlp(cadena)
    texto_normalizado = ""
    for token in doc:
        if not token.is_stop and token.pos_ != 'SPACE':
            texto_normalizado += f" {token.lemma_}"
    return texto_normalizado[1:]

# Función principal para procesar la consulta
def procesar_consulta(consulta, genero, libros_df):
    # Normalización de la consulta
    sentences1 = [normalizacion(consulta)]

    # Codificación (embedding) de la consulta
    embeddings1 = model.encode(sentences1, convert_to_tensor=True)

    # Carga de los embeddings precalculados de los libros
    ruta_libros_tm_e = 'ruta_a_tu_archivo.csv'  # Asegúrate de proporcionar la ruta correcta al archivo CSV
    libros = libros_df.copy()
    embeddings2 = libros['Embeddings'].apply(lambda x: torch.tensor(eval(x)))
    embeddings2 = torch.stack(embeddings2.tolist())

    # Cálculo de las puntuaciones de similitud de coseno
    cosine_scores = util.cos_sim(embeddings1, embeddings2)

    # Asignación de las puntuaciones al DataFrame de libros
    libros['Similitud_Coseno'] = cosine_scores[0].cpu().tolist()

    # Selección de los libros de acuerdo al género y similitud
    if genero:
        libros_seleccionados = libros[libros['Género'] == genero].sort_values('Similitud_Coseno', ascending=False).head(5)
    else:
        libros_seleccionados = libros.sort_values('Similitud_Coseno', ascending=False).head(5)

    # Conversión de los resultados a un formato adecuado para JSON
    resultado = libros_seleccionados.to_dict(orient='records')

    return resultado

def dict_a_array(dict_dist, num_topics=6):
    return np.array([dict_dist.get(i, 0) for i in range(num_topics)])

# Función para calcular la distancia euclidiana
def distancia_euclidiana(distribucion1, distribucion2):
    return np.linalg.norm(distribucion1 - distribucion2)


def generar_recomendacion(libro, libros_df):
    libros = libros_df.copy()
    # Aplicar la conversión y calcular la distancia
    libros['Distancia'] = libros['Topic Distribution'].apply(lambda x: distancia_euclidiana(dict_a_array(eval(x)), dict_a_array(eval(libro['Topic Distribution']))))
  
    libros = libros.drop(libros[libros['ISBN'] == libro['ISBN']].index)

    # Encontrar la fila con la menor distancia
    top_4_mas_cercanos = libros[libros['Género']== libro['Género']].sort_values('Distancia').head(4)
    return top_4_mas_cercanos.to_dict(orient='records')