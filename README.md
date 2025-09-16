# Projeto de Integração SQL/Python

# 📊 Sales Dashboard — ContosoRetailDW

This project is an interactive dashboard built with **Streamlit** and **Plotly**, integrating data from the **ContosoRetailDW** SQL Server database via **PyODBC**. The goal is to deliver a clean, responsive, browser-based experience for exploring key sales metrics across channels, regions, and time.

---

## 🚀 Purpose

To create a visual interface that allows users to:

- Filter data by year, sales channel, and region  
- Navigate between sections using tabs  
- View KPIs and interactive charts with export options  
- Explore insights by continent, country, and sales channel

---

## 🧰 Libraries Used

| Library            | Purpose                                               |
|--------------------|-------------------------------------------------------|
| `streamlit`        | Web interface and layout                              |
| `plotly.express`   | Interactive and exportable charts                     |
| `pandas`           | Data manipulation                                     |
| `pyodbc`           | SQL Server connection to ContosoRetailDW              |

---

## 🎨 Visual Design Choices

- **Custom Contoso Palette**: corporate tones with adjusted contrast to avoid similar blues  
- **Horizontal bar charts**: improve readability and highlight top performers  
- **Soft-toned KPIs**: reinforce visual identity without overwhelming the layout  
- **Export mode enabled**: all charts include a download-as-image button

---

## 🧭 Navigation

The dashboard is organized into thematic tabs:

- 📈 Revenue by Channel  
- 📍 Revenue by Continent  
- 📊 Yearly Trends  
- 🥧 Channel Share  
- 🗺️ Revenue Map by Country  
- 📦 Export Data  

Each tab presents targeted visualizations with applicable filters, making the experience smooth and intuitive.

---

## 💡 Key Learnings

This project was a hands-on discovery of **Streamlit** and **Plotly**, showcasing how data can be transformed into a visual experience — all within the browser, without complex front-end frameworks.

---

## 📂 Project Structure

- `app.py`: main dashboard script  
- `requirements.txt`: project dependencies  
- `README.md`: documentation and context

---

## 🖥️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
````
## 🚀 Launch the Dashboard

[▶️ Open Dashboard on Browser](http://localhost:8501)

----
✨ Outcome
A lightweight, visually appealing, and functional application — perfect for executive presentations, internal analytics, or as a foundation for larger BI initiatives.
````

````
## 📊 Dashboard de Vendas — ContosoRetailDW - Versão em Português

Este projeto é um dashboard interativo desenvolvido com **Streamlit** e **Plotly**, integrando dados do banco **ContosoRetailDW** via **PyODBC**. A proposta é oferecer uma visualização clara, responsiva e navegável das principais métricas de vendas, canais, regiões e evolução temporal.

---

## 🚀 Objetivo

Criar uma interface visual acessível via navegador que permita:

- Filtrar dados por ano, canal e região
- Navegar entre seções como em um site (via abas)
- Visualizar KPIs e gráficos interativos com exportação
- Explorar insights por continente, país e canal de vendas

---

## 🧰 Bibliotecas Utilizadas

| Biblioteca       | Função Principal                                          |
|------------------|-----------------------------------------------------------|
| `streamlit`      | Interface web interativa e responsiva                     |
| `plotly.express` | Criação de gráficos dinâmicos e exportáveis               |
| `pandas`         | Manipulação de dados tabulares                            |
| `pyodbc`         | Conexão com banco SQL Server (ContosoRetailDW)            |

---

## 🎨 Escolhas Visuais

- **Paleta Contoso Personalizada**: tons corporativos com contraste ajustado para evitar confusão entre azuis semelhantes.
- **Gráficos horizontais ordenados**: facilitam a leitura e destacam os maiores valores no topo.
- **KPIs com tons suaves**: reforçam a identidade visual sem sobrecarregar o layout.
- **Modo de exportação ativado**: todos os gráficos possuem botão para salvar como imagem.

---

## 🧭 Navegação

O dashboard é dividido em abas temáticas:

- 📈 Receita por Canal  
- 📍 Receita por Continente  
- 📊 Evolução Anual  
- 🥧 Participação dos Canais  
- 🗺️ Mapa de Receita por País  
- 📦 Exportações  

Cada aba apresenta visualizações específicas com filtros aplicáveis, tornando a experiência fluida e intuitiva.
---

## 🚀 Acesse o Dashboard

[▶️ Abrir Dashboard no Navegador](http://localhost:8501)


---

## 💡 Aprendizados

Este projeto foi uma descoberta prática das bibliotecas **Streamlit** e **Plotly**, que permitem transformar dados em experiências visuais acessíveis via navegador — sem necessidade de frameworks complexos ou front-end dedicado.

---

## 📂 Organização do Código

- `app.py`: script principal do dashboard
- `requirements.txt`: dependências do projeto
- `README.md`: documentação e contexto do projeto

---

## 🖥️ Como Executar

```bash
pip install -r requirements.txt
streamlit run app.py

````
### 1. Importação de bibliotecas
````

import seaborn as sns
import plotly.express as px
import numpy as np
import datetime
import streamlit as st
import pyodbc
import pandas as pd

`````
### 2. Configurações visuais
```
st.set_page_config(page_title="Dashboard Contoso", layout="wide")

cores_personalizadas = ['#0078D4', '#00B294', '#FFB900', '#E81123', '#5C2D91', '#A1C9F4']
````
### 3. Conexão com o banco de dados
````

dados_conexao = (
    "Driver={SQL Server};"
    "Server=Debora;"
    "Database=ContosoRetailDW;"
)
conexao = pyodbc.connect(dados_conexao)

````
### 4. Consulta SQL e carregamento dos dados
````

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

````
### 5. Configuração da interface Streamlit
````

st.set_page_config(page_title="Dashboard Contoso", layout="wide")
st.title("📊 Dashboard de Vendas - ContosoRetailDW")

````
### 6. Função para exibir KPIs com cor
````

def format_kpi(label, value, color="black"):
    st.markdown(f"""
        <div style="text-align: center; padding: 10px;">
            <h4 style="margin-bottom: 5px;">{label}</h4>
            <p style="font-size: 24px; color: {color}; font-weight: bold;">{value}</p>
        </div>
    """, unsafe_allow_html=True)
````
### 6. Filtros interativos na sidebar
````

st.sidebar.header("🔍 Filtros")

anos = sorted(df['CalendarYear'].unique())
ano_selecionado = st.sidebar.selectbox("Ano", anos)

canais = sorted(df['ChannelName'].unique())
canal_selecionado = st.sidebar.multiselect("Canal de Vendas", canais, default=canais)


regioes = sorted(df['RegionCountryName'].unique())
regiao_selecionada = st.sidebar.multiselect("Região", regioes, default=regioes)

````
### 7. Botão de Reset dos Filtros
````

if st.sidebar.button("🔄 Resetar Filtros"):
    ano_selecionado = anos[0]
    canal_selecionado = canais
    regiao_selecionada = regioes

````
### 8. Aplicação dos filtros
````

df_filtrado = df[
    (df['CalendarYear'] == ano_selecionado) &
    (df['ChannelName'].isin(canal_selecionado)) &
    (df['RegionCountryName'].isin(regiao_selecionada))
    
]
````
### 9. Preparar os dados para o mapa
````

df_mapa = df.groupby('RegionCountryName')['Receita'].sum().reset_index()

````
### 10. Cálculo dos KPIs dinâmicos
````

receita_total = df_filtrado['Receita'].sum()
custo_total = df_filtrado['Custo'].sum()
margem_total = receita_total - custo_total
quantidade_total = df_filtrado['Quantidade'].sum()


cor_margem = "green" if margem_total >= 0 else "red"
````
### 11. Função para formatar valores grandes
````

def format_num(valor):
    if valor >= 1_000_000_000:
        return f"R$ {valor / 1_000_000_000:.2f}B"
    elif valor >= 1_000_000:
        return f"R$ {valor / 1_000_000:.2f}M"
    elif valor >= 1_000:
        return f"R$ {valor / 1_000:.2f}K"
    else:
        return f"R$ {valor:.2f}"
````
### 12. Exibição dos KPIs com cor
````

st.markdown("### 📈 Receita por Canal", help="Clique no menu lateral para navegar direto aqui")

col1, col2, col3, col4 = st.columns(4)

with col1:
    format_kpi("Receita Total", format_num(receita_total), "#0078D4")
with col2:
    format_kpi("Custo Total", format_num(custo_total), "#0078D4")
with col3:
    format_kpi("Margem de Lucro", format_num(margem_total), "#0078D4")
with col4:
    format_kpi("Qtd Vendida", f"{int(quantidade_total):,}", "#0078D4")

````    
### 13. Criar as abas
````
aba1, aba2, aba3, aba4, aba5, aba6, aba7 = st.tabs([
    "📈 Receita por Canal",
    "📍 Receita por Continente",
    "📊 Evolução Anual",
    "🥧 Participação dos Canais",
    "🗺️ Mapa de Receita por País",
    "📊 Evolução por Canal",
    "📦 Exportações"
])

````
### 14. Gráfico por Canal (aba 1)
````
with aba1:
    df_filtrado = df_filtrado.sort_values(by='Receita', ascending=False)

    fig_canal = px.bar(df_filtrado, 
                       x='Receita', 
                       y='ChannelName',
                       orientation='h',
                       color='ChannelName',
                       color_discrete_sequence=cores_personalizadas,
                       labels={'ChannelName': 'Canal de Vendas', 'Receita': 'Receita (R$)'},
                       title=f"📈 Receita por Canal - {ano_selecionado}",
                       category_orders={'ChannelName': df_filtrado['ChannelName'].tolist()})

    fig_canal.update_layout(
        showlegend=False,
        margin=dict(t=40),
        modebar=dict(remove=["zoom", "pan"], add=["toImage"])
    )

    st.plotly_chart(fig_canal, use_container_width=True)



````
### 15. Gráfico por Região (aba 2)
````

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
        modebar=dict(remove=["zoom", "pan"], add=["toImage"])
)

    st.plotly_chart(fig_regiao, use_container_width=True)

````
### 16. Evolução Anual (aba 3)
````

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
    modebar=dict(remove=["zoom", "pan"], add=["toImage"])
)

    st.plotly_chart(fig_ano, use_container_width=True)
    
````
### 17. Participação dos Canais (aba 4)
````

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
    modebar=dict(remove=["zoom", "pan"], add=["toImage"])
)

    st.plotly_chart(fig_pizza, use_container_width=True)

```` 
### 18. Gráfico de mapa com Plotly
````

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
    modebar=dict(remove=["zoom", "pan"], add=["toImage"])
)

    st.plotly_chart(fig_mapa, use_container_width=True)

````
### 19. Análise temporal: gráfico de linha com múltiplos canais
````

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
    modebar=dict(remove=["zoom", "pan"], add=["toImage"])
)


    st.plotly_chart(fig_temporal, use_container_width=True)
````  
### 20. 4. Exportação avançada: download de dados agregados
````

with aba7:
    df_agregado = df.groupby(['ChannelName', 'RegionCountryName'])[['Receita', 'Custo', 'MargemLucro']].sum().reset_index()

    st.download_button(
        label="📥 Baixar dados agregados",
        data=df_agregado.to_csv(index=False).encode('utf-8'),
        file_name='dados_agregados.csv',
        mime='text/csv'
)
