import inspect
from TTS.api import TTS

# Load XTTS v2
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# Get function signature
tts_params = inspect.signature(tts.tts_to_file)
print(tts_params)


