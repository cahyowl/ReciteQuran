import random
import urllib.parse
import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="ReciteQuran", layout="centered")  # Must be first Streamlit command[2]

# --- App Header ---
st.title("📖 ReciteQuran")
st.write("Bored? Stuck and feeling weary? Perhaps Allah is calling you to embrace the Quran today. Have you?")

# --- Surah List ---
surahs = [
    "Al-Fatihah", "Al-Baqarah", "Al-'Imran", "An-Nisa'", "Al-Ma'idah",
    "Al-An'am", "Al-A'raf", "Al-Anfal", "At-Tawbah", "Yunus",
    "Hud", "Yusuf", "Ar-Ra'd", "Ibrahim", "Al-Hijr",
    "An-Nahl", "Al-Isra'", "Al-Kahf", "Maryam", "Ta-Ha",
    "Al-Anbiya'", "Al-Hajj", "Al-Mu'minun", "An-Nur", "Al-Furqan",
    "Ash-Shu'ara'", "An-Naml", "Al-Qasas", "Al-'Ankabut", "Ar-Rum",
    "Luqman", "As-Sajdah", "Al-Ahzab", "Saba'", "Fatir",
    "Ya-Sin", "As-Saffat", "Sad", "Az-Zumar", "Ghafir",
    "Fussilat", "Ash-Shura", "Az-Zukhruf", "Ad-Dukhan", "Al-Jathiyah",
    "Al-Ahqaf", "Muhammad", "Al-Fath", "Al-Hujurat", "Qaf",
    "Adh-Dhariyat", "At-Tur", "An-Najm", "Al-Qamar", "Ar-Rahman",
    "Al-Waqi'ah", "Al-Hadid", "Al-Mujadila", "Al-Hashr", "Al-Mumtahanah",
    "As-Saff", "Al-Jumu'ah", "Al-Munafiqun", "At-Taghabun", "At-Talaq",
    "At-Tahrim", "Al-Mulk", "Al-Qalam", "Al-Haqqah", "Al-Ma'arij",
    "Nuh", "Al-Jinn", "Al-Muzzammil", "Al-Muddaththir", "Al-Qiyamah",
    "Al-Insan", "Al-Mursalat", "An-Naba'", "An-Nazi'at", "'Abasa",
    "At-Takwir", "Al-Infitar", "Al-Mutaffifin", "Al-Inshiqaq", "Al-Buruj",
    "At-Tariq", "Al-A'la", "Al-Ghashiyah", "Al-Fajr", "Al-Balad",
    "Ash-Shams", "Al-Layl", "Ad-Duha", "Ash-Sharh", "At-Tin",
    "Al-'Alaq", "Al-Qadr", "Al-Bayyinah", "Az-Zalzalah", "Al-Adiyat",
    "Al-Qari'ah", "At-Takathur", "Al-'Asr", "Al-Humazah", "Al-Fil",
    "Quraysh", "Al-Ma'un", "Al-Kawthar", "Al-Kafirun", "An-Nasr",
    "Al-Masad", "Ikhlas", "Al-Falaq", "An-Nas"
]

def format_slug(name: str) -> str:
    """Convert a Surah name into a URL-friendly slug."""
    slug = name.lower().replace("'", "").replace("’", "")
    return urllib.parse.quote(slug)

# --- Button Interaction ---
if st.button("Your Today's Surah"):
    surah = random.choice(surahs)
    slug = format_slug(surah)

    youtube_url = f"https://www.youtube.com/results?search_query=surah+{slug}+recitation"
    quran_url = f"https://quran.com/{slug}"

    st.subheader(f"Surah to Read Today: {surah}")
    st.markdown(f"- [📺 Watch Recitation on YouTube]({youtube_url})")
    st.markdown(f"- [📖 Read Full Text on Quran.com]({quran_url})")

