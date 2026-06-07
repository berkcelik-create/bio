import streamlit as st

# Sayfa ayarları
st.set_page_config(page_title="Berk Çelik | Bio", page_icon="🚀")

# CSS ile özelleştirme (Dark Mode ve Şık Tasarım)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Profil Bölümü
col1, col2 = st.columns([1, 2])
with col1:
    st.image("profil.png", width=200) # Kendi fotoğrafın
with col2:
    st.title("Berk Çelik")
    st.write("### Web Developer | 3D Modeler | Gamer")
    st.write("Teknoloji ve oyun dünyasını birleştiren projeler geliştiriyorum.")

st.divider()

# Sosyal Linkler / İletişim
st.subheader("Bana Ulaşın")
c1, c2, c3 = st.columns(3)
with c1: st.link_button("GitHub", "https://github.com/kullanici-adin")
with c2: st.link_button("LinkedIn", "https://linkedin.com/in/kullanici-adin")
with c3: st.link_button("Discord", "https://discord.gg/...")

st.divider()

# Projelerim
st.header("Projelerim")
with st.container(border=True):
    st.subheader("G-ENGINE")
    st.write("Hardware takip ve arama motoru projem.")
    if st.button("Detayları Gör"):
        st.write("Proje linki veya açıklaması burada açılabilir.")
