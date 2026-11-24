import streamlit as st

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


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

# Konfigurasi halaman
st.set_page_config(
    page_title="SPI Dashboard | Jabodetabek",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
st.title("SPI Dashboard")
st.markdown(
    """
    ### Monitoring Kekeringan Meteorologis di Jabodetabek

    Dashboard interaktif untuk mengeksplorasi kondisi kekeringan
    meteorologis berdasarkan Standardized Precipitation Index (SPI-3,
    SPI-6, dan SPI-12) menggunakan data historis CHIRPS periode 1981–2025.
    """
)

st.divider()

# Ringkasan informasi
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Periode Analisis", "1981–2025")

with col2:
    st.metric("Indeks Kekeringan", "3 Indeks")

with col3:
    st.metric("Wilayah Kajian", "Jabodetabek")

with col4:
    st.metric("Sumber Data", "CHIRPS")

st.divider()

# Deskripsi dashboard
st.subheader("Tentang Dashboard")

st.write(
    """
    Dashboard ini dikembangkan untuk memvisualisasikan dan menganalisis
    karakteristik kekeringan meteorologis di wilayah Jabodetabek.
    Analisis dilakukan menggunakan tiga skala waktu SPI, yaitu SPI-3,
    SPI-6, dan SPI-12.

    Pengguna dapat mengeksplorasi distribusi spasial, dinamika temporal,
    serta statistik kejadian kekeringan melalui halaman yang tersedia
    pada menu navigasi.
    """
)

st.info(
    "Silakan pilih halaman melalui menu navigasi di sebelah kiri "
    "untuk mulai mengeksplorasi hasil analisis."
)

st.caption(
    "SPI Dashboard | Jabodetabek | Historical Analysis 1981–2025"
)