import numpy as np
import pandas as pd
import plotly.express as px

np.random.seed(42)
data = {
    "x": np.arange(10),
    "y": np.random.randint(1, 100, 10)
}
df = pd.DataFrame(data)

fig = px.bar(df, x="x", y="y", title="Interactive Bar Chart", labels={"x": "X-Axis", "y": "Y-Axis"})
fig.update_layout(hovermode="x unified", dragmode="zoom")
fig.show()

def create_figure(chart_type="bar"):
    if chart_type == "bar":
        fig = px.bar(df, x="x", y="y", title="Bar Chart", labels={"x": "X-Axis", "y": "Y-Axis"})
    elif chart_type == "scatter":
        fig = px.scatter(df, x="x", y="y", title="Scatter Plot", labels={"x": "X-Axis", "y": "Y-Axis"})
    fig.update_layout(hovermode="x unified", dragmode="zoom")
    return fig

fig.update_traces(hovertemplate="X: %{x}<br>Y: %{y}")

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import plotly.io as pio

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def render_chart(chart_type: str = "bar"):
    fig = create_figure(chart_type)
    html = pio.to_html(fig, full_html=False)
    return html
