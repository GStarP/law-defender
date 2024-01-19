from TTS.api import TTS

print(TTS().list_models())

text = "这种行为违反了消费者权益保护法第三十五条，可能面临一至三个月的有期徒刑。"

tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2").to("cpu")
tts.tts_to_file(text, file_path="./demo.wav", language='zh-cn', speaker_wav='./speaker.wav')
