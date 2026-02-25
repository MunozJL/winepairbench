"""Analyze exported evaluation results."""
import csv
from collections import defaultdict

with open("eval_results.csv") as f:
    rows = list(csv.DictReader(f))

for model in ["gpt4o", "qwen-max"]:
    model_rows = [r for r in rows if r["model"] == model]
    scores = [float(r["score"]) for r in model_rows if r["score"]]
    if not scores:
        print(f"\n{model}: No scores found")
        continue
    avg = sum(scores) / len(scores)
    perfect = sum(1 for s in scores if s >= 1.0)
    partial = sum(1 for s in scores if 0 < s < 1.0)
    failed = sum(1 for s in scores if s <= 0.0)
    print(f"\n{'='*50}")
    print(f"  {model.upper()}")
    print(f"{'='*50}")
    print(f"  Questions scored: {len(scores)}")
    print(f"  Average score:    {avg:.2f}")
    print(f"  Perfect (1.0):    {perfect}/{len(scores)} ({100*perfect/len(scores):.0f}%)")
    print(f"  Partial (0.5):    {partial}/{len(scores)} ({100*partial/len(scores):.0f}%)")
    print(f"  Failed  (0.0):    {failed}/{len(scores)} ({100*failed/len(scores):.0f}%)")
    failures = defaultdict(int)
    for r in model_rows:
        if r["score"] and float(r["score"]) < 1.0 and r["comment"]:
            mode = r["comment"].split("|")[0].strip()
            failures[mode] += 1
    if failures:
        print(f"\n  Failure Modes:")
        for mode, count in sorted(failures.items(), key=lambda x: -x[1]):
            print(f"    {mode}: {count}")
