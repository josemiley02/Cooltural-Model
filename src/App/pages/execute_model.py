import streamlit as st
from Entities.cultural_number import Cultural
from Entities.singing_performance import *
from Entities.dancing_performance import *
from Entities.theatrical_performance import *
from Model.model import Model


def get_cultural_numbers() -> list[Cultural]:
    cultural_numbers = []
    number_id = 0
    for idx, num in enumerate(st.session_state["cultural_numbers"]):
        cultural_number = None
        if num["Type"] == "Song":
            cultural_number = singing_performance(number_id= number_id, number_name= num["Name"], time= num["Time"], number_type= "Song",
                                                  song_name= num["Song"],artists= num["Artists"], gender= num["Genre"], composed= num["Composed"])
        elif num["Type"] == "Dance":
            cultural_number = dancing_performance(number_id= number_id, number_name= num["Name"], time= num["Time"], number_type= "Dance",
                                                   artists=num["Artists"], songs=num["Songs"], styles=num["Styles"], count_dancers=num["Dancers"])
        else:
            cultural_number = theatrical_performance(number_id= number_id, number_name= num["Name"], time= num["Time"], number_type= "Theatric",
                                                     artists=num["Artists"] ,type_performance= num["Theatric type"], genders= num["Theatric genders"])
        cultural_numbers.append(cultural_number)
        number_id += 1
    return cultural_numbers

st.title("Listo para hacerte un guion: ")
time_max = st.number_input("Tiempo del Show")
min_count = st.number_input("Cantidad Minima de Numeros", min_value=1)
max_count = st.number_input("Cantidad Maxima de Numeros", min_value=min_count)
show_type = st.selectbox("Selecciona el tipo de espectaculo", ["Festival", "Obra de Teatro", "Peña", "Político"])

if st.button("Generar Guion"):
    list_cultural_numbers = get_cultural_numbers()
    model = Model(
        cultural_numbers=list_cultural_numbers,
        max_time=time_max,
        show_type=show_type,
        min_count_numbers=min_count,
        max_count_numbers=max_count
    )

    result, score = model.get_show()

    # Puedes mostrar el resultado:
    for item in result:
        st.markdown(f"""
        - **Nombre:** {item.number_name}  
        - **Duración:** {item.time} minutos
        """)

    st.write(score)