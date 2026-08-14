import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="HSE Safety Dashboard", layout="wide")

# DATA LOADING

@st.cache_data
def load_data():
    # In a real scenario, use: return pd.read_csv("your_hse_data.csv")
    # Generating dummy HSE data for demonstration:
    np.random.seed(42)
    dates = [datetime.now() - timedelta(days=x) for x in range(100)]
    sites = ['Refinery A', 'Plant B', 'Warehouse C', 'Offshore Rig D']
    incident_types = ['Near Miss', 'First Aid', 'Lost Time Injury (LTI)', 'Medical Treatment']
    
    data = pd.DataFrame({
        'Date': pd.to_datetime(dates),
        'Site': np.random.choice(sites, 100),
        'Incident_Type': np.random.choice(incident_types, 100),
        'Severity': np.random.randint(1, 11, 100),  # 1-10 scale
        'Is_Critical': np.random.choice([True, False], 100, p=[0.1, 0.9]),
        'latitude': np.random.uniform(-1.2, -1.3, 100),
        'longitude': np.random.uniform(36.7, 36.9, 100)
    })
    return data

df = load_data()

# SIDEBAR CONTROLS
st.sidebar.header("Dashboard Filters")

# Site Filter
selected_sites = st.sidebar.multiselect(
    "Select Site/Location", 
    options=df['Site'].unique(), 
    default=df['Site'].unique()
)

# Date Range Filter
min_date = df['Date'].min().to_pydatetime()
max_date = df['Date'].max().to_pydatetime()
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Incident Type Filter
selected_types = st.sidebar.multiselect(
    "Incident Type",
    options=df['Incident_Type'].unique(),
    default=df['Incident_Type'].unique()
)

# INTERACTIVITY: Apply Filters
# Check if date_range has both start and end to avoid errors during selection
if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
    mask = (
        df['Site'].isin(selected_sites) & 
        df['Incident_Type'].isin(selected_types) & 
        (df['Date'].dt.date >= start_date) & 
        (df['Date'].dt.date <= end_date)
    )
    filtered_df = df.loc[mask]
else:
    filtered_df = df # Fallback

# ALERTING LOGIC

critical_count = filtered_df['Is_Critical'].sum()
CRITICAL_THRESHOLD = 5

st.title("🛡️ HSE Safety Performance Dashboard")

if critical_count > CRITICAL_THRESHOLD:
    st.warning(f"🚨 ALERT: High risk detected! There are {critical_count} critical incidents in the selected period.")


# KPI METRICS

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_incidents = len(filtered_df)
    st.metric("Total Incidents", total_incidents, delta="-2% (vs last month)")

with col2:
    avg_severity = round(filtered_df['Severity'].mean(), 1) if not filtered_df.empty else 0
    # Logic: Higher severity is bad (red)
    st.metric("Avg Severity Score", avg_severity, delta="Increasing", delta_color="inverse")

with col3:
    st.metric("Critical Incidents", critical_count, delta=f"{critical_count} active", delta_color="off")

with col4:
    # EXPORT DATA
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Export Filtered Data",
        data=csv,
        file_name='filtered_safety_data.csv',
        mime='text/csv',
    )

st.markdown("---")

# VISUALIZATIONS

row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("Incident Trends Over Time")
    # Resample to daily counts
    trend_df = filtered_df.resample('D', on='Date').size().reset_index(name='Counts')
    fig_line = px.line(trend_df, x='Date', y='Counts', title="Daily Incident Count")
    st.plotly_chart(fig_line, use_container_width=True)

with row1_col2:
    st.subheader("Breakdown by Incident Type")
    fig_pie = px.pie(filtered_df, names='Incident_Type', hole=0.4, 
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_pie, use_container_width=True)

row2_col1, row2_col2 = st.columns([2, 1])

with row2_col1:
    st.subheader("Geospatial Incident Mapping")
    # Map view using the Lat/Lon data
    if not filtered_df.empty:
        st.map(filtered_df)
    else:
        st.write("No location data available for current filters.")

with row2_col2:
    st.subheader("Site Severity Analysis")
    fig_bar = px.bar(
        filtered_df.groupby('Site')['Severity'].mean().reset_index(),
        x='Site', y='Severity', color='Site',
        title="Avg Severity per Site"
    )
    st.plotly_chart(fig_bar, use_container_width=True)