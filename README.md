# 胡桃 AI 语音聊天

基于 [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) 和 [DeepSeek](https://www.deepseek.com/) 的胡桃（原神）实时语音聊天项目。

## 功能

-   用文字和胡桃实时聊天
-   自动将胡桃的文字回复合成语音并播放
-   支持自定义角色设定（性格、语气、关系等）
-   可单独生成指定文本的语音文件

## 项目结构

| 文件 | 说明 |
| --- | --- |
| `hutao.py` | 主程序，包含聊天循环、DeepSeek 调用和 TTS 合成 |
| `requirements.txt` | Python 依赖列表 |
| `.env` | 存放 DeepSeek API Key（已 Git 忽略） |
| `.gitignore` | Git 忽略规则 |

## 快速开始

### 1. 克隆仓库

\`\`\`bash
git clone https://github.com/737415119-source/hutao-ai-voice-chat.git
cd hutao-ai-voice-chat
\`\`\`

### 2. 安装依赖

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. 配置 API Key

在项目目录下创建 `.env` 文件，写入：

\`\`\`
DEEPSEEK_API_KEY=你的DeepSeek API Key
\`\`\`

### 4. 启动 GPT-SoVITS API

先启动本地 GPT-SoVITS 的 API 服务，参考 [GPT-SoVITS 官方文档](https://github.com/RVC-Boss/GPT-SoVITS)。

### 5. 运行聊天

\`\`\`bash
python hutao.py
\`\`\`

## 自定义设定

编辑 `hutao.py` 中 `get_deepseek_reply` 函数的 `system` 提示词，即可改变胡桃的性格、语气和聊天方式。

## 依赖

-   Python 3.10+
-   GPT-SoVITS（本地部署）
-   DeepSeek API

## 致谢

-   [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - 语音克隆引擎
-   [DeepSeek](https://www.deepseek.com/) - 大语言模型 API
-   [原神](https://genshin.hoyoverse.com/) - 胡桃角色版权归米哈游所有

## 免责声明

本项目仅供学习交流使用，请勿用于商业用途。胡桃角色版权归属米哈游。