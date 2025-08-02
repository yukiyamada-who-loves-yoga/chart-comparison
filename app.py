# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Chart Types Reference",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Chart Types Reference")
st.markdown("A comprehensive reference showing different types of charts and graphs")

# Chart reference table
st.header("Chart Types Reference Table")
chart_data = {
    "Japanese": [
        "円グラフ", "折れ線グラフ", "棒グラフ", "面グラフ", "帯グラフ", 
        "ヒストグラム", "バブルチャート", "レーダーチャート", "等高線グラフ", 
        "ドーナツグラフ", "散布図", "ベン図", "表", "図", "写真", "資料"
    ],
    "English": [
        "pie chart", "line chart", "bar chart", "area chart", "horizontal bar chart",
        "histogram", "bubble chart", "radar chart", "contour chart",
        "doughnut chart", "scatter diagram", "venn diagram", "table / chart", 
        "figure / chart", "picture", "data"
    ]
}

df_reference = pd.DataFrame(chart_data)
st.dataframe(df_reference, use_container_width=True)

# Sample data for charts
np.random.seed(42)

# Data for categorical charts (pie, bar, etc.)
categorical_data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [23, 45, 56, 78, 32]
})

# Data for scatter plots, bubble charts, etc.
scatter_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'size': np.random.randint(10, 100, 100),
    'color': np.random.choice(['red', 'blue', 'green', 'orange'], 100)
})

time_series_data = pd.DataFrame({
    'date': pd.date_range('2023-01-01', periods=50, freq='D'),
    'value': np.cumsum(np.random.randn(50)) + 100,
    'category': np.random.choice(['Series A', 'Series B'], 50)
})

# Create chart examples
st.header("Chart Examples")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Pie Chart (円グラフ)")
    fig_pie = px.pie(categorical_data, values='value', names='category', title="Sample Pie Chart")
    fig_pie.update_layout(plot_bgcolor='#FAFAFA', paper_bgcolor='#FAFAFA')
    st.plotly_chart(fig_pie, use_container_width=True)

    st.subheader("Line Chart (折れ線グラフ)")
    fig_line = px.line(time_series_data, x='date', y='value', color='category', title="Sample Line Chart")
    fig_line.update_layout(plot_bgcolor='#FAFAFA', paper_bgcolor='#FAFAFA')
    st.plotly_chart(fig_line, use_container_width=True)

    st.subheader("Bar Chart (棒グラフ)")
    fig_bar = px.bar(categorical_data, x='category', y='value', title="Sample Bar Chart")
    fig_bar.update_layout(plot_bgcolor='#FAFAFA', paper_bgcolor='#FAFAFA')
    st.plotly_chart(fig_bar, use_container_width=True)

    st.subheader("Area Chart (面グラフ)")
    fig_area = px.area(time_series_data, x='date', y='value', color='category', title="Sample Area Chart")
    fig_area.update_layout(plot_bgcolor='#FAFAFA', paper_bgcolor='#FAFAFA')
    st.plotly_chart(fig_area, use_container_width=True)

    st.subheader("Horizontal Bar Chart (帯グラフ)")
    fig_hbar = px.bar(categorical_data, x='value', y='category', orientation='h', title="Sample Horizontal Bar Chart")
    fig_hbar.update_layout(plot_bgcolor='#FAFAFA', paper_bgcolor='#FAFAFA')
    st.plotly_chart(fig_hbar, use_container_width=True)

with col2:
    st.subheader("Histogram (ヒストグラム)")
    fig_hist = px.histogram(scatter_data, x='x', nbins=20, title="Sample Histogram")
    fig_hist.update_layout(plot_bgcolor='#FAFAFA', paper_bgcolor='#FAFAFA')
    st.plotly_chart(fig_hist, use_container_width=True)

    st.subheader("Bubble Chart (バブルチャート)")
    bubble_data = scatter_data.head(20).copy()
    fig_bubble = px.scatter(bubble_data, x='x', y='y', size='size', color='color', 
                           title="Sample Bubble Chart", size_max=60)
    fig_bubble.update_layout(plot_bgcolor='#FAFAFA', paper_bgcolor='#FAFAFA')
    st.plotly_chart(fig_bubble, use_container_width=True)

    st.subheader("Scatter Plot (散布図)")
    fig_scatter = px.scatter(scatter_data, x='x', y='y', color='color', title="Sample Scatter Plot")
    fig_scatter.update_layout(plot_bgcolor='#FAFAFA', paper_bgcolor='#FAFAFA')
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader("Doughnut Chart (ドーナツグラフ)")
    fig_donut = go.Figure(data=[go.Pie(labels=categorical_data['category'], values=categorical_data['value'], hole=.3)])
    fig_donut.update_layout(title_text="Sample Doughnut Chart", plot_bgcolor='#FAFAFA', paper_bgcolor='#FAFAFA')
    st.plotly_chart(fig_donut, use_container_width=True)

    st.subheader("Radar Chart (レーダーチャート)")
    categories = ['A', 'B', 'C', 'D', 'E']
    values1 = [4, 3, 2, 4, 5]
    values2 = [3, 4, 4, 2, 3]
    
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=values1 + [values1[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name='Series 1'
    ))
    fig_radar.add_trace(go.Scatterpolar(
        r=values2 + [values2[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name='Series 2'
    ))
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )),
        title="Sample Radar Chart",
        plot_bgcolor='#FAFAFA',
        paper_bgcolor='#FAFAFA'
    )
    st.plotly_chart(fig_radar, use_container_width=True)

# Contour chart
st.subheader("Contour Chart (等高線グラフ)")
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

fig_contour = go.Figure(data=go.Contour(z=Z, x=x, y=y))
fig_contour.update_layout(title="Sample Contour Chart", plot_bgcolor='#FAFAFA', paper_bgcolor='#FAFAFA')
st.plotly_chart(fig_contour, use_container_width=True)

# Additional information
st.header("Additional Chart Information")
st.markdown("""
**Note**: Some chart types like Venn diagrams require specialized libraries and are not commonly used in standard data visualization libraries. The charts above represent the most commonly used types in data analysis and business intelligence.

**Libraries used in this example**:
- Plotly Express & Plotly Graph Objects for interactive charts
- Streamlit for the web interface
- Pandas & NumPy for data manipulation
""")

if st.button("Generate New Sample Data"):
    st.rerun()