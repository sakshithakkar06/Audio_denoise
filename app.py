
import streamlit as st
from pathlib import Path

from src.denoise import reduce_noise

PROJECT_DIR = Path(__file__).resolve().parent
INPUT_DIR = PROJECT_DIR / "data"

st.set_page_config(page_title="Speech Noise Reducer", page_icon="🎧")

st.title("🎧 Speech Noise Reducer")
st.write("Remove background noise from your audio recordings.")

uploaded_file = st.file_uploader(
    "Upload audio",
    type=["wav", "mp3", "flac"]
)

strength = st.select_slider(
    "Noise reduction strength",
    options=["low", "medium", "high"],
    value="medium"
)

noise_type = st.selectbox(
    "Noise type",
    ["Non-stationary", "Stationary"]
)

if uploaded_file:
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    input_path = INPUT_DIR / uploaded_file.name
    input_path.write_bytes(uploaded_file.getvalue())

    st.subheader("Original Audio")
    st.audio(str(input_path))

    if st.button("Reduce Noise", type="primary"):
        with st.spinner("Reducing background noise..."):
            output_path = reduce_noise(
                input_file=input_path,
                strength=strength,
                stationary=(noise_type == "Stationary")
            )

        st.success("Noise reduction complete!")

        st.subheader("Enhanced Audio")
        st.audio(str(output_path))

        with open(output_path, "rb") as audio_file:
            st.download_button(
                "Download Cleaned Audio",
                data=audio_file,
                file_name=output_path.name,
                mime="audio/wav"
            )
