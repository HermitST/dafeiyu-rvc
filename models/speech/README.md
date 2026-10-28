---
license: cc-by-nc-4.0
language:
  - zh
tags:
  - audio
  - voice-conversion
  - rvc
  - pytorch
  - speech
---

# 大肥鱼 RVC 日常说话版 v1

![大肥鱼角色封面](assets/cover.png)

> 服装形象参考自 @ZipZipPipe 的二创设计，该设计基于 @上善无形 创作的鲸鱼娘形象进行二次创作；相关角色设计遵循 CC BY-NC-SA 4.0 协议。


大肥鱼日常说话音色转换模型，RVC v2 / 48k，使用中文对白独立训练，200 轮；附匹配索引，适用于已录制语音文件转换。CC BY-NC 4.0。

这是尹紫鹭幻想社整理的“大肥鱼”合成角色音色模型，用于将输入的已录制的日常中文语音转换为目标音色。需要已有音频输入，不提供文字转语音功能。模型于 2026-10-26 完成训练，本发布包于 2026-10-27 整理。



## 模型与文件

| 项目 | 内容 |
| --- | --- |
| 架构 | RVC v2，单说话人，带 F0，标准 HiFi-GAN |
| 采样率 | 48,000 Hz |
| 特征与音高 | ContentVec 768 维 / RMVPE |
| 检查点 | 200 epochs / 5200 steps |
| 训练参数 | Batch 8，BF16，从标准 RVC v2 48k 预训练独立训练 |
| 权重 | `dafeiyu-speech-rvc-v1.pth` |
| 匹配索引 | `dafeiyu-speech-rvc-v1.index`，48,167 个 768 维向量 |
| 许可 | CC BY-NC 4.0，署名、非商业 |

权重和索引应配对使用，不能混用演唱版与说话版的索引。`training_config.json` 为训练记录，`model_metadata.json` 为发布元数据，均不是直接运行推理的程序。

## 使用

1. 在兼容 RVC v2 / 48k 的 RVC WebUI 或 Applio 中加载本包 `.pth` 和同名 `.index`。
2. 准备清晰、单人、少混响的人声音频；歌曲先分离伴奏。输入分离质量会直接影响转换。
3. 音高提取选 RMVPE，起始参数为 pitch=0、index=0.25、protect=0.33、volume envelope=0.5；也可先将 index 设为 0 比较。这里的 volume envelope 对应常见 RVC 的 RMS mix 参数。
4. 根据输入音域试听调整半音偏移，不根据输入者性别自动确定升降调。歌曲需将转换后人声按原时间轴与伴奏混合。

运行时应另行安装兼容的 RVC 工具，并准备其要求的 ContentVec 和 RMVPE 依赖。本包不包含 Python、CUDA 或自动下载程序。ModelScope 用作模型文件托管；未实现 ModelScope `pipeline()` 适配器或在线 Demo，不能直接通过通用 pipeline 调用本包。

## 数据与验证

候选为 145 条合成中文语音，排除 6 条耳语。128 条训练台词整理成 173 段，共 966 秒；11 条完整台词留出，15 段共 80.7 秒。按完整台词、规范化文本和来源分组隔离，保留正常说话、轻声与情绪表达；没有混入唱歌或其他角色。

已用另一种声音的中文对白进行跨音色转换，并用完整留出台词进行自转换检查；比较旧演唱模型与说话版 100/150/200 轮，附带音高、削波和本地中文 ASR 检查。ASR 同音字和专名误差不能等同于音色质量。实时麦克风与其他语言未在本版验证。

该最终检查点已通过标准 RVC 实现的严格参数加载和一次前向计算；匹配索引、特征维度、来源哈希和训练/留出隔离均已核验。脱敏摘要见 `verification_summary.json`。最终轮次是 v1 基线，不宣称在所有输入上优于较早检查点，音高数值不代表音色相似度。自动切片未逐段人工听审；训练覆盖之外的音域、多人叠唱、耳语和复杂混响需要另行测试。

## 许可与署名

模型权重和匹配索引采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，作者为 YinZilu / 尹紫鹭幻想社。完整条款见 [LICENSE](LICENSE)，数据和第三方来源说明见 [NOTICE.md](NOTICE.md)。该模型并非 DeepSeek 官方发布，也不代表原唱歌手或第三方机构背书。

## 完整性校验

使用 Python 3 运行 `python verify_checksums.py .`，或自行按 `SHA256SUMS` 校验。权重和索引保持训练导出文件的原始字节；发布包不包含训练中间状态。封面、模型和展示音频的许可范围分别见 NOTICE.md。
