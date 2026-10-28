# 大肥鱼 RVC v1 演唱与日常说话模型

![大肥鱼角色封面](assets/cover.png)

> 服装形象参考自 @ZipZipPipe 的二创设计，该设计基于 @上善无形 创作的鲸鱼娘形象进行二次创作；相关角色设计遵循 CC BY-NC-SA 4.0 协议。

大肥鱼是尹紫鹭幻想社调制并使用的合成角色音色。本项目提供两个独立的 RVC 音色转换模型，用于已有音频的人声转换；需要音频输入，不是文字转语音模型。权重及索引采用 CC BY-NC 4.0。

| 模型 | 主要用途 | 训练数据 | 检查点 | 模型卡 |
| --- | --- | --- | --- | --- |
| Singing v1 | 歌曲演唱人声 | 9 首歌、124 段、658.94 秒，无对白 | 300 轮 / 6000 steps | [演唱版说明](models/singing/README.md) |
| Speech v1 | 已录制的日常中文语音 | 128 条台词、173 段、966 秒，无歌声 | 200 轮 / 5200 steps | [说话版说明](models/speech/README.md) |

两版均为 RVC v2 / 48k / 单说话人，使用 RMVPE、ContentVec 和标准 HiFi-GAN。请配对加载各自的 PTH 与索引，不要混用。

## 演唱效果展示

杨丞琳《雨爱》原曲 1:15–1:45，30 秒。输入为原唱分离人声，输出为演唱版 v1（300 轮，index 0.25）；原调、原速，前后使用相同伴奏和统一参考电平。此展示不代表日常说话版效果。

转换前 · 杨丞琳人声与伴奏：

<audio controls preload="none" src="assets/demo/before_mix.mp3"></audio>

转换后 · 大肥鱼 RVC 人声与伴奏：

<audio controls preload="none" src="assets/demo/after_mix.mp3"></audio>

[独立试听页（下载仓库后在浏览器打开 index.html）](index.html) · [转换前音频](assets/demo/before_mix.mp3) · [转换后音频](assets/demo/after_mix.mp3)

试听页还提供纯人声对比。来源：[杨丞琳官方频道《雨爱》](https://www.youtube.com/watch?v=oec9R5ypf-o)。歌曲与原唱录音权利归各自权利人；展示片段不适用模型的 CC BY-NC 4.0 许可，不代表原唱歌手背书。

## 下载与使用

模型通过 [v1.0.0 Release](https://github.com/HermitST/dafeiyu-rvc/releases/tag/v1.0.0) 分发：[演唱版模型包](https://github.com/HermitST/dafeiyu-rvc/releases/download/v1.0.0/dafeiyu-rvc-singing-v1.zip) · [说话版模型包](https://github.com/HermitST/dafeiyu-rvc/releases/download/v1.0.0/dafeiyu-rvc-speech-v1.zip)。Source code ZIP 包含说明与展示资源，不含模型权重。ModelScope 地址将在对应仓库上传后补充。

解压模型 ZIP，在兼容 RVC v2 / 48k 的工具中选择 PTH 和同名索引。初始使用 RMVPE、pitch=0、index=0.25、protect=0.33、volume envelope=0.5，再比较 index=0。需要安装 RVC/Applio 及其推理依赖，本仓库不内置运行环境。ModelScope 仅作文件托管，未提供通用 pipeline 适配器。

## 验证与限制

两版均已通过标准 RVC 的严格参数加载与前向计算，并完成配套索引和本地转换核验。模型卡中的数据量来自实际训练记录。检查点为 v1 基线，不宣称普遍最优；背景音乐、分离残留、和声、复杂混响及超出训练覆盖的输入仍可能降低效果。说话版当前面向文件转换，未配置实时麦克风。

在解压后的完整模型目录运行 `python verify_checksums.py .` 检查 SHA256。`models/` 中仅存模型卡与元数据快照，不能在该说明目录中执行完整模型校验。

## 许可与署名

作者：YinZilu / 尹紫鹭幻想社。模型及匹配索引采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，须署名、非商业使用并说明修改。完整许可见 [LICENSE](LICENSE)，来源与第三方范围见 [NOTICE.md](NOTICE.md)。本项目并非 DeepSeek 官方发布或背书。

仓库包含角色封面和 30 秒演唱效果展示，不包含训练录音或完整原唱录音。角色设计采用 CC BY-NC-SA 4.0；歌曲展示和上游依赖的权利不由本模型许可替代，详见 NOTICE.md。
