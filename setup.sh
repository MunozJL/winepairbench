#!/bin/bash
# WinePairBench Environment Setup
# Run: chmod +x setup.sh && source setup.sh

python3 -m venv ~/winepairbench-env
source ~/winepairbench-env/bin/activate
pip install langsmith langchain langchain-openai langchain-anthropic

# SET YOUR API KEYS HERE (replace with your own)
export LANGCHAIN_API_KEY="your-langsmith-key"
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_PROJECT=winepairbench
export OPENAI_API_KEY="your-openai-key"
export OPENROUTER_API_KEY="your-openrouter-key"

echo "Environment ready. Run: python3 upload_questions.py"
