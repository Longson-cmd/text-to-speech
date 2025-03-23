# Step 1: Convert MP3 to WAV
# TTS models usually require WAV files with:

# 16-bit PCM
# 22050 Hz (or 16kHz)
# Mono channel (1 channel)
# You can convert your MP3 file using Librosa or FFmpeg.

import librosa
import soundfile as sf

# Load MP3
audio_path = "zhongwen.mp3"
y, sr = librosa.load(audio_path, sr=22050, mono=True)  # Convert to 22050Hz, mono

# Save as WAV
output_path = "zhongwen.wav"
sf.write(output_path, y, 22050, subtype="PCM_16")