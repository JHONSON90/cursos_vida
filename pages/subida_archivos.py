import streamlit as st
import pandas as pd 

def show_carga_archivos_page():
    st.title("SUBIDA DE ARCHIVOS")

    archivo = st.file_uploader("Carga tu archivo Excel", type=["xlsx"])

    if archivo:
        df = pd.read_excel(archivo, sheet_name = "Hoja1")
        st.session_state["df"] = df
        st.success("Datos Cargados Correctamente.")
        st.dataframe(df.head(5))
    else:
        st.warning("Revisa que los datos esten guardados en Hoja1")