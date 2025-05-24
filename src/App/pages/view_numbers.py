import streamlit as st

st.title("📜 Ver Números Culturales")

# Revisar si hay números culturales en session_state
if "cultural_numbers" not in st.session_state or not st.session_state["cultural_numbers"]:
    st.warning("No hay números culturales guardados todavía.")
else:
    # Mostrar lista de números culturales
    for idx, num in enumerate(st.session_state["cultural_numbers"]):
        with st.expander(f"🎭 {num['Name']} ({num['Type']})"):
            st.write(f"**Duración:** {num['Time']} min")

            if "Artists" in num and num["Artists"]:
                st.write("**Artistas y Popularidad:**")
                for artist, popularity in num["Artists"]:
                    st.write(f"- {artist}: {popularity}")

            if num["Type"] == "Song":
                st.write(
                    f"🎵 **Song:** {num['Song']} | Género: {num['Genre']} | Compuesta: {'Sí' if num['Composed'] else 'No'}")
            elif num["Type"] == "Dance":
                st.write(f"💃 **Estilos de Danza:** {', '.join(num['Styles'])}")
            elif num["Type"] == "Theatric":
                st.write(f"🎭 **Tipo de Actuación:** {num['Theatric type']} | Géneros: {', '.join(num['Theatric genders'])}")

            # Botón para eliminar un número cultural
            if st.button(f"Eliminar {num['Name']}", key=f"delete_{idx}"):
                st.session_state["cultural_numbers"].pop(idx)
                st.experimental_rerun()

# Botón para ejecutar el modelo y generar el guion
if st.button("🎬 DAME GUION"):
    st.switch_page("pages/execute_model.py")