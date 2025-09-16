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

)
