import streamlit as st

# Sayfa ayarları
st.set_page_config(page_title="Berk Çelik | Bio", page_icon="🚀")

# Profil Bölümü (Fotoğraf kaldırıldı)
st.title("Berk Çelik")
st.write("### Web Developer | 3D Modeler | Gamer")
st.write("Teknoloji ve oyun dünyasını birleştiren projeler geliştiriyorum.")

st.divider()

# Sosyal Linkler
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
        st.write("Proje detayları buraya eklenecek.")
