import noisereduce as nr
import soundfile as sf
from pathlib import Path
from .audio_utils import load_audio


PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "results"

# Noise reduction strength
STRENGTH = {
    "low": 0.5,
    "medium": 0.8,
    "high": 1.0
}


def reduce_noise(input_file, strength="medium", stationary=False):

    if strength not in STRENGTH:
        raise ValueError("Choose low, medium, or high")

    audio, sample_rate = load_audio(input_file)

    cleaned_audio = nr.reduce_noise(
        y=audio,
        sr=sample_rate,
        stationary=stationary,
        prop_decrease=STRENGTH[strength]
    )

    output_file = OUTPUT_DIR / f"{Path(input_file).stem}_denoised.wav"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    sf.write(output_file, cleaned_audio, sample_rate)

    print(f"Processed: {Path(input_file).name}")
    print(f"Strength: {strength}")
    print(f"Noise type: {'Stationary' if stationary else 'Non-stationary'}")
    print(f"Output: {output_file}")
    return output_file


def main():

    audio_files = [
        file for file in INPUT_DIR.iterdir()
        if file.suffix.lower() in {".wav", ".mp3", ".flac"}
    ]

    if not audio_files:
        print("No supported audio files found in data folder.")
        return

    for audio_file in audio_files:
        reduce_noise(
            input_file=audio_file,
            strength="medium",
            stationary=False
        )


if __name__ == "__main__":
    main()
