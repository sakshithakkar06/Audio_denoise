# 🎧 Speech Noise Reducer

A Python-based audio enhancement application that reduces background noise from speech recordings while retaining speech clarity. The application uses spectral gating for noise reduction and provides an interactive interface built with Streamlit.

## 📌 Overview

Background noise can affect speech clarity and make audio recordings difficult to understand. Speech noise reduction techniques help suppress unwanted sounds while preserving the important speech components.

This project implements an offline speech enhancement application that allows users to upload audio recordings, configure noise reduction settings, and listen to the processed output.

## ✨ Features

- **Multiple Audio Formats:** Supports WAV, MP3, and FLAC files.
- **Configurable Noise Reduction:** Choose between Low, Medium, and High reduction strengths.
- **Noise Type Selection:** Supports stationary and non-stationary noise reduction.
- **Audio Preview:** Listen to the original recording before processing.
- **Enhanced Audio Playback:** Compare the processed output with the original recording.
- **Download Output:** Download the noise-reduced audio in WAV format.

## 🖥️ User Interface

<img width="393" height="441" alt="image" src="https://github.com/user-attachments/assets/690bc1e5-6cbc-4b74-90e4-6e67857c218e" />


The application provides a simple and interactive Streamlit interface.

1. Upload an audio file in WAV, MP3, or FLAC format.
2. Select the desired noise reduction strength (Low, Medium, or High).
3. Choose the noise type (Stationary or Non-stationary).
4. Preview the original audio.
5. Click **Reduce Noise** to process the recording.
6. Listen to the enhanced audio and download the output.

## ⚙️ Working Principle

The application uses **spectral gating**, a signal-processing technique for reducing background noise.

The general processing flow is:

1. Load the input audio and convert it into a mono signal.
2. Analyze the audio in the frequency domain.
3. Estimate the background noise characteristics.
4. Generate a suppression mask to attenuate frequency components identified as noise.
5. Reconstruct the enhanced audio signal and save it as a WAV file.

The application uses the `noisereduce` library for spectral noise reduction.

## 🛠️ Technologies Used

- **Python** – Core application development.
- **Streamlit** – Interactive web-based user interface.
- **Librosa** – Audio loading and processing.
- **Noisereduce** – Spectral gating-based noise reduction.
- **NumPy** – Numerical operations.
- **SciPy** – Scientific and signal-processing support.
- **SoundFile** – Audio file writing and output generation.

## 📂 Project Structure

```text
Audio_denoise/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│
├── results/
│
└── src/
    ├── audio_utils.py
    └── denoise.py
```

## 🚀 Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sakshithakkar06/Audio_denoise.git
cd Audio_denoise
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Linux / WSL:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser. If it doesn't, open the local URL displayed in the terminal.

## 🎯 Significance and Applications

Speech noise reduction is useful in applications where clear audio communication is important, such as:

- Voice and video communication systems.
- Hands-free communication in automotive systems.
- Smart speakers and voice-controlled devices.
- Audio recording and speech enhancement applications.
- Hearing assistance and assistive listening technologies.

This project provides practical exposure to digital signal processing concepts and Python-based audio enhancement. The techniques explored can also serve as a foundation for future implementation and optimization on embedded audio-processing platforms.

## 📌 Future Scope

- Real-time audio noise reduction.
- Support for additional noise reduction algorithms.
- Optimization for resource-constrained embedded platforms.
- Improved speech preservation in recordings with overlapping noise.

## 👩‍💻 Author
