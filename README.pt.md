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
