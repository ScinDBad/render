""" Script que simula el lanzamiento de una moneda mediante prueba bernoulli.
    Obtiene la media de probabilidades por todos los intentos.
    Se utiliza en una app de streamlit para visualizar en el browser la
    simulación y muestra el trazado gráfico junto con una tabla historica de 
    los datos obtenidos
"""
import time
import pandas as pd
import scipy.stats
import streamlit as st

# estas son variables de estado que se conservan cuando Streamlin vuelve a ejecutar este script
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iteraciones', 'media'])

st.header('Lanzar una moneda')
chart = st.line_chart([0.5])

# función que emula el lanzamiento de una moneda
def toss_coin(n):
    """
    Simula el lanzamiento de una moneda y devuelve la media de las probabilidades.

    Parameters:
    - n (int): Número de intentos.

    Returns:
    - float: Media de las probabilidades calculadas.
    """
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    st.session_state['experiment_no'] += 1
    mean_toss = toss_coin(number_of_trials)
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        pd.DataFrame(data=[[st.session_state['experiment_no'],
                            number_of_trials,
                            mean_toss]],
                     columns=['no', 'iteraciones', 'media'])
        ],
        axis=0)
    st.session_state['df_experiment_results'] = \
        st.session_state['df_experiment_results'].reset_index(drop=True)

st.write(st.session_state['df_experiment_results'])
#st.write('Esta aplicación aún no es funcional. En construcción.')
