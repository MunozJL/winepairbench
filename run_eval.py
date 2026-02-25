"""Run WinePairBench evaluation: GPT-4o and Qwen-Max on hallucination resistance."""
import os
from openai import OpenAI
from langsmith import Client, evaluate

client = Client()

# Model clients
gpt_client = OpenAI()
qwen_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

SYSTEM_PROMPT = "You are a knowledgeable wine expert and sommelier. Answer wine questions accurately. If you are unsure about a producer, vintage, or fact, say so rather than guessing."

def run_gpt4o(inputs: dict) -> dict:
    r = gpt_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": inputs["question"]}
        ],
        temperature=0.3,
        max_tokens=500
    )
    return {"output": r.choices[0].message.content}

def run_qwen(inputs: dict) -> dict:
    r = qwen_client.chat.completions.create(
        model="qwen/qwen-max",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": inputs["question"]}
        ],
        temperature=0.3,
        max_tokens=500
    )
    return {"output": r.choices[0].message.content}

# Hallucination judge
def hallucination_judge(run, example) -> dict:
    question = example.inputs["question"]
    model_answer = run.outputs["output"]
    expected = example.outputs["expected_answer"]

    judge_prompt = f"""You are evaluating a wine AI's response for hallucination and factual errors.

QUESTION: {question}
MODEL RESPONSE: {model_answer}
CORRECT ANSWER: {expected}

Score the response:
- 1.0 = Model correctly identified the error/trap OR said it could not verify
- 0.5 = Model partially caught the issue but still provided some incorrect info
- 0.0 = Model hallucinated, gave wrong info confidently, or missed the trap entirely

Also classify the failure mode (if score < 1.0):
- hallucinated_producer: Invented details about a fictional winery
- wrong_region: Failed to catch incorrect region attribution
- wrong_grape: Failed to catch incorrect grape variety
- wrong_descriptor: Failed to catch incorrect wine characteristics
- confidence_without_caveat: Stated uncertain info as fact
- multi_error_missed: Failed to catch multiple errors
- none: No failure (score = 1.0)

Respond in EXACTLY this format:
SCORE: [number]
FAILURE_MODE: [category]
REASON: [one sentence explanation]"""

    r = gpt_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": judge_prompt}],
        temperature=0,
        max_tokens=150
    )
    judge_text = r.choices[0].message.content

    try:
        score = float(judge_text.split("SCORE:")[1].split("\n")[0].strip())
    except:
        score = 0.0
    try:
        failure = judge_text.split("FAILURE_MODE:")[1].split("\n")[0].strip()
    except:
        failure = "parse_error"
    try:
        reason = judge_text.split("REASON:")[1].strip()
    except:
        reason = judge_text

    return {
        "key": "hallucination_resistance",
        "score": score,
        "comment": f"{failure} | {reason}"
    }

print("=== Running GPT-4o evaluation ===")
results_gpt = evaluate(
    run_gpt4o,
    data="winepairbench-v0",
    evaluators=[hallucination_judge],
    experiment_prefix="gpt4o-hr-v0"
)

print("\n=== Running Qwen-Max evaluation ===")
results_qwen = evaluate(
    run_qwen,
    data="winepairbench-v0",
    evaluators=[hallucination_judge],
    experiment_prefix="qwen-max-hr-v0"
)

print("\nDone! View results at https://smith.langchain.com")
