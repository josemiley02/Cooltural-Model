import streamlit as st

# Definir colores según cada facultad
FACULTADES = {
    "Ingeniería": {"primaryColor": "#FF0000", "backgroundColor": "#000000"},
    "Artes": {"primaryColor": "#8E44AD", "backgroundColor": "#F4ECF7"},
    "Medicina": {"primaryColor": "#229954", "backgroundColor": "#E8F8F5"},
    "Ciencias": {"primaryColor": "#2874A6", "backgroundColor": "#D6EAF8"},
}

st.title("🎭 Aplicación de Guiones Culturales")

# Botón para desplegar opciones de colores
if "selected_faculty" not in st.session_state:
    st.session_state["selected_faculty"] = None

if st.button("🎨 Color"):
    st.session_state["show_faculty_menu"] = not st.session_state.get("show_faculty_menu", False)

# Mostrar menú de facultades si el usuario tocó el botón
if st.session_state.get("show_faculty_menu", False):
    selected_faculty = st.selectbox("Seleccione su facultad", list(FACULTADES.keys()))

    # Actualizar colores
    if selected_faculty:
        st.session_state["selected_faculty"] = selected_faculty
        colores = FACULTADES[selected_faculty]

        st.markdown(f"""
        <style>
            :root {{
                --primary-color: {colores["primaryColor"]};
                --background-color: {colores["backgroundColor"]};
            }}
            .stApp {{
                background-color: {colores["backgroundColor"]} !important;
            }}
        </style>
        """, unsafe_allow_html=True)

        st.success(f"Color de {selected_faculty} aplicado ✅")

st.write("Selecciona una opción en el menú lateral.")

st.sidebar.title("Menú")
st.sidebar.page_link("pages/add_numbers.py", label="Crear Número Cultural")
st.sidebar.page_link("pages/view_numbers.py", label="Seleccionar Números")
st.sidebar.page_link("pages/execute_model.py", label="Optimización del Guion")