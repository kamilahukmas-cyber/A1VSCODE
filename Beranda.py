import streamlit as st

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Jabodetabek Drought Monitor",
    layout="wide"
)

# HEADER
st.title("Jabodetabek Drought Monitor")
st.markdown(
    "### Meteorological Drought Analysis"
)
st.caption(
    "Standardized Precipitation Index (SPI) | CHIRPS"
)

st.divider()

# SIDEBAR
st.sidebar.title("Analysis Options")

spi_type = st.sidebar.selectbox(
    "Select SPI Indicator",
    ["SPI-3", "SPI-6", "SPI-12"]
)

year = st.sidebar.selectbox(
    "Select Year",
    list(range(1981, 2026)),
    index=44
)

# OVERVIEW
st.subheader("Drought Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Selected Indicator", spi_type)
col2.metric("Selected Year", year)
col3.metric("Study Area", "Jabodetabek")

st.divider()

# MAP SECTION
st.subheader("Spatial Distribution of SPI")

st.info(
    "Peta SPI akan ditampilkan setelah data hasil "
    "perhitungan SPI diimpor ke dalam dashboard."
)

# CHART SECTION
st.subheader("SPI Time Series")

st.info(
    "Grafik deret waktu akan tersedia setelah "
    "data historis SPI selesai diolah."
)

st.divider()

st.caption(
    "Jabodetabek Drought Monitor | Data source: CHIRPS"
)
