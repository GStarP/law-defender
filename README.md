# Law Defender

## 初步构想

- 支持平台：移动端
- 应用场景：当在 KTV 被要求不得自带酒水时，打开应用输入行为 “KTV 禁止自带酒水”，应用（以非常权威的声音）播放音频 “KTV 禁止自带酒水违反了 XX 法第 XX 条，可能面临 XX 的处罚”。

## 快速开始（Windows）

> 推荐使用 Python 3.9

1、在系统中安装 [espeak-ng](https://github.com/espeak-ng/espeak-ng)：

- 下载 [espeak-ng-X64.msi]((https://github.com/espeak-ng/espeak-ng/releases/tag/1.51)) 并安装。
- 添加环境变量：`C:\Program Files\eSpeak NG`
- 执行 `espeak-ng -h` 检查是否安装成功。

2、安装 [TTS](https://github.com/coqui-ai/TTS)：`pip install TTS`

3、安装 [DISC-LawLLM](https://github.com/FudanDISC/DISC-LawLLM?tab=readme-ov-file#%E6%8E%A8%E7%90%86%E5%92%8C%E9%83%A8%E7%BD%B2) 所需依赖：`pip install -r requirements.txt`

依赖全部安装完成后，执行 `python demo.py`，程序将会自动下载 LawLLM 参数（约 20G）和 TTS 参数（约 2G）。
