
import soundfile as sf
import librosa
import numpy as np
from pathlib import Path


SUPPORTED_FORMATS = {".wav", ".mp3", ".flac"}


def load_audio(file_path):
    file_path = Path(file_path)

    if file_path.suffix.lower() not in SUPPORTED_FORMATS:
        raise ValueError("Unsupported audio format")

    audio, sample_rate = librosa.load(
        file_path,
        sr=None,
        mono=True
    )

    return audio, sample_rate
