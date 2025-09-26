# 1. Importação de bibliotecas

import plotly.express as px
import numpy as np
import datetime
import streamlit as st
import pyodbc
import pandas as pd

# 🔧 Configurações visuais
st.set_page_config(page_title="Dashboard Contoso", layout="wide")

cores_personalizadas = ['#0078D4', '#00B294', '#FFB900', '#E81123', '#5C2D91', '#A1C9F4']




# 2. Conexão com o banco de dados

dados_conexao = (
    "Driver={SQL Server};"
    "Server=Debora;"
    "Database=ContosoRetailDW;"
)
conexao = pyodbc.connect(dados_conexao)

# 3. Consulta SQL e carregamento dos dados

query = """
SELECT 
    d.CalendarYear,
    ch.ChannelName,
    geo.RegionCountryName,
    geo.ContinentName,
    SUM(fs.SalesAmount) AS Receita,
    SUM(fs.TotalCost) AS Custo,
    SUM(fs.SalesQuantity) AS Quantidade
FROM FactSales fs
JOIN DimDate d ON fs.DateKey = d.DateKey
JOIN DimChannel ch ON fs.ChannelKey = ch.ChannelKey
JOIN DimStore st ON fs.StoreKey = st.StoreKey
JOIN DimGeography geo ON st.GeographyKey = geo.GeographyKey
GROUP BY d.CalendarYear, ch.ChannelName, geo.RegionCountryName, geo.ContinentName
ORDER BY Receita DESC
"""

df = pd.read_sql(query, conexao)
df['MargemLucro'] = df['Receita'] - df['Custo']


# 4. Configuração da interface Streamlit

st.set_page_config(page_title="Dashboard Contoso", layout="wide")
st.title("📊 Dashboard de Vendas - ContosoRetailDW")

# 5. Função para exibir KPIs com cor

def format_kpi(label, value, color="black"):
    st.markdown(f"""
        <div style="text-align: center; padding: 10px;">
            <h4 style="margin-bottom: 5px;">{label}</h4>
            <p style="font-size: 24px; color: {color}; font-weight: bold;">{value}</p>
        </div>
    """, unsafe_allow_html=True)
    
# 6. Filtros interativos na sidebar

st.sidebar.header("🔍 Filtros")

anos = sorted(df['CalendarYear'].unique())
ano_selecionado = st.sidebar.selectbox("Ano", anos)

canais = sorted(df['ChannelName'].unique())
canal_selecionado = st.sidebar.multiselect("Canal de Vendas", canais, default=canais)


regioes = sorted(df['RegionCountryName'].unique())
regiao_selecionada = st.sidebar.multiselect("Região", regioes, default=regioes)


# Botão de Reset dos Filtros

if st.sidebar.button("🔄 Resetar Filtros"):
    ano_selecionado = anos[0]
    canal_selecionado = canais
    regiao_selecionada = regioes


# 7. Aplicação dos filtros

df_filtrado = df[
    (df['CalendarYear'] == ano_selecionado) &
    (df['ChannelName'].isin(canal_selecionado)) &
    (df['RegionCountryName'].isin(regiao_selecionada))
    
]

# 8. Preparar os dados para o mapa

df_mapa = df.groupby('RegionCountryName')['Receita'].sum().reset_index()

# 9. Cálculo dos KPIs dinâmicos

receita_total = df_filtrado['Receita'].sum()
custo_total = df_filtrado['Custo'].sum()
margem_total = receita_total - custo_total
quantidade_total = df_filtrado['Quantidade'].sum()


cor_margem = "#0078D4" if margem_total >= 0 else "red"

# 10. Função para formatar valores grandes

def format_num(valor):
    if valor >= 1_000_000_000:
        return f"R$ {valor / 1_000_000_000:.2f}B"
    elif valor >= 1_000_000:
        return f"R$ {valor / 1_000_000:.2f}M"
    elif valor >= 1_000:
        return f"R$ {valor / 1_000:.2f}K"
    else:
        return f"R$ {valor:.2f}"

# 11. Exibição dos KPIs com cor

col1, col2, col3, col4 = st.columns(4)

with col1:
    format_kpi("Receita Total", format_num(receita_total), "#0078D4")
with col2:
    format_kpi("Custo Total", format_num(custo_total), "#0078D4")
with col3:
    format_kpi("Margem de Lucro", format_num(margem_total), "#0078D4")
with col4:
    format_kpi("Qtd Vendida", f"{int(quantidade_total):,}", "#0078D4")

    
# 12. Criar as abas
aba1, aba2, aba3, aba4, aba5, aba6, aba7 = st.tabs([
    "📈 Receita por Canal",
    "📍 Receita por Continente",
    "📊 Evolução Anual",
    "🥧 Participação dos Canais",
    "🗺️ Mapa de Receita por País",
    "📊 Evolução por Canal",
    "📦 Exportações"
])


# 13. Gráfico por Canal (aba 1)

with aba1:
    # Ordena os dados pela Receita (decrescente)
    df_filtrado = df_filtrado.sort_values(by='Receita', ascending=False)

    # Cria gráfico de barras verticais com ordem manual
    fig_canal = px.bar(df_filtrado,
                       x='ChannelName',
                       y='Receita',
                       color='ChannelName',
                       color_discrete_sequence=cores_personalizadas,
                       labels={'ChannelName': 'Canal de Vendas', 'Receita': 'Receita (R$)'},
                       title=f"📈 Receita por Canal - {ano_selecionado}",
                       category_orders={'ChannelName': df_filtrado['ChannelName'].tolist()})

    fig_canal.update_layout(
        showlegend=False,
        margin=dict(t=40)
    )

    st.plotly_chart(fig_canal, use_container_width=True)

    
# 14. Gráfico por Região (aba 2)

with aba2:
    df_continente = df.groupby('ContinentName')['Receita'].sum().reset_index()
    df_continente = df_continente.sort_values(by='Receita', ascending=False)


    fig_regiao = px.bar(df_continente,
                    x='Receita',
                    y='ContinentName',
                    orientation='h',
                    labels={'ContinentName': 'Continente', 'Receita': 'Receita (R$)'},
                    color='ContinentName',
                    color_discrete_sequence=cores_personalizadas,
                    title="📍 Receita por Continente")

    fig_regiao.update_layout(
        showlegend=False,
        margin=dict(t=40),
)

    st.plotly_chart(fig_regiao, use_container_width=True)

    
# 15. Evolução Anual (aba 3)

with aba3:
    df_ano = df.groupby('CalendarYear')['Receita'].sum().reset_index()
    fig_ano = px.line(df_ano,
                      x='CalendarYear',
                      y='Receita',
                      title="Evolução da Receita por Ano",
                      color_discrete_sequence=cores_personalizadas,
                      labels={'CalendarYear': 'Ano', 'Receita': 'Receita (R$)'},
                      markers=True)
    fig_ano.update_layout(
    title="Evolução da Receita por Ano",
    showlegend=True,
    margin=dict(t=40),
)

    st.plotly_chart(fig_ano, use_container_width=True)
    
    
# 16. Participação dos Canais (aba 4)

with aba4:
    df_canais = df.groupby('ChannelName')['Receita'].sum().reset_index()
    fig_pizza = px.pie(df_canais,
                       names='ChannelName',
                       values='Receita',
                       labels={'ChannelName': 'Canal', 'Receita': 'Receita (R$)'},
                       color_discrete_sequence=cores_personalizadas,
                       title="Participação dos Canais de Vendas")
    fig_pizza.update_layout(
    title="Participação dos Canais de Vendas",
    showlegend=True,
    margin=dict(t=40),
)

    st.plotly_chart(fig_pizza, use_container_width=True)
    
# 17. Gráfico de mapa com Plotly

with aba5:
    df_mapa = df.groupby('RegionCountryName')['Receita'].sum().reset_index()
    fig_mapa = px.choropleth(df_mapa, locations='RegionCountryName',
                             locationmode='country names', color='Receita',
                             color_continuous_scale='Blues',
                             title="Mapa de Receita por País")
    st.plotly_chart(fig_mapa, use_container_width=True)
    
    
    fig_mapa.update_layout(
    title="Receita Total por País",
    showlegend=True,
    margin=dict(t=40),
)

    st.plotly_chart(fig_mapa, use_container_width=True)
    
# 18. Análise temporal: gráfico de linha com múltiplos canais

with aba6:
    df_temporal = df.groupby(['CalendarYear', 'ChannelName'])['Receita'].sum().reset_index()

    fig_temporal = px.line(df_temporal, x='CalendarYear', y='Receita',
                        color='ChannelName',
                        markers=True,
                        labels={'ChannelName': 'Canal', 'Receita': 'Receita (R$)'},
                        color_discrete_sequence=cores_personalizadas,
                        title="📈 Evolução da Receita por Canal ao Longo dos Anos")
    fig_temporal.update_layout(
    title="Evolução da Receita por Canal ao Longo dos Anos",
    showlegend=True,
    margin=dict(t=40),
)


    st.plotly_chart(fig_temporal, use_container_width=True)
    
# 19. 4. Exportação avançada: download de dados agregados

with aba7:
    df_agregado = df.groupby(['ChannelName', 'RegionCountryName'])[['Receita', 'Custo', 'MargemLucro']].sum().reset_index()

    st.download_button(
        label="📥 Baixar dados agregados",
        data=df_agregado.to_csv(index=False).encode('utf-8'),
        file_name='dados_agregados.csv',
        mime='text/csv'
)

    
