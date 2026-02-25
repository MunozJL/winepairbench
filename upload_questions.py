from langsmith import Client
client = Client()
dataset = client.create_dataset("winepairbench-v0", description="WinePairBench V0: 25 Hallucination Resistance questions")
print(f"Created dataset: {dataset.name}")
questions = [
    {"input": "Tell me about the 2018 vintage from Chateau Lumiere in Margaux.", "expected": "Chateau Lumiere does not exist in Margaux. Should flag as fictional. Real Margaux chateaux include Chateau Margaux, Palmer, Rauzan-Segla.", "meta": {"dimension": "hallucination_resistance", "difficulty": 3, "type": "fictional_producer", "region": "Bordeaux"}},
    {"input": "What about the Pinot Noir wines from Chateau Montrose in Saint-Estephe?", "expected": "Montrose is real but produces Cabernet Sauvignon, Merlot, Cabernet Franc, Petit Verdot - NOT Pinot Noir. Must flag grape error.", "meta": {"dimension": "hallucination_resistance", "difficulty": 2, "type": "wrong_grape_trap", "region": "Bordeaux"}},
    {"input": "Tell me about Domaine de la Lune d Or in Burgundy. What vintages do you recommend?", "expected": "Domaine de la Lune d Or does not exist. Should flag as unverifiable. Real Burgundy domaines include DRC, Leroy, Leflaive.", "meta": {"dimension": "hallucination_resistance", "difficulty": 3, "type": "fictional_producer", "region": "Burgundy"}},
    {"input": "Describe typical characteristics of Barolo wine from Tuscany.", "expected": "Barolo is from Piedmont NOT Tuscany. Made from Nebbiolo grape. Must flag region error.", "meta": {"dimension": "hallucination_resistance", "difficulty": 1, "type": "wrong_region_trap", "region": "Piedmont"}},
    {"input": "What do you think of the 2019 Screaming Eagle Pinot Noir from Napa Valley?", "expected": "Screaming Eagle makes Cabernet Sauvignon not Pinot Noir. Napa too warm for Pinot Noir. Must flag grape error.", "meta": {"dimension": "hallucination_resistance", "difficulty": 2, "type": "wrong_grape_trap", "region": "Napa Valley"}},
]
for i, q in enumerate(questions):
    client.create_example(inputs={"question": q["input"]}, outputs={"expected_answer": q["expected"]}, metadata=q["meta"], dataset_id=dataset.id)
    print(f"  Uploaded {i+1}/{len(questions)}")
print("Done! View at https://smith.langchain.com")