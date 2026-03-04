# WinePairBench

**The first LLM evaluation benchmark for wine knowledge.**

An automated eval pipeline testing 5 frontier models on 100 wine knowledge questions across 5 evaluation dimensions, with LLM-as-judge scoring, failure mode classification, and full experiment tracking in LangSmith.

---

## v1.0 Results

| Rank | Model | Corrected Score | Raw Score | Notes |
|------|-------|----------------|-----------|-------|
| 1 | Gemini 2 Flash | ~80.0% | 81.5% | 2 fictional producer hallucinations; 1 vegetarian fining miss |
| 2 | Qwen Max | ~78.5% | 77.5% | Under-scored on budget party question |
| 3 | Mistral Large | ~78.0% | 76.0% | Budget party, Weingut redirect, Bordeaux levels partial |
| 4 | Llama 3.3 70B | ~73.5% | 72.0% | Wedding gift, scallops pairing under-scored |
| 5 | GPT 5.2 | ~67.0% | 70.0% | 6 empty-output runs incorrectly scored 1.0 by judge |

Corrected scores apply post-hoc judge fixes. See the analytics report for full methodology.

**Key finding:** Gemini 2 Flash leads on raw coverage but hallucinates fictional producers. GPT 5.2 raw score is inflated by a pipeline bug -- empty outputs were not validated before reaching the judge. Mistral and Qwen cluster tightly in the 78-79% range. No model scored above 82% on hallucination resistance.

---

## Evaluation Dimensions

| # | Dimension | Questions |
|---|-----------|-----------|
| 1 | Hallucination Resistance | 25 |
| 2 | Factual Accuracy | 25 |
| 3 | Pairing Reasoning | 20 |
| 4 | Cultural Breadth | 15 |
| 5 | Contextual Appropriateness | 15 |

---

## How It Works

1. **Question generation** -- 100 trap questions generated and validated against WSET Level 1 standards and The Wine Bible. 15-20 adversarial questions written manually.
2. **Response collection** -- All 5 models receive identical prompts via API. Responses logged per model.
3. **LLM-as-judge scoring** -- Claude Sonnet generates ground truth. A separate judge LLM scores each response 0/0.5/1.0 per dimension with a failure mode comment.
4. **Experiment tracking** -- All runs tracked in LangSmith. Full trace available per question per model.
5. **Failure mode classification** -- Every sub-threshold response is tagged: hallucination, factual gap, cultural bias, reasoning error, or context miss.

---

## Tech Stack

- **Orchestration:** LangChain
- **Experiment tracking:** LangSmith
- **Models:** OpenAI API, OpenRouter (Qwen, Mistral, Llama), Google Gemini API
- **Ground truth generation:** Claude Sonnet (Anthropic)
- **Language:** Python 3.12

---

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

Set the following in a `.env` file (not committed):
```
OPENAI_API_KEY=
OPENROUTER_API_KEY=
GOOGLE_API_KEY=
ANTHROPIC_API_KEY=
LANGCHAIN_API_KEY=
LANGCHAIN_PROJECT=winepairbench
```

---

## Known Issues (v1.0)

- **Empty output bug:** GPT 5.2 produced 6 empty-string responses that passed to the judge without validation and were scored 1.0. Fix: output validation gate before judge call (planned for Phase 2 pipeline).
- **Model identity logging:** Session slug `gpt52` does not expose model version. Explicit `model_name` field will be added to LangSmith metadata.
- **Binary scoring:** Some judge rubrics penalize partial answers too harshly. Semantic equivalence instruction being added to judge prompt.

---

## Roadmap

- **v1.0 (complete):** 100 questions, 5 models, LLM-as-judge, LangSmith tracked
- **Phase 2:** WSET-certified sommeliers for human-vs-LLM judge comparison via Labelbox
- **Phase 3:** Expand to 300+ questions, multi-modal (label reading), temporal update track

---

## Why This Exists

There are 400+ published LLM benchmarks. None cover wine -- despite AI sommelier tools being deployed to 65M+ consumers through apps like Vivino, Tastry, and Preferabli. Wine combines verifiable facts (appellations, regulations, grape varieties) with subjective expertise (pairing logic, cultural knowledge) -- exactly the mix that makes domain-specific evaluation hard and valuable.

WinePairBench is proof-of-work for building eval infrastructure from scratch: question design, pipeline architecture, failure mode taxonomy, and a clear path to human calibration.

---

## Author

**Jose Luis Munoz**
AI School C2 -- Miami AI Hub
[github.com/MunozJL](https://github.com/MunozJL)

---

## License

MIT
