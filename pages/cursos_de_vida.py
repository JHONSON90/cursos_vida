import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def show_cursos_vida_page():

    st.title("Cursos de vida")

    if "df" in st.session_state:
        df = st.session_state["df"]

        if "Curso de vida" in df.columns:
            #total municipio discriminado por sexo
            total_mpios_cursovida = df.groupby(['Mun Horus', 'Curso de vida'])['Curso de vida'].count().unstack()
            total_mpios = total_mpios_cursovida.fillna(0).astype(int)  # Handle missing values and convert to integers
            st.write(total_mpios)
        else:
            condiciones = [
                (df["Edad Cumplida"] <= 5),
                (df["Edad Cumplida"] <= 11),
                (df["Edad Cumplida"] <= 17),
                (df["Edad Cumplida"] <= 28),
                (df["Edad Cumplida"] <= 59),
                (df["Edad Cumplida"] > 59)
            ]

            valores = [
                        "Primera Infancia",
                        "Infancia",
                        "Adolescencia",
                        "Juventud",
                        "Adultez",
                        "Vejez"
                    ]

            # Aplicar np.select() para crear la nueva columna
            df["Curso de vida"] = np.select(condiciones, valores, default="Desconocido")
            
            total_mpios_cursovida = df.groupby(['Mun Horus', 'Curso de vida'])['Curso de vida'].count().unstack()
            total_mpios = total_mpios_cursovida.fillna(0).astype(int)  # Handle missing values and convert to integers
            st.write(total_mpios)

    vertical_alignment = st.selectbox(
        "Seleccione alineación", ["top", "center", "bottom"], index=1)

    col1, col2 = st.columns(2, vertical_alignment=vertical_alignment)

    with col1:
        x = df["Curso de vida"].value_counts()
        labels = x.index

        st.write(x)

    with col2:
        # Crear el gráfico de pastel
        fig = px.pie(values=x.values, names=x.index, color_discrete_sequence=px.colors.sequential.RdBu)

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, use_container_width=True)

    # Gráfico de dispersión: Cursos de vida por municipio
    st.subheader("Cursos de Vida por Municipio (Gráfico de Dispersión)")

    # Agrupar los datos por municipio y curso de vida, y contar las ocurrencias
    scatter_data = df.groupby(["Mun Horus", "Curso de vida"]).size().reset_index(name="Conteo")

    # Crear el gráfico de dispersión con Plotly Express
    fig_scatter = px.scatter(
        scatter_data,
        x="Mun Horus",              # Eje X: Municipios
        y="Curso de vida",          # Eje Y: Cursos de vida
        size="Conteo",              # Tamaño de los puntos: Conteo
        color="Curso de vida",      # Color por curso de vida (opcional, para distinguirlos mejor)
        color_discrete_sequence=px.colors.sequential.RdBu,  # Paleta de colores
        hover_data=["Conteo"],      # Mostrar el conteo al pasar el mouse
        title="Cursos de Vida por Municipio",
    )

    # Personalizar el diseño del gráfico
    fig_scatter.update_layout(
        xaxis_title="Municipio",
        yaxis_title="Curso de Vida",
        xaxis_tickangle=45,         # Rotar etiquetas del eje X para mejor legibilidad
        height=600,                 # Ajustar altura del gráfico
        showlegend=True,            # Mostrar leyenda
        margin=dict(l=50, r=50, t=80, b=150),  # Ajustar márgenes para que las etiquetas sean visibles
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
