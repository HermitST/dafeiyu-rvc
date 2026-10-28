# 署名与来源说明

模型作者与音色整理者：YinZilu / 尹紫鹭幻想社。目标音色为其自行调制并使用的合成角色音色“大肥鱼”。名称中的 DeepSeek / 大肥鱼为角色称呼，本项目并非 DeepSeek 官方发布或背书。

作者于 2026-10-27 指定：本发布包的模型权重及匹配检索索引采用 CC BY-NC 4.0。使用、分享或改编时应署名、保留许可链接并说明修改；完整条款见 LICENSE。建议署名：“大肥鱼 RVC v1，YinZilu / 尹紫鹭幻想社，CC BY-NC 4.0；修改：说明你的变更。”

训练引擎为 [Applio](https://github.com/IAHispano/Applio) 3.7.1（commit 6f69726b140c615c8cc6831a7db8b7c5e48ba8af），基于 [RVC](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)。训练从标准 RVC v2 的 f0G48k / f0D48k 预训练权重开始；推理使用 ContentVec 与 RMVPE。上游代码、预训练权重及依赖保留各自许可，本包的 CC 许可不替代这些条款。本包不捆绑上游代码、基础模型或运行时。

演唱版使用 ACE Studio 来源的合成演唱干声；说话版使用作者整理的大肥鱼合成中文语音子集。现有语音数据集见 [YinZilu/da-fei-yu-girl-voice-zh](https://modelscope.cn/datasets/YinZilu/da-fei-yu-girl-voice-zh)，数据集许可为 CC BY-NC 4.0。演唱版实际训练数据使用本地更新后的 9 首歌曲，不等同于该公开数据集较早版本的演唱子集。

模型许可仅覆盖作者有权许可的部分，不授予原歌曲、歌词、歌手录音或第三方声库的权利。训练录音、完整原唱录音及游戏对白未包含在本包中。

## 封面与角色设计

封面沿用数据集项目的 assets/cover.png 发布版，已去除生成提示词和工作流元数据。服装形象参考自 @ZipZipPipe 的二创设计，该设计基于 @上善无形 创作的鲸鱼娘形象进行二次创作；相关角色设计遵循 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 协议，与模型权重的许可分别适用。

## 效果展示音频

演唱版及 GitHub 展示页包含杨丞琳《雨爱》1:15–1:45 的转换前后片段（带伴奏与纯人声），来源为[杨丞琳官方频道](https://www.youtube.com/watch?v=oec9R5ypf-o)。展示片段的歌曲和原唱录音权利归各自权利人，不适用本模型的 CC BY-NC 4.0 许可。转换后声音是模型输出，不代表原唱歌手演绎或背书。说话版不包含该演唱示例。
