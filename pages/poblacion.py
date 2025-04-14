import streamlit as st
import pandas as pd
import numpy as np

import pydeck as pdk
import plotly.graph_objects as go

def show_poblacion_page():
    st.title("Poblacion departamento de Nariño")

    vertical_alignment = st.selectbox(
        "Ajustar alineación", ["top", "center"], index=1
    )

    col1, col2 = st.columns(2, vertical_alignment=vertical_alignment)

    with col1:
        if "df" in st.session_state:
            df = st.session_state["df"]

            if "Mun Horus" in df.columns:
                total_mpios = df['Mun Horus'].value_counts()
                st.write(total_mpios)
            else:
                condiciones = [
                    (df["Codigo Horus2"] =="52001"),
                    (df["Codigo Horus2"] =="52019"),
                    (df["Codigo Horus2"] =="52022"),
                    (df["Codigo Horus2"] =="52036"),
                    (df["Codigo Horus2"] =="52051"),
                    (df["Codigo Horus2"] =="52079"),
                    (df["Codigo Horus2"] =="52083"),
                    (df["Codigo Horus2"] =="52110"),
                    (df["Codigo Horus2"] =="52203"),
                    (df["Codigo Horus2"] =="52207"),
                    (df["Codigo Horus2"] =="52210"),
                    (df["Codigo Horus2"] =="52215"),
                    (df["Codigo Horus2"] =="52224"),
                    (df["Codigo Horus2"] =="52227"),
                    (df["Codigo Horus2"] =="52233"),
                    (df["Codigo Horus2"] =="52240"),
                    (df["Codigo Horus2"] =="52250"),
                    (df["Codigo Horus2"] =="52254"),
                    (df["Codigo Horus2"] =="52256"),
                    (df["Codigo Horus2"] =="52258"),
                    (df["Codigo Horus2"] =="52260"),
                    (df["Codigo Horus2"] =="52287"),
                    (df["Codigo Horus2"] =="52317"),
                    (df["Codigo Horus2"] =="52320"),
                    (df["Codigo Horus2"] =="52323"),
                    (df["Codigo Horus2"] =="52352"),
                    (df["Codigo Horus2"] =="52354"),
                    (df["Codigo Horus2"] =="52356"),
                    (df["Codigo Horus2"] =="52378"),
                    (df["Codigo Horus2"] =="52381"),
                    (df["Codigo Horus2"] =="52385"),
                    (df["Codigo Horus2"] =="52390"),
                    (df["Codigo Horus2"] =="52399"),
                    (df["Codigo Horus2"] =="52405"),
                    (df["Codigo Horus2"] =="52411"),
                    (df["Codigo Horus2"] =="52418"),
                    (df["Codigo Horus2"] =="52427"),
                    (df["Codigo Horus2"] =="52435"),
                    (df["Codigo Horus2"] =="52473"),
                    (df["Codigo Horus2"] =="52480"),
                    (df["Codigo Horus2"] =="52490"),
                    (df["Codigo Horus2"] =="52506"),
                    (df["Codigo Horus2"] =="52520"),
                    (df["Codigo Horus2"] =="52540"),
                    (df["Codigo Horus2"] =="52560"),
                    (df["Codigo Horus2"] =="52565"),
                    (df["Codigo Horus2"] =="52573"),
                    (df["Codigo Horus2"] =="52585"),
                    (df["Codigo Horus2"] =="52612"),
                    (df["Codigo Horus2"] =="52621"),
                    (df["Codigo Horus2"] =="52678"),
                    (df["Codigo Horus2"] =="52683"),
                    (df["Codigo Horus2"] =="52685"),
                    (df["Codigo Horus2"] =="52687"),
                    (df["Codigo Horus2"] =="52693"),
                    (df["Codigo Horus2"] =="52694"),
                    (df["Codigo Horus2"] =="52696"),
                    (df["Codigo Horus2"] =="52699"),
                    (df["Codigo Horus2"] =="52720"),
                    (df["Codigo Horus2"] =="52786"),
                    (df["Codigo Horus2"] =="52788"),
                    (df["Codigo Horus2"] =="52835"),
                    (df["Codigo Horus2"] =="52838"),
                    (df["Codigo Horus2"] =="52885")
                ]

                valores = ["PASTO","ALBÁN","ALDANA","ANCUYÁ","ARBOLEDA","BARBACOAS","BELÉN","BUESACO","COLÓN","CONSACÁ","CONTADERO","CÓRDOBA","CUASPUD","CUMBAL","CUMBITARA","CHACHAGÜÍ","EL CHARCO","EL PEÑOL","EL ROSARIO","EL TABLÓN DE GÓMEZ","EL TAMBO","FUNES","GUACHUCAL","GUAITARILLA","GUALMATÁN","ILES","IMUÉS","IPIALES","LA CRUZ","LA FLORIDA","LA LLANADA","LA TOLA","LA UNIÓN","LEIVA","LINARES","LOS ANDES","MAGÜI","MALLAMA","MOSQUERA","NARIÑO","OLAYA HERRERA","OSPINA","FRANCISCO PIZARRO","POLICARPA","POTOSÍ","PROVIDENCIA","PUERRES","PUPIALES","RICAURTE","ROBERTO PAYÁN","SAMANIEGO","SANDONÁ","SAN BERNARDO","SAN LORENZO","SAN PABLO","SAN PEDRO DE CARTAGO","SANTA BÁRBARA","SANTACRUZ","SAPUYES","TAMINANGO","TANGUA","SAN ANDRES DE TUMACO","TÚQUERRES","YACUANQUER"]

                df["Mun Horus"] = np.select(condiciones, valores, default="Desconocido")

                total_mpios = df['Mun Horus'].value_counts()
                st.write(total_mpios)



    localizacion = [
        {'Codigo Horus2': 52001, 'LATITUD': 1.0836054947, 'LONGITUD': -77.26010704},
        {'Codigo Horus2': 52019, 'LATITUD': 1.469831916, 'LONGITUD': -77.685380974},
        {'Codigo Horus2': 52022, 'LATITUD': 0.9131431916, 'LONGITUD': -77.769530731},
        {'Codigo Horus2': 52036, 'LATITUD': 1.425254077, 'LONGITUD': -77.59115771},
        {'Codigo Horus2': 52061, 'LATITUD': 1.460051172, 'LONGITUD': -77.712385601},
        {'Codigo Horus2': 52079, 'LATITUD': 1.15637742, 'LONGITUD': -78.15631077},
        {'Codigo Horus2': 52083, 'LATITUD': 1.593645287, 'LONGITUD': -77.01999366},
        {'Codigo Horus2': 52110, 'LATITUD': 1.315833658, 'LONGITUD': -77.116856},
        {'Codigo Horus2': 52123, 'LATITUD': 1.515333732, 'LONGITUD': -77.704517155},
        {'Codigo Horus2': 52207, 'LATITUD': 1.209066732, 'LONGITUD': -77.44063221},
        {'Codigo Horus2': 52210, 'LATITUD': 0.932667458, 'LONGITUD': -77.52808731},
        {'Codigo Horus2': 52260, 'LATITUD': 1.43026376, 'LONGITUD': -77.383115977},
        {'Codigo Horus2': 52215, 'LATITUD': 0.78274688, 'LONGITUD': -77.795331446},
        {'Codigo Horus2': 52224, 'LATITUD': 0.737573939, 'LONGITUD': -77.95958446},
        {'Codigo Horus2': 52227, 'LATITUD': 0.944232274, 'LONGITUD': -77.95958446},
        {'Codigo Horus2': 52233, 'LATITUD': 1.72559011, 'LONGITUD': -77.59281637},
        {'Codigo Horus2': 52240, 'LATITUD': 1.306491842, 'LONGITUD': -77.95302384},
        {'Codigo Horus2': 52250, 'LATITUD': 2.213682925, 'LONGITUD': -77.9533242},
        {'Codigo Horus2': 52258, 'LATITUD': 1.43026376, 'LONGITUD': -77.383115977},
        {'Codigo Horus2': 52259, 'LATITUD': 1.887689437, 'LONGITUD': -7.748319589},
        {'Codigo Horus2': 52268, 'LATITUD': 1.409336207, 'LONGITUD': -77.698326559},
        {'Codigo Horus2': 52283, 'LATITUD': 1.031276376, 'LONGITUD': -77.738311587},
        {'Codigo Horus2': 52287, 'LATITUD': 0.957786429, 'LONGITUD': -77.39552781},
        {'Codigo Horus2': 52317, 'LATITUD': 0.975037904, 'LONGITUD': -77.753811336},
        {'Codigo Horus2': 52323, 'LATITUD': 1.151369268, 'LONGITUD': -77.752758124},
        {'Codigo Horus2': 52326, 'LATITUD': 0.926626623, 'LONGITUD': -77.750156893},
        {'Codigo Horus2': 52352, 'LATITUD': 0.980534037, 'LONGITUD': -77.775186573},
        {'Codigo Horus2': 52354, 'LATITUD': 0.980534037, 'LONGITUD': -77.775186573},
        {'Codigo Horus2': 52356, 'LATITUD': 0.82501, 'LONGITUD': -77.63966},
        {'Codigo Horus2': 52378, 'LATITUD': 1.552175858, 'LONGITUD': -77.892393256},
        {'Codigo Horus2': 52381, 'LATITUD': 1.338034371, 'LONGITUD': -77.742293041},
        {'Codigo Horus2': 52385, 'LATITUD': 1.541184847, 'LONGITUD': -77.761781608},
        {'Codigo Horus2': 52390, 'LATITUD': 2.029627333, 'LONGITUD': -77.751306684},
        {'Codigo Horus2': 52399, 'LATITUD': 1.613697376, 'LONGITUD': -77.712284622},
        {'Codigo Horus2': 52405, 'LATITUD': 1.900862361, 'LONGITUD': -77.731220073},
        {'Codigo Horus2': 52411, 'LATITUD': 1.399173084, 'LONGITUD': -77.752093774},
        {'Codigo Horus2': 52418, 'LATITUD': 1.673501269, 'LONGITUD': -77.771052444},
        {'Codigo Horus2': 52427, 'LATITUD': 1.906858429, 'LONGITUD': -77.804737646},
        {'Codigo Horus2': 52435, 'LATITUD': 1.155947016, 'LONGITUD': -77.78466466},
        {'Codigo Horus2': 52473, 'LATITUD': 2.412493658, 'LONGITUD': -77.731433527},
        {'Codigo Horus2': 52480, 'LATITUD': 1.285775273, 'LONGITUD': -77.73322027},
        {'Codigo Horus2': 52490, 'LATITUD': 2.28785614, 'LONGITUD': -77.831219024},
        {'Codigo Horus2': 52506, 'LATITUD': 1.029815854, 'LONGITUD': -77.755234944},
        {'Codigo Horus2': 52540, 'LATITUD': 2.083564202, 'LONGITUD': -77.859193093},
        {'Codigo Horus2': 52560, 'LATITUD': 1.793864292, 'LONGITUD': -77.752154388},
        {'Codigo Horus2': 52565, 'LATITUD': 0.785941088, 'LONGITUD': -77.752707872},
        {'Codigo Horus2': 52573, 'LATITUD': 1.232864821, 'LONGITUD': -77.759844212},
        {'Codigo Horus2': 52578, 'LATITUD': 0.944351651, 'LONGITUD': -77.753032523},
        {'Codigo Horus2': 52583, 'LATITUD': 0.916739884, 'LONGITUD': -77.765862856},
        {'Codigo Horus2': 52612, 'LATITUD': 1.147671848, 'LONGITUD': -77.805811118},
        {'Codigo Horus2': 52621, 'LATITUD': 1.897581156, 'LONGITUD': -77.783811616},
        {'Codigo Horus2': 52678, 'LATITUD': 1.419051209, 'LONGITUD': -77.769476176},
        {'Codigo Horus2': 52683, 'LATITUD': 1.288105405, 'LONGITUD': -77.745670068},
        {'Codigo Horus2': 52685, 'LATITUD': 1.529782482, 'LONGITUD': -77.702070693},
        {'Codigo Horus2': 52687, 'LATITUD': 1.542139582, 'LONGITUD': -77.72187279},
        {'Codigo Horus2': 52693, 'LATITUD': 1.518376274, 'LONGITUD': -77.757327379},
        {'Codigo Horus2': 52694, 'LATITUD': 1.536823494, 'LONGITUD': -77.710140325},
        {'Codigo Horus2': 52696, 'LATITUD': 2.494420411, 'LONGITUD': -77.798256461},
        {'Codigo Horus2': 52699, 'LATITUD': 1.285175376, 'LONGITUD': -77.778745114},
        {'Codigo Horus2': 52736, 'LATITUD': 1.045287472, 'LONGITUD': -77.776810544},
        {'Codigo Horus2': 52788, 'LATITUD': 1.064661112, 'LONGITUD': -77.732525316},
        {'Codigo Horus2': 52835, 'LATITUD': 1.79112, 'LONGITUD':  -78.79275},
        {'Codigo Horus2': 52838, 'LATITUD': 1.154410523, 'LONGITUD': -77.763073491},
        {'Codigo Horus2': 52885, 'LATITUD': 1.125547916, 'LONGITUD': -77.742467258},
        {'Codigo Horus2': 52786, 'LATITUD': 1.591661392, 'LONGITUD': -77.325253116},
    ]


    geolocalizacion = pd.DataFrame(localizacion)

    df_geolocalizado = pd.merge(df, geolocalizacion, on='Codigo Horus2', how='left')

    grouped_data = df_geolocalizado.groupby('Mun Horus').agg({'LATITUD': 'mean',
            'LONGITUD':'mean',
            'Codigo Horus2': 'count'
            }).reset_index()

    grouped_data = grouped_data.rename(columns={'Codigo Horus2': 'Conteo'})


    with col2:
        # Configurar la capa del mapa
        layer = pdk.Layer(
            "ScatterplotLayer",  # Tipo de capa para marcadores
            data=grouped_data,
            get_position=["LONGITUD", "LATITUD"],  # Coordenadas [longitud, latitud]
            get_radius="Conteo * 1",  # Radio de los marcadores en metros
            radius_min_pixels=5,  # Tamaño mínimo del círculo en píxeles
            radius_max_pixels=50,  # Tamaño máximo del círculo en píxeles
            get_fill_color=[255, 0, 0, 140],  # Color RGBA (rojo con transparencia)
            pickable=True,  # Permite interactuar (tooltips)
            auto_highlight=True
        )

        # Configurar la vista inicial del mapa
        view_state = pdk.ViewState(
            latitude=grouped_data["LATITUD"].mean(),  # Centrar en la media de latitudes
            longitude=grouped_data["LONGITUD"].mean(),  # Centrar en la media de longitudes
            zoom=6,  # Nivel de zoom inicial
            pitch=0  # Ángulo de inclinación
        )

        # Crear el objeto PyDeck
        deck = pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"text": "Ciudad: {Mun Horus}\nConteo: {Conteo}"  # Tooltip con nombre y conteo
            }
        )

        # Mostrar el mapa en Streamlit
        st.pydeck_chart(deck)


    st.title("Clasificación por Municipio y sexo")

    col3, col4 = st.columns(2, vertical_alignment=vertical_alignment)

    with col3:

        #total municipio discriminado por sexo

        total_mpios_sexo = df.groupby(['Mun Horus', 'Sexo'])['Sexo'].count().unstack()
        total_mpios_sexo = total_mpios_sexo.fillna(0).astype(int)
        st.write(total_mpios_sexo)  


    with col4:
        # Crear el gráfico de barras horizontales apiladas con Plotly
        fig = go.Figure()

        # Agregar las barras para "Mujeres"
        fig.add_trace(go.Bar(
            y=total_mpios_sexo.index,  # Municipios en el eje Y
            x=total_mpios_sexo['Femenino'],  # Valores para "Mujeres" en el eje X
            name='Mujeres',
            orientation='h',  # Barras horizontales
            marker=dict(color='orangered')  # Color para "Mujeres"
        ))

        # Agregar las barras para "Hombres"
        fig.add_trace(go.Bar(
            y=total_mpios_sexo.index,  # Municipios en el eje Y
            x=total_mpios_sexo['Masculino'],  # Valores para "Hombres" en el eje X
            name='Hombres',
            orientation='h',  # Barras horizontales
            marker=dict(color='blue')  # Color para "Hombres"
        ))

        # Configurar el diseño del gráfico
        fig.update_layout(
            title="Población por Municipio y Sexo",
            xaxis_title="Total",
            yaxis_title="Municipio",
            barmode='stack',  # Modo apilado para las barras
            yaxis=dict(autorange="reversed"),  # Invertir el eje Y para que el primer municipio esté arriba
            legend=dict(
                x=0.95,  # Posición de la leyenda (a la derecha)
                y=0.05,  # Posición de la leyenda (abajo)
                bgcolor='rgba(255, 255, 255, 0.5)',  # Fondo de la leyenda
                bordercolor='black',
                borderwidth=1
            ),
            margin=dict(l=150),  # Ajustar el margen izquierdo para que los nombres de los municipios sean visibles
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig)