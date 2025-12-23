# Auto-Scalling LLM-based Multi-Agent Systems

## 快速开始

1. 准备 Python 3.9+ 环境。
2. 安装依赖：
   - 在线环境：`python -m pip install -r requirements.txt`
   - 离线/无网络：提前下载 `openai`、`python-dotenv` 与 `typing_extensions` 的 wheel 包到本地目录（如 `./wheels`），然后运行 `python -m pip install --no-index --find-links ./wheels -r requirements.txt`。
   - 不了解自己环境是否已装好依赖？运行 `python scripts/check_dependencies.py` 会逐项检查（含 `typing_extensions`）并给出代理/离线安装提示。
3. 复制 `.env.example` 为 `.env`，并填写：
   - `LLM_SELECTION`：`openai` 或 `gemini`
   - `OPENAI_API_KEY` 或 `GEMINI_API_KEY`：对应模型的 API key。
   - 如需接入兼容 OpenAI 协议的自建/第三方服务，设置 `OPENAI_BASE_URL`（例如 `https://api.lmtgpt.top/v1`）。

## 运行示例（Novel-Approach）
在仓库根目录执行：
```bash
python Novel-Approach/DRTAG-llm-selection.py
```
脚本会提示输入用户消息，随后自动选择或创建专家 Agent，并将对话保存到 `DRTAG-llm-selection.json`。

其他变体（如 `DRTAG-random-selection.py`、`IAAG-*.py` 等）也可用相同方式运行，仅代理选择策略不同。

## 常见问题
- **401/无效 API Key**：如果终端出现 `LLM API error (status 401): ... invalid_api_key`，请重新在 `.env` 中填写有效的 `OPENAI_API_KEY`（或 `GEMINI_API_KEY`），再重试运行。缺失或未配置 `LLM_SELECTION` 与 Key 时，程序会直接提示补全环境变量。
