from email.mime import base
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# tutorial que apresentará dados estatísticos de jogadores da NFL


st.title('Estatísticas de Jogadores da NFL')

# Esse app mostrará estatísticas com focus em Rushing

# Criando o sidebar à esquerda

st.sidebar.header('Busca')
selected_year = st.sidebar.selectbox('Ano', list(reversed(range(1990, 2021))))

# importando dados


@st.cache
def load_data(year):
    url = "https://www.pro-football-reference.com/years/" + \
        str(year) + "/rushing.htm"
    html = pd.read_html(url, header=1)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)  # deletando cabeçalhos repetidos
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats


playerstats = load_data(selected_year)

# Seleção de times na Sidebar
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect(
    'Time ', sorted_unique_team, sorted_unique_team)

# Seleção da Posição
unique_pos = ['RB', 'QB,', 'WR', 'FB', 'TE']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtrando dados
df_selected_team = playerstats[(playerstats.Tm.isin(
    selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Mostrar os Dados Estatísicos')
st.write('Dimensão dos Dados: ' + str(df_selected_team.shape[0])
         + ' linhas e ' + str(df_selected_team.shape[1]) + ' colunas.')

st.dataframe(df_selected_team)

# Link para download dos dados em formato CSV


def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href = "data:file/csv;base64,{b64}" download="playerstats.csv">Download Arquivo CSV</a>'
    return href


st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)


# Gráficos Heatmap


if st.button('Intercorrelação do Mapa de Calor'):
    st.header('Intercorrelação da Matriz do Mapa de Calor')
    df_selected_team.to_csv('dados_time.csv', index=False)
    df = pd.read_csv('dados_time.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot()
