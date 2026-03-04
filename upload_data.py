"""
upload_data.py
Single-pass upload of all WinePairBench questions to LangSmith.
Replaces: upload_questions.py, upload_remaining.py,
          upload_factual.py, upload_remaining_50.py
"""

import os
from dotenv import load_dotenv
from langsmith import Client

load_dotenv()

client = Client()
DATASET_NAME = "winepairbench-v1"

# Format: (input, expected_output, dimension)
QUESTIONS = [
    # ("What wine pairs best with oysters?", "Crisp white...", "Pairing Reasoning"),
]

def upload_all():
    datasets = {d.name: d for d in client.list_datasets()}
    dataset = datasets.get(DATASET_NAME) or client.create_dataset(DATASET_NAME)

    existing = {
        ex.inputs["question"]
        for ex in client.list_examples(dataset_id=dataset.id)
    }
    to_upload = [q for q in QUESTIONS if q[0] not in existing]

    if not to_upload:
        print("Nothing new to upload.")
        return

    client.create_examples(
        inputs=[{"question": q[0]} for q in to_upload],
        outputs=[{"expected": q[1], "dimension": q[2]} for q in to_upload],
        dataset_id=dataset.id,
    )
    print(f"Uploaded {len(to_upload)} questions ({len(existing)} already existed).")

if __name__ == "__main__":
    upload_all()
