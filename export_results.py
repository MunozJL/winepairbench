"""Export all LangSmith evaluation results to CSV."""
import csv
from langsmith import Client

client = Client()
projects = list(client.list_projects())
eval_projects = [p for p in projects if "hr-v0" in p.name]
print("Found experiments:")
for p in eval_projects:
    print(f"  {p.name}")
rows = []
for proj in eval_projects:
    model = "gpt4o" if "gpt4o" in proj.name else "qwen-max"
    runs = list(client.list_runs(project_name=proj.name, run_type="chain"))
    for run in runs:
        question = run.inputs.get("question", "")
        output = run.outputs.get("output", "") if run.outputs else ""
        score = None
        comment = ""
        feedbacks = list(client.list_feedback(run_ids=[run.id]))
        for fb in feedbacks:
            score = fb.score
            comment = fb.comment or ""
        rows.append({"model": model, "question": question, "response": output, "score": score, "comment": comment})
outfile = "eval_results.csv"
with open(outfile, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["model", "question", "response", "score", "comment"])
    writer.writeheader()
    writer.writerows(rows)
print(f"\nExported {len(rows)} rows to {outfile}")
