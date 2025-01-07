# Interactive Data Visualization with Plotly and FastAPI

## Project Overview
This project demonstrates how to create an interactive data visualization using Plotly and integrate it with a FastAPI backend. The interactive visualizations include dropdown menus, tooltips, and zooming capabilities, providing a dynamic way to explore data. The app is set up to run locally using FastAPI and can be extended for deployment to platforms like Vercel.

---

## Why I Created This Project
1. **Learn Data Visualization**: To understand how to use Plotly for creating visually appealing and interactive charts.
2. **Integrate with FastAPI**: To practice combining Python backends with frontend visualizations.
3. **Build Deployable Apps**: To create a project that can easily be deployed and scaled.
4. **Extend to Other Projects**: To apply interactive data visualization concepts in future projects.

---

## What I Learned
- How to use Plotly to create interactive charts.
- Setting up a FastAPI backend to serve dynamic content.
- Adding interactivity to visualizations with dropdowns and tooltips.
- Structuring a project for local development and potential deployment.

---

## How the Code Works

### **1. Dataset Preparation**
A simple dataset is generated with random data to serve as input for the visualization.

```python
import numpy as np
import pandas as pd

np.random.seed(42)
data = {
    "x": np.arange(10),
    "y": np.random.randint(1, 100, 10)
}
df = pd.DataFrame(data)
```
- **`np.random.seed(42)`** ensures reproducibility.
- The DataFrame contains `x` and `y` columns, where `x` represents labels and `y` represents corresponding values.

---

### **2. Visualization with Plotly**
A bar chart is created using Plotly Express, with dropdowns and tooltips for interactivity.

```python
import plotly.express as px
from fastapi.responses import JSONResponse

fig = px.bar(df, x="x", y="y", title="Interactive Bar Chart", labels={"x": "Index", "y": "Value"})
fig.update_layout(
    xaxis=dict(title="X-Axis", tickangle=-45),
    yaxis=dict(title="Y-Axis"),
    showlegend=False
)
fig.update_traces(marker_color="blue", hovertemplate="<b>X:</b> %{x}<br><b>Y:</b> %{y}<extra></extra>")
```
- **`update_layout`** adjusts chart titles and axis labels.
- **`update_traces`** sets tooltip formatting and marker colors.

---

### **3. FastAPI Integration**
The visualization is served through a FastAPI endpoint as an interactive webpage.

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return fig.to_html()
```
- The **`home`** endpoint renders the Plotly chart as an HTML page.
- The `to_html` method converts the Plotly figure into an embeddable HTML format.

---

### **4. Running the App**
The app runs locally using Uvicorn:

```bash
uvicorn main:app --reload
```
- **`main:app`** specifies the file (`main.py`) and the FastAPI app object (`app`).
- **`--reload`** enables live reloading for development.

---

## Future Improvements
- Add more data and advanced visualizations (e.g., scatter plots, line charts).
- Implement filters for selecting data ranges.
- Deploy the app to platforms like Vercel for wider access.

---

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd interactive-visualization
   ```
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn plotly pandas numpy
   ```
4. Run the FastAPI app:
   ```bash
   uvicorn main:app --reload
   ```
5. Open the browser and visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the interactive chart.

---

## Conclusion
This project showcases how to build an interactive data visualization with Plotly and serve it through a FastAPI backend. The integration of dynamic charts and dropdowns makes it suitable for use in data exploration and reporting tools. By combining Plotly's rich visualization capabilities with FastAPI's lightweight framework, this project serves as a foundation for building scalable and interactive applications.
