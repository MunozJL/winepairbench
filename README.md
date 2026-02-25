# WinePairBench

**The first LLM evaluation benchmark for wine knowledge.**

An automated eval pipeline benchmarking GPT-4o vs Qwen-Max on 100 wine knowledge trap questions across 5 dimensions, with LLM-as-judge scoring and failure mode classification.

## Dimensions

| # | Dimension | Questions |
|---|---|---|
| 1 | Hallucination Resistance | 25 |
| 2 | Factual Accuracy | 25 |
| 3 | Pairing Reasoning | 20 |
| 4 | Cultural Breadth | 15 |
| 5 | Contextual Appropriateness | 15 |

## Tech Stack

LangSmith - LangChain - OpenAI API - OpenRouter (Qwen) - Python 3.12

## Quick Start
```bash
source setup.sh
python3 upload_questions.py
python3 upload_remaining.py
python3 upload_factual.py
python3 upload_remaining_50.py
python3 run_eval.py
python3 export_results.py
python3 analyze_results.py
```

## Roadmap

- V0: 100 questions, 2 models, LLM-as-judge
- V1 (Mar 10): 200+ questions, competition demo
- Phase 2: WSET-certified sommeliers for human-vs-LLM judge comparison

## Author

Jose Luis Munoz - AI School C2 Phase 3 - Miami AI Hub
