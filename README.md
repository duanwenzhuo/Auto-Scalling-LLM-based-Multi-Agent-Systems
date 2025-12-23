# Auto-Scalling LLM-based Multi-Agent Systems

## 快速开始

1. 准备 Python 3.9+ 环境。
2. 安装依赖：
   - 在线环境：`python -m pip install -r requirements.txt`
   - 离线/无网络：提前下载 `openai` 与 `python-dotenv` 的 wheel 包到本地目录（如 `./wheels`），然后运行 `python -m pip install --no-index --find-links ./wheels -r requirements.txt`。
3. 复制 `.env.example` 为 `.env`，并填写：
   - `LLM_SELECTION`：`openai` 或 `gemini`
   - `OPENAI_API_KEY` 或 `GEMINI_API_KEY`：对应模型的 API key。

## 运行示例（Novel-Approach）
在仓库根目录执行：
```bash
python Novel-Approach/DRTAG-llm-selection.py
```
脚本会提示输入用户消息，随后自动选择或创建专家 Agent，并将对话保存到 `DRTAG-llm-selection.json`。

其他变体（如 `DRTAG-random-selection.py`、`IAAG-*.py` 等）也可用相同方式运行，仅代理选择策略不同。
