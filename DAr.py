import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Centre de Contacts — Tableau de bord",
    page_icon="📞",
    layout="wide"
)

st.markdown("""
<style>
    .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
    .metric-label { font-size: 13px; }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("centre_contacts_data.csv", parse_dates=["date"])
    df["mois"] = df["date"].dt.to_period("M").astype(str)
    df["semaine"] = df["date"].dt.to_period("W").astype(str)
    df["duree_min"] = (df["duree_secondes"] / 60).round(1)
    return df

df = load_data()

# ── Sidebar filters ──────────────────────────────────────────────────────────
st.sidebar.header("Filtres")

canaux = st.sidebar.multiselect(
    "Canal",
    options=df["canal"].unique().tolist(),
    default=df["canal"].unique().tolist()
)

motifs = st.sidebar.multiselect(
    "Motif de contact",
    options=df["motif"].unique().tolist(),
    default=df["motif"].unique().tolist()
)

date_min = df["date"].min().date()
date_max = df["date"].max().date()
date_range = st.sidebar.date_input(
    "Période",
    value=(date_min, date_max),
    min_value=date_min,
    max_value=date_max
)

df_f = df[
    df["canal"].isin(canaux) &
    df["motif"].isin(motifs) &
    (df["date"].dt.date >= date_range[0]) &
    (df["date"].dt.date <= date_range[1])
]

# ── Header ───────────────────────────────────────────────────────────────────
st.title("📞 Tableau de bord — Centre de Contacts")
st.caption("Analyse de la performance opérationnelle · Données 2024")
st.divider()

# ── KPI row ──────────────────────────────────────────────────────────────────
total = len(df_f)
taux_resolution = round(len(df_f[df_f["statut"] == "Résolu"]) / total * 100, 1) if total else 0
duree_moy = round(df_f["duree_min"].mean(), 1) if total else 0
satisfaction_moy = round(df_f["satisfaction"].mean(), 2) if total else 0

k1, k2, k3, k4 = st.columns(4)
k1.metric("Contacts traités", f"{total:,}".replace(",", " "))
k2.metric("Taux de résolution", f"{taux_resolution} %")
k3.metric("Durée moyenne", f"{duree_moy} min")
k4.metric("Satisfaction moyenne", f"{satisfaction_moy} / 5")

st.divider()

# ── Row 1 : volume & résolution ───────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("Volume de contacts par mois")
    vol = df_f.groupby("mois").size().reset_index(name="contacts")
    fig = px.bar(vol, x="mois", y="contacts", color_discrete_sequence=["#378ADD"])
    fig.update_layout(xaxis_title="", yaxis_title="Contacts", margin=dict(t=10, b=0))
    fig.update_xaxes(tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Répartition par canal")
    canal_count = df_f["canal"].value_counts().reset_index()
    canal_count.columns = ["Canal", "Contacts"]
    fig2 = px.pie(canal_count, values="Contacts", names="Canal",
                  color_discrete_sequence=["#378ADD", "#1D9E75", "#EF9F27", "#D4537E"],
                  hole=0.4)
    fig2.update_layout(margin=dict(t=10, b=0))
    st.plotly_chart(fig2, use_container_width=True)

# ── Row 2 : satisfaction & motifs ─────────────────────────────────────────────
col3, col4 = st.columns(2)

with col3:
    st.subheader("Satisfaction par motif de contact")
    sat_motif = df_f.groupby("motif")["satisfaction"].mean().reset_index()
    sat_motif.columns = ["Motif", "Satisfaction"]
    sat_motif = sat_motif.sort_values("Satisfaction")
    fig3 = px.bar(sat_motif, x="Satisfaction", y="Motif", orientation="h",
                  color="Satisfaction",
                  color_continuous_scale=["#E24B4A", "#EF9F27", "#1D9E75"],
                  range_color=[1, 5])
    fig3.update_layout(margin=dict(t=10, b=0), coloraxis_showscale=False)
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("Taux de résolution par agent")
    agent_stats = df_f.groupby("agent").apply(
        lambda x: round(len(x[x["statut"] == "Résolu"]) / len(x) * 100, 1)
    ).reset_index()
    agent_stats.columns = ["Agent", "Taux résolution (%)"]
    agent_stats = agent_stats.sort_values("Taux résolution (%)", ascending=False)
    fig4 = px.bar(agent_stats, x="Agent", y="Taux résolution (%)",
                  color_discrete_sequence=["#1D9E75"])
    fig4.update_layout(margin=dict(t=10, b=0), yaxis_range=[0, 100])
    st.plotly_chart(fig4, use_container_width=True)

# ── Row 3 : durée par canal ───────────────────────────────────────────────────
st.subheader("Durée moyenne de traitement par canal (minutes)")
duree_canal = df_f.groupby("canal")["duree_min"].mean().reset_index()
duree_canal.columns = ["Canal", "Durée moyenne (min)"]
duree_canal["Durée moyenne (min)"] = duree_canal["Durée moyenne (min)"].round(1)
fig5 = px.bar(duree_canal, x="Canal", y="Durée moyenne (min)",
              color_discrete_sequence=["#EF9F27"])
fig5.update_layout(margin=dict(t=10, b=40))
st.plotly_chart(fig5, use_container_width=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Dashboard réalisé avec Python · Streamlit · Plotly — Yasmine-Coraline Kana Ngangom")
