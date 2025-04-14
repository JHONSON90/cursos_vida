# import streamlit as st
# import pandas as pd
# import numpy as np

# st.title('Uber pickups in NYC')

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# datos = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })
# st.table(datos)

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)


# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)


# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# st.text_input("Your name", key="name")

# # You can access the value at any point with:
# st.session_state.name

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data


# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

import streamlit as st

st.set_page_config(
    page_title="Limpieza de base de datos",
    page_icon="😁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] {  /* Ocultar el contenedor de las páginas */
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

DIANA_MARIA = "30122023"

# Inicializar el estado de la sesión para la autenticación
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "page" not in st.session_state:
    st.session_state.page = "login"  # Página inicial es el login

# --- Importar las páginas (que están en la carpeta pages) ---
# Estas funciones las definimos en los archivos correspondientes
from pages.subida_archivos import show_carga_archivos_page
from pages.cursos_de_vida import show_cursos_vida_page
from pages.poblacion import show_poblacion_page

# --- Función para mostrar el formulario de login ---
def show_login_page():
    st.title("Iniciar Sesión")
    with st.form(key="login_form"):
        password = st.text_input("Contraseña", type="password")
        submit_button = st.form_submit_button("Iniciar Sesión")

        if submit_button:
            if password == DIANA_MARIA:
                st.session_state.authenticated = True
                st.session_state.page = "carga_archivos"  # Redirigir a la página de carga de archivos
                st.success("¡Inicio de sesión exitoso!")
                st.rerun()  # Refrescar la página para mostrar el contenido autenticado
            else:
                st.error("Contraseña incorrecta. Intenta de nuevo.")

# --- Lógica de navegación ---
if not st.session_state.authenticated:
    show_login_page()
else:
    # Inyectar CSS para estilizar los botones
    st.markdown(
        """
        <style>
        [data-testid="stSidebarNav"] {  /* Ocultar las páginas predeterminadas */
            display: none;
        }
        .custom-button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            margin: 5px 0;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
            text-align: left;
        }
        .custom-button:hover {
            background-color: #45a049;
        }
        .custom-button-active {
            background-color: #2196F3;
            color: white;
            padding: 10px 20px;
            margin: 5px 0;
            border: none;
            border-radius: 5px;
            width: 100%;
            text-align: left;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Barra lateral para navegación
    st.sidebar.title("Navegación")

    # Usar botones estilizados con emojis
    pages = [
        ("📁 Carga de Archivos", "carga_archivos"),  # Emoji de carpeta
        ("🌍 Población", "poblacion"),              # Emoji de globo terráqueo
        ("📊 Cursos de Vida", "cursos_vida")        # Emoji de gráfico
    ]

    for page_name, page_key in pages:
        # Determinar si este botón está activo
        is_active = st.session_state.page == page_key
        button_style = "custom-button-active" if is_active else "custom-button"
        
        if st.sidebar.button(
            page_name,
            key=f"btn_{page_key}",
            help=f"Ir a {page_name}",
            use_container_width=True
        ):
            st.session_state.page = page_key
            st.rerun()

    # Botón para cerrar sesión con emoji
    if st.sidebar.button(
        "🚪 Cerrar Sesión",
        key="btn_logout",
        help="Cerrar la sesión actual",
        use_container_width=True
    ):
        st.session_state.authenticated = False
        st.session_state.page = "login"
        st.rerun()

    # Mostrar la página seleccionada
    if st.session_state.page == "carga_archivos":
        show_carga_archivos_page()
    elif st.session_state.page == "poblacion":
        show_poblacion_page()
    elif st.session_state.page == "cursos_vida":
        show_cursos_vida_page()

