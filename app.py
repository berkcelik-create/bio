import streamlit as st

# Sayfa ayarları
st.set_page_config(page_title="Berk Çelik | Bio", page_icon="🚀", layout="centered")

# CSS ile genel görünüm (Opsiyonel: Daha şık bir dokunuş için)
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 1. Başlık ve Kısa Tanıtım
st.title("Berk Çelik")
st.write("### 💻 Web Developer | 🎮 Gamer | 🎨 3D Modeler")
st.write("Teknoloji ve oyun dünyasını birleştiren projeler geliştiriyorum. İşte çalışmalarım ve bana ulaşabileceğin kanallar:")

st.divider()

# 2. Sosyal Linkler (Buton olarak)
st.subheader("Bana Ulaşın")
c1, c2, c3 = st.columns(3)

with c1:
    st.link_button("GitHub", "https://github.com/KULLANICI_ADIN")
with c2:
    st.link_button("LinkedIn", "https://linkedin.com/in/KULLANICI_ADIN")
with c3:
    st.link_button("Discord", "https://discord.gg/DAVET_LINKIN")

st.divider()

# 3. Projeler Bölümü
st.header("Projelerim")

# G-ENGINE Projesi
with st.container(border=True):
    st.subheader("G-ENGINE")
    st.write("Donanım arama motoru ve fiyat takip uygulaması.")
    st.link_button("Projeye Git", "https://github.com/KULLANICI_ADIN/G-ENGINE")

# Başka projelerin varsa buraya kopyala-yapıştır yapabilirsin
with st.container(border=True):
    st.subheader("Diğer Projem")
    st.write("Buraya başka bir projenin kısa açıklaması gelecek.")
    st.link_button("Detayları Gör", "https://github.com/KULLANICI_ADIN/proje-linki")

st.divider()

# 4. Footer
st.caption("© 2026 Berk Çelik - Streamlit ile hazırlandı.")
