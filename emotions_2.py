from TTS.api import TTS
import torch
import pickle

# Load XTTS v2 model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda" if torch.cuda.is_available() else "cpu")

# Set the path to your speaker audio file
speaker_wav = "C:/Users/PC/Desktop/unfinish projects/audio_projects_1/zhongwen.wav"  # Replace with your uploaded audio file

# Generate speech in that voice
tts.tts_to_file(
    text="天啊！太惊喜了！这份礼物美得让我说不出话，我的心跳加快，眼里满是感动！有你在，我就是世界上最幸福的人!",
    language="zh-cn",
    speaker_wav= speaker_wav,
    emotion="excited",
    file_path="excited_chinese_voice.wav"
)

