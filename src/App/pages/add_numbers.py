import streamlit as st
from Services.compatibilty import *
from Services.database import VIDEOS

# Definir géneros compatibles según la matriz de compatibilidad
GENRES_SONGS = matrix_show_type_gender_song.keys()
TYPES_DANCES = matrix_show_type_dance_style.keys()

THEATRIC_TYPES = matrix_theatrical.keys()
THEATRIC_GENRES = matrix_theatrical_gender.keys()

st.title("🎭 Agregar Número Cultural")

# Selección del tipo de número
options = ["Song", "Dance", "Theatric"]
number_type = st.selectbox("Seleccione el tipo de número cultural", options)

# Campos comunes
number_name = st.text_input("Nombre del número cultural")
time = st.number_input("Duración (minutos)", min_value=1, max_value=60, value=10)

# Ingreso de artistas con popularidad
artists = st.text_area("Ingrese artistas y popularidad (Ej: Juan,80 | María,95)")
artists_set = set()

if artists:
    for entry in artists.split("|"):
        try:
            name, popularity = entry.strip().split(",")
            artists_set.add((name.strip(), int(popularity.strip())))
        except ValueError:
            st.error("Formato incorrecto. Use 'Nombre,Popularidad' separados por '|'")

# 🟢 Si se selecciona "Song", mostrar campos adicionales
if number_type == "Song":
    song_name = st.selectbox("Ingrese el nombre la cancion", VIDEOS.keys(), accept_new_options= True)
    song_genre = st.selectbox("Género de la canción", GENRES_SONGS)
    composed = st.checkbox("¿Es una canción original compuesta por los artistas?")
    instrument = st.checkbox("¿Se usan instrumentos en el numero?")

if number_type == "Dance":
    songs_names = st.multiselect("Ingrese las canciones", VIDEOS.keys(), accept_new_options= True)
    songs_set = set(songs_names)
    styles_names = st.multiselect("Escoja los estlos", TYPES_DANCES)
    styles_set = set(styles_names)
    count_dancer = st.number_input("Cantidad de Bailarines", min_value=1)

if number_type == "Theatric":
    type_performance = st.selectbox("Tipo de Obra", THEATRIC_TYPES)
    genre_theatric = set(st.multiselect("Escoja los genres", THEATRIC_GENRES))

# Guardar número cultural
if st.button("Guardar Número Cultural"):
    new_number = {
        "Type": number_type,
        "Name": number_name,
        "Time": time,
        "Artists": artists_set
    }

    if number_type == "Song":
        new_number.update({
            "Song": song_name,
            "Genre": song_genre,
            "Composed": composed,
            "Instrument": instrument
        })

    if number_type == "Dance":
        new_number.update({
            "Songs": songs_set,
            "Styles": styles_set,
            "Dancers": count_dancer
        })

    if number_type == "Theatric":
        new_number.update({
            "Theatric type": type_performance,
            "Theatric genders": genre_theatric
        })

    st.session_state.setdefault("cultural_numbers", []).append(new_number)
    st.success("Número Cultural guardado exitosamente!")