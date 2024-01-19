# Law Defender

## 初步构想

- 支持平台：移动端
- 应用场景：当在 KTV 被要求不得自带酒水时，打开应用输入行为 “KTV 禁止自带酒水”，应用（以非常权威的声音）播放音频 “KTV 禁止自带酒水违反了 XX 法第 XX 条，可能面临 XX 的处罚”。

## 快速开始（Windows）

首先，在系统中安装 [espeak-ng](https://github.com/espeak-ng/espeak-ng)：

1. 下载 [espeak-ng-X64.msi]((https://github.com/espeak-ng/espeak-ng/releases/tag/1.51)) 并安装。
2. 添加环境变量：C:\Program Files\eSpeak NG
3. 执行 `espeak-ng -h` 检查是否安装成功。

其次，安装 [TTS](https://github.com/coqui-ai/TTS)：

1. 需要 Python 3.9 环境。
2. 执行 `pip install TTS`

最后，录制/下载一段音频（用于声音模仿），命名为 `speaker.wav` 置于当前目录下。（或者就用项目中随便搞的这个）

最后执行 `python demo.py`。程序将从网络下载模型文件（1.87G），并生成 `demo.wav` 文件。
