from TTS.api import TTS
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig
import time

# chat model
t = time.time()
model_path = "ShengbinYue/DISC-LawLLM"
model = AutoModelForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.float32, device_map="auto", trust_remote_code=True, offload_folder="offload"
)
model.generation_config = GenerationConfig.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(
    model_path, use_fast=False, trust_remote_code=True,
)
print("chat model:", time.time() - t, "s")

# tts model
t = time.time()
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2").to("cpu")
print("tts model:", time.time() - t, "s")

def ask(action: str):
  question = action + "违反了哪些法律法规？可能面临怎样的处罚？"
  messages = [
      {"role": "user", "content": question},
  ]
  t = time.time()
  answer = model.chat(tokenizer, messages)
  print("chat:", time.time() - t, "s")
  print("问: " + question + "\n" + "答: " + answer)

  t = time.time()
  tts.tts_to_file(answer, file_path="./demo.wav", language='zh-cn', speaker_wav='./speaker.wav')
  print("tts:", time.time() - t, "s")

ask("KTV 禁止自带酒水")
