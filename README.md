# Projeto de Integração SQL/Python

# Sales Dashboard — ContosoRetailDW

This project is an interactive dashboard built with **Streamlit** and **Plotly**, integrating data from the **ContosoRetailDW** SQL Server database via **PyODBC**. The goal is to deliver a clean, responsive, browser-based experience for exploring key sales metrics across channels, regions, and time.

---

## Purpose

To create a visual interface that allows users to:

- Filter data by year, sales channel, and region  
- Navigate between sections using tabs  
- View KPIs and interactive charts with export options  
- Explore insights by continent, country, and sales channel

---

## Libraries Used

| Library            | Purpose                                               |
|--------------------|-------------------------------------------------------|
| `streamlit`        | Web interface and layout                              |
| `plotly.express`   | Interactive and exportable charts                     |
| `pandas`           | Data manipulation                                     |
| `pyodbc`           | SQL Server connection to ContosoRetailDW              |

---

## Visual Design Choices

- **Custom Contoso Palette**: corporate tones with adjusted contrast to avoid similar blues  
- **Horizontal bar charts**: improve readability and highlight top performers  
- **Soft-toned KPIs**: reinforce visual identity without overwhelming the layout  
- **Export mode enabled**: all charts include a download-as-image button

 ![Dashboard](https://github.com/user-attachments/assets/03bb3004-aa85-4272-8a6e-5c372d258d63) 
 ![Dashboard](https://github.com/user-attachments/assets/679de1e3-b1ff-408f-aeb0-04c240736c8f) 

---

## Navigation

The dashboard is organized into thematic tabs:

-  Revenue by Channel  
-  Revenue by Continent  
-  Yearly Trends  
-  Channel Share  
-  Revenue Map by Country  
-  Export Data  

Each tab presents targeted visualizations with applicable filters, making the experience smooth and intuitive.

---

## Key Learnings

This project was a hands-on discovery of **Streamlit** and **Plotly**, showcasing how data can be transformed into a visual experience — all within the browser, without complex front-end frameworks.

---

## Project Structure

- `app.py`: main dashboard script  
- `requirements.txt`: project dependencies  
- `README.md`: documentation and context

---

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
````
## Launch the Dashboard

[ Open Dashboard on Browser](http://localhost:8501)

----
## Outcome
A lightweight, visually appealing, and functional application — perfect for executive presentations, internal analytics, or as a foundation for larger BI initiatives.
````


