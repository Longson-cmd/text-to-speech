# Step 1: Convert MP3 to WAV
# TTS models usually require WAV files with:

# 16-bit PCM
# 22050 Hz (or 16kHz)
# Mono channel (1 channel)
# You can convert your MP3 file using Librosa or FFmpeg.

import librosa
import soundfile as sf

# Load MP3
audio_path = "advice.mp3"
y, sr = librosa.load(audio_path, sr=22050, mono=True)  # Convert to 22050Hz, mono

# Save as WAV
output_path = "advice.wav"
sf.write(output_path, y, 22050, subtype="PCM_16")

print("Conversion completed:", output_path)


# Step 2: Normalize the Audio
import numpy as np

# Normalize audio
y = y / np.max(np.abs(y))

# Save normalized audio
sf.write(output_path, y, 22050, subtype="PCM_16")
print("Normalization completed:", output_path)

# Step 3: Trim Silence
y_trimmed, _ = librosa.effects.trim(y, top_db=25)

# Save trimmed audio
sf.write(output_path, y_trimmed, 22050, subtype="PCM_16")
print("Silence trimmed:", output_path)


# Step 4: Segment Long Audio into Shorter Clips
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Load WAV
audio = AudioSegment.from_wav(output_path)

# Split based on silence
chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-40)

# Save each chunk separately
output_dir = "C:/Users/PC/Desktop/unfinish projects/audio projects/chunks"
os.makedirs(output_dir, exist_ok=True)

for i, chunk in enumerate(chunks):
    chunk_path = os.path.join(output_dir, f"chunk_{i}.wav")
    chunk.export(chunk_path, format="wav")
    print(f"Saved: {chunk_path}")


