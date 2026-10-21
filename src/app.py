import streamlit as st
import pandas as pd
import json
from pathlib import Path

st.set_page_config(page_title="Analiza Rynku Pracy", layout="wide")

st.title("Dashboard: Analiza Ofert Pracy")
st.markdown("Ten dashboard prezentuje aktualne dane z rynku pracy na podstawie pobranych i oczyszczonych ofert.")

@st.cache_data
def load_serving_data(filename):
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / "data" / "serving" / filename
    try:
        return pd.read_json(file_path)
    except Exception:
        return pd.DataFrame()

df_offers = load_serving_data("serving_job_offers.json")
df_locations = load_serving_data("serving_location_stats.json")
df_tags = load_serving_data("serving_tags_summary.json")
df_job_types = load_serving_data("serving_job_types_summary.json")

if df_offers.empty:
    st.warning("Brak danych w warstwie serving. Uruchom najpierw build_serving_data.py")
    st.stop()

st.sidebar.header("Filtry")

locations = df_offers['location'].dropna().unique().tolist()
selected_location = st.sidebar.multiselect("Wybierz lokalizację", options=locations, default=locations[:10])

df_filtered = df_offers[df_offers['location'].isin(selected_location)]

st.subheader("Kluczowe wskaźniki")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Liczba ofert", value=len(df_filtered))

with col2:
    st.metric(label="Liczba unikalnych firm", value=df_filtered['company_name'].nunique())

with col3:
    remote_count = len(df_filtered[df_filtered['remote'] == True])
    remote_pct = (remote_count / len(df_filtered) * 100) if len(df_filtered) > 0 else 0
    st.metric(label="Oferty w 100% zdalne", value=f"{remote_count} ({remote_pct:.1f}%)")

st.divider()

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Top 10 Lokalizacji (Ogółem)")
    if not df_locations.empty:
        st.bar_chart(df_locations.set_index('location').head(10))

with col_chart2:
    st.subheader("Najczęstsze typy umów (Ogółem)")
    if not df_job_types.empty:
        st.bar_chart(df_job_types.set_index('job_type').head(10))

st.subheader("Popularne Tagi (Ogółem)")
if not df_tags.empty:
    st.bar_chart(df_tags.set_index('tag').head(15))

st.subheader("Tabela ofert")
st.dataframe(df_filtered, use_container_width=True)