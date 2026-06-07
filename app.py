import streamlit as st
from streamlit_extras.mention import mention
import os

# Sayfa Yapılandırması
st.set_page_config(page_title="Berk Çelik | Portfolio", layout="centered")

# --- ZİYARETÇİ SAYACI ---
COUNTER_FILE = "counter.txt"
def update_counter():
    if not os.path.exists(COUNTER_FILE):
        count = 1
    else:
        with open(COUNTER_FILE, "r") as f:
            count = int(f.read()) + 1
    with open(COUNTER_FILE, "w") as f:
        f.write(str(count))
    return count

visitor_count = update_counter()

# --- VERİ VE STİL ---
PROJECTS = [
    {"title": "G-ENGINE", "desc": "Donanım arama motoru ve fiyat takip uygulaması.", "link": "https://github.com/KULLANICI_ADIN/G-ENGINE"},
]

st.markdown("""
    <style>
    .big-font { font-size:40px !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="big-font">Berk Çelik</p>', unsafe_allow_html=True)
st.write("### Web Developer | Gamer | 3D Modeler")

# --- SOSYAL ---
col1, col2 = st.columns([1, 5])
with col1:
    mention(label="GitHub", icon="github", url="https://github.com/KULLANICI_ADIN")

st.divider()

# --- PROJELER ---
st.subheader("🚀 Öne Çıkan Projeler")
for project in PROJECTS:
    with st.container(border=True):
        st.write(f"### {project['title']}")
        st.write(project['desc'])
        st.link_button("Projeye Git", project['link'])

st.divider()

# --- İLETİŞİM FORMU (Formspree ile) ---
# Formspree, kod yazmadan e-posta almanı sağlar. 
# https://formspree.io/ üzerinden ücretsiz hesap açıp bir "Endpoint" almalısın.
st.subheader("📩 İletişim")
contact_form = """
<form action="https://formspree.io/f/KENDI_FORM_ID_BURAYA" method="POST">
    <input type="hidden" name="_subject" value="Yeni mesaj!">
    <input type="email" name="email" placeholder="E-posta adresin" required style="width:100%; padding:10px; margin-bottom:10px;">
    <textarea name="message" placeholder="Mesajın" required style="width:100%; padding:10px;"></textarea>
    <button type="submit" style="width:100%; padding:10px; background-color:#ff4b4b; color:white; border:none; border-radius:5px;">Gönder</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# --- FOOTER & SAYAÇ ---
st.divider()
st.caption(f"Bu site {visitor_count} kez görüntülendi.")
