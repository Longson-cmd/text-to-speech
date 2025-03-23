from TTS.api import TTS

# Initialize a specific model (replace with an actual model name)
model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
tts = TTS(model_name)

# Check if the model supports multiple languages
if tts.is_multi_lingual:
    print("Supported languages:", tts.languages)
else:
    print("This model supports only one language.")

# Supported languages: ['en', 'es', 'fr', 'de', 'it', 'pt', 
#                       'pl', 'tr', 'ru', 'nl', 'cs', 'ar', 'zh-cn', 'hu', 'ko', 'ja', 'hi']
