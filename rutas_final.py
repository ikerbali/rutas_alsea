import networkx as nx
import numpy as np
import pandas as pd
from numpy.linalg import norm
import streamlit as st

def lista_en_renglones(lista):
    return '\n'.join(f"{i+1}. {elem}" for i, elem in enumerate(lista))

# Función para calcular similitud coseno
def cosine_similarity(v1, v2):
    if norm(v1) == 0 or norm(v2) == 0:
        return 0  # para evitar división entre cero
    return np.dot(v1, v2) / (norm(v1) * norm(v2))

def ruta(inicio, destino):
    if inicio not in G or destino not in G:
        return "Uno o ambos nodos no existen en el grafo.", None
    try:
        ruta_mas_corta = nx.shortest_path(G, source=inicio, target=destino, weight='weight')
        return f"La ruta más corta de {inicio} a {destino} es:\n{lista_en_renglones(ruta_mas_corta)}", ruta_mas_corta[-1]
    except nx.NetworkXNoPath:
        return f"No hay un camino disponible de {inicio} a {destino}", None

# Cargar el CSV

df_descripciones = pd.read_excel('descripciones_vacantes_embeddings.xlsx')

# Crear diccionario {puesto: descripcion}
descripciones_puestos = dict(zip(df_descripciones["Puesto"], df_descripciones["Descripción embedding"]))

  
grafo_con_pesos = {
    "Crew DP": {"Supervisor DP": [0, 0, 0]},
    
    "Supervisor DP": {
        "Sub-gerente DP": [0, 0, 0],
        "Subgerente de Tienda BK": [0, 0, 0],
        "Supervisor SB": [0, 0, 0]
    },

    "Sub-gerente DP": {
        "Gerente de Tienda C DP": [0, 0, 0],
        "Gerente de Tienda BK": [0, 0, 0],
        "Subgerente de Tienda BK": [0, 0, 0]
    },

    "Gerente de Tienda C DP": {
        "Gerente de Tienda B DP": [0, 0, 0],
        "Gerente de Tienda SB": [0, 0, 0]
    },

    "Gerente de Tienda B DP": {
        "Gerente de Tienda A DP": [0, 0, 0],
        "Gerente de Cocina MM": [0, 0, 0],
        "Gerente de Servicio MM": [0, 0, 0]
    },

    "Gerente de Tienda A DP": {
        "Distrital Coach Trainee (DC1) DP": [0, 0, 0],
        "Gerente de Tienda SB": [0, 0, 0]
    },

    "Distrital Coach Trainee (DC1) DP": {
        "Gerente de Distrito Supervisor (DC1) DP": [0, 0, 0]
    },

    "Gerente de Distrito Supervisor (DC1) DP": {
        "Gerente de Distrito Supervisor (GV1) DP": [0, 0, 0]
    },

    "Gerente de Distrito Supervisor (GV1) DP": {
        "Distrital Coach (DC2) DP": [0, 0, 0]
    },

    "Distrital Coach (DC2) DP": {
        "Gerente de Divisional de operaciones (GV2) BK": [0, 0, 0]
    },

    "Crew BK": {
        "Subgerente de Tienda BK": [0, 0, 0]
    },

    "Subgerente de Tienda BK": {
        "Gerente de Tienda BK": [0, 0, 0],
        "Subgerente de Tienda SB": [0, 0, 0]
    },

    "Gerente de Tienda BK": {
        "Gerente de Distrito (GV1) BK": [0, 0, 0],
        "Gerente de Tienda SB": [0, 0, 0]
    },

    "Gerente de Tienda SB": {
        "Distrital Coach Trainee (DC1) SB": [0, 0, 0],
        "Gerente de Cocina MM": [0, 0, 0],
        "Gerente de Servicio MM": [0, 0, 0]
    },

    "Gerente de Distrito (GV1) BK": {
        "Distrital Coach (DC2) SB": [0, 0, 0],
        "Gerente de Divisional de operaciones (GV2) BK": [0, 0, 0]
    },

    "Barista SB": {
        "Supervisor SB": [0, 0, 0]
    },

    "Supervisor SB": {
        "Subgerente de Tienda SB": [0, 0, 0],
        "Gerente de Tienda B DP": [0, 0, 0]
    },

    "Subgerente de Tienda SB": {
        "Gerente de Tienda SB": [0, 0, 0]
    },

    "Distrital Coach Trainee (DC1) SB": {
        "Distrital Coach (DC2) SB": [0, 0, 0]
    },

    "Distrital Coach (DC2) SB": {
        "Distrital Coach Senior (DC3) SB": [0, 0, 0]
    },

    "Distrital Coach Senior (DC3) SB": {},

    "Crew MM": {
        "Gerente en Turno MM": [0, 0, 0]
    },

    "Gerente en Turno MM": {
        "Gerente de Servicio MM": [0, 0, 0]
    },

    "Gerente de Servicio MM": {
        "Gerente de Cocina MM": [0, 0, 0],
        "Chef MM": [0, 0, 0]
    },

    "Gerente de Cocina MM": {
        "Gerente General MM": [0, 0, 0]
    },

    "Chef MM": {},

    "Gerente General MM": {
        "Gerente de Distrito (GV1) BK": [0, 0, 0],
        "Distrital Coach (DC2) SB": [0, 0, 0],
        "Gerente de Distrito (GV2) Vips": [0, 0, 0],
        "Distrital Coach (DC2) MM": [0, 0, 0]
    },

    "Gerente de Divisional de operaciones (GV2) MM": {
        "Distrital Coach Senior (DC3) MM": [0, 0, 0]
    },

    "Distrital Coach Senior (DC3) MM ": {},

    "Distrital Coach (DC2) MM": {
        "Gerente de Divisional de operaciones (GV2) MM": [0, 0, 0]
    },

    "Gerente de Divisional de operaciones (GV2) BK": {},

    "Gerente de Divisional de operaciones (GV2) MM": {
        "Distrital Coach Senior (DC3) MM": [0, 0, 0]
    },

    "Distrital Coach Senior (DC3) MM": {},

    "Crew Vips": {
        "Sub-gerente Vips": [0, 0, 0]
    },

    "Sub-gerente Vips": {
        "Gerente de Tienda Vips": [0, 0, 0],
        "Gerente en Turno MM": [0, 0, 0],
        "Subgerente de Tienda SB": [0, 0, 0]
    },

    "Chef Vips": {
        "Chef MM": [0, 0, 0]
    },

    "Gerente de Tienda Vips": {
        "Gerente de Distrito (GV2) Vips": [0, 0, 0],
        "Gerente de Distrito Superior (GV1) DP": [0, 0, 0],
        "Gerente General MM": [0, 0, 0]
    },

    "Gerente de Distrito (GV2) Vips": {},

    "Gerente de Distrito Superior (GV1) DP": {}
}

# Ejemplo para todos los nodos, extraídos de las llaves y valores de tu grafo
todos_los_nodos = set(grafo_con_pesos.keys())
for vecinos in grafo_con_pesos.values():
    todos_los_nodos.update(vecinos.keys())

# Asignar un vector a cada nodo (puedes cambiarlo por vectores reales)
np.random.seed(42)
vectores = {nodo: np.random.rand(3) for nodo in todos_los_nodos}

# Actualizar pesos del grafo con similitud coseno (peso = 1 - similitud para Dijkstra)
for nodo, vecinos in grafo_con_pesos.items():
    for vecino in vecinos:
        v1 = vectores[nodo]
        v2 = vectores[vecino]
        sim = cosine_similarity(v1, v2)
        peso = 1 - sim  # peso para que Dijkstra busque minimizar la "distancia"
        grafo_con_pesos[nodo][vecino] = peso

# Crear grafo dirigido en NetworkX
G = nx.DiGraph()

# Agregar nodos con atributos (vectores)
for nodo in todos_los_nodos:
    G.add_node(nodo, vector=vectores[nodo])

# Agregar aristas con el peso calculado
for nodo, vecinos in grafo_con_pesos.items():
    for vecino, peso in vecinos.items():
        G.add_edge(nodo, vecino, weight=peso)

st.title("Bienvenido a Rutas Alsea")

posiciones = [
    "Crew DP",
    "Supervisor DP",
    "Sub-gerente DP",
    "Subgerente de Tienda BK",
    "Supervisor SB",
    "Gerente de Tienda C DP",
    "Gerente de Tienda BK",
    "Gerente de Tienda B DP",
    "Gerente de Tienda SB",
    "Gerente de Tienda A DP",
    "Distrital Coach Trainee (DC1) DP",
    "Gerente de Distrito Supervisor (DC1) DP",
    "Gerente de Distrito Supervisor (GV1) DP",
    "Distrital Coach (DC2) DP",
    "Gerente de Divisional de operaciones (GV2) BK",
    "Crew BK",
    "Gerente de Distrito (GV1) BK",
    "Distrital Coach Trainee (DC1) SB",
    "Distrital Coach (DC2) SB",
    "Distrital Coach Senior (DC3) SB",
    "Barista SB",
    "Subgerente de Tienda SB",
    "Crew MM",
    "Gerente en Turno MM",
    "Gerente de Servicio MM",
    "Gerente de Cocina MM",
    "Chef MM",
    "Gerente General MM",
    "Gerente de Divisional de operaciones (GV2) MM",
    "Distrital Coach Senior (DC3) MM",
    "Distrital Coach (DC2) MM",
    "Crew Vips",
    "Sub-gerente Vips",
    "Gerente de Tienda Vips",
    "Gerente de Distrito (GV2) Vips",
    "Chef Vips",
    "Gerente de Distrito Superior (GV1) DP"
]

opcion_entrada= st.selectbox(options=posiciones,label="Selecciona tu puesto actual")
opcion_salida= st.selectbox(options=posiciones,label="Selecciona tu meta de puesto")

if st.button(" Calcular la mejor ruta"):
    resultado, puesto_final = ruta(opcion_entrada, opcion_salida)
    st.write(resultado)
    if puesto_final and puesto_final in descripciones_puestos:
        st.markdown(f"**Descripción del puesto final ({puesto_final}):**")
        st.write(descripciones_puestos[puesto_final])
    elif puesto_final:
        st.warning("No se encontró una descripción para el puesto final.")
