# Definimos la matriz de compatibilidad
matrix_show_type_gender_song = {
    "Pop": {"Peña": 3, "Festival": 4, "Obra de Teatro": 2, "Políticos": 1},
    "Rock": {"Peña": 4, "Festival": 4, "Obra de Teatro": 2, "Políticos": 0},
    "Hip-hop/Rap": {"Peña": 4, "Festival": 3, "Obra de Teatro": 1, "Políticos": 0},
    "Música Electrónica": {"Peña": 3, "Festival": 4, "Obra de Teatro": 1, "Políticos": 0},
    "Country": {"Peña": 4, "Festival": 3, "Obra de Teatro": 2, "Políticos": 2},
    "Jazz": {"Peña": 3, "Festival": 3, "Obra de Teatro": 3, "Políticos": 3},
    "Música Clásica": {"Peña": 2, "Festival": 3, "Obra de Teatro": 4, "Políticos": 4},
    "R&B/Soul": {"Peña": 3, "Festival": 4, "Obra de Teatro": 2, "Políticos": 1},
    "Indie/Alternativa": {"Peña": 3, "Festival": 4, "Obra de Teatro": 2, "Políticos": 1},
    "Regueton": {"Peña": 3, "Festival": 3, "Obra de Teatro": 0, "Políticos": 0},
    "Salsa": {"Peña": 4, "Festival": 4, "Obra de Teatro": 2, "Políticos": 1},
}

# Definimos la matriz de compatibilidad
matrix_show_type_dance_style = {
    "Ballet": {"Peña": 2, "Festival": 3, "Obra de Teatro": 4, "Políticos": 3},
    "Hip-hop": {"Peña": 4, "Festival": 4, "Obra de Teatro": 2, "Políticos": 0},
    "Salsa": {"Peña": 4, "Festival": 4, "Obra de Teatro": 2, "Políticos": 1},
    "Tango": {"Peña": 3, "Festival": 3, "Obra de Teatro": 3, "Políticos": 2},
    "Danza Contemporánea": {"Peña": 3, "Festival": 4, "Obra de Teatro": 4, "Políticos": 2},
    "Flamenco": {"Peña": 3, "Festival": 3, "Obra de Teatro": 4, "Políticos": 2},
    "Breakdance": {"Peña": 4, "Festival": 4, "Obra de Teatro": 1, "Políticos": 0},
    "Jazz Dance": {"Peña": 3, "Festival": 4, "Obra de Teatro": 3, "Políticos": 3},
    "Danza Folklórica": {"Peña": 4, "Festival": 3, "Obra de Teatro": 3, "Políticos": 2},
    "Danza Clásica India": {"Peña": 3, "Festival": 3, "Obra de Teatro": 4, "Políticos": 2},
}

# Definimos la matriz de compatibilidad
matrix_theatrical = {
    "Obra de teatro corta": {"Peña": 3, "Festival": 3, "Obra de Teatro": 4, "Políticos": 2},
    "Monólogo": {"Peña": 4, "Festival": 4, "Obra de Teatro": 3, "Políticos": 3},
    "Declamación de poema": {"Peña": 3, "Festival": 3, "Obra de Teatro": 3, "Políticos": 4},
    "Improvisación teatral": {"Peña": 4, "Festival": 4, "Obra de Teatro": 3, "Políticos": 1},
    "Teatro de sombras": {"Peña": 3, "Festival": 3, "Obra de Teatro": 4, "Políticos": 2},
    "Stand-up comedy": {"Peña": 4, "Festival": 4, "Obra de Teatro": 2, "Políticos": 1},
    "Cuentacuentos": {"Peña": 3, "Festival": 3, "Obra de Teatro": 3, "Políticos": 2},
    "Performance experimental": {"Peña": 3, "Festival": 4, "Obra de Teatro": 4, "Políticos": 1},
}

matrix_theatrical_gender ={
    "Comedia": {"Peña": 4, "Festival": 4, "Obra de Teatro": 4, "Políticos": 2},
    "Drama": {"Peña": 2, "Festival": 2, "Obra de Teatro": 3, "Políticos": 1},
    "Romance": {"Peña": 3, "Festival": 3, "Obra de Teatro": 3, "Políticos": 1},
}

def get_compatibility_theatrical_gender(gender, show_type):
    return matrix_theatrical_gender.get(gender, {}).get(show_type, "Desconocido")

def get_compatibility_type_theatric(theatric_type, show_type):
    """
    Función que devuelve la compatibilidad entre un número teatral y un tipo de espectáculo.
    """
    return matrix_theatrical.get(theatric_type, {}).get(show_type, "Desconocido")


def get_compatibility_style_show_type(style, show_type):
    """
    Función que devuelve la compatibilidad entre un estilo de baile y un tipo de espectáculo.
    """
    return matrix_show_type_dance_style.get(style, {}).get(show_type, "Desconocido")


def get_compatibility_gender_show_type(gender, show_type):
    """
    Función que devuelve la compatibilidad entre un género y un tipo de espectáculo.
    """
    return matrix_show_type_gender_song.get(gender, {}).get(show_type, "Desconocido")