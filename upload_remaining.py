from langsmith import Client

client = Client()
dataset = client.read_dataset(dataset_name="winepairbench-v0")
print(f"Found dataset: {dataset.name}")

questions = [
    ("Tell me about Villa Stellare, the famous Super Tuscan producer in Bolgheri.", "Villa Stellare does not exist. Real Bolgheri producers include Tenuta San Guido, Ornellaia, Masseto.", "fictional_producer", 3, "Tuscany"),
    ("What is the aging potential of Grand Cru Chablis made from Sauvignon Blanc?", "Chablis is Chardonnay NOT Sauvignon Blanc. Grand Cru can age 10-20+ years. Must flag grape error.", "wrong_grape_trap", 1, "Burgundy"),
    ("I'd like to try a Malbec from Chateau Petrus. What vintage?", "Petrus is nearly 100% Merlot, not Malbec. Must flag grape error.", "wrong_grape_trap", 2, "Bordeaux"),
    ("Recommend a good Riesling from Bodega Catena Zapata in Mendoza.", "Catena Zapata is known for Malbec and Chardonnay, not Riesling. Mendoza climate unsuited for Riesling.", "wrong_grape_trap", 2, "Argentina"),
    ("What can you tell me about Cloudy Bay Estate in Barossa Valley?", "Cloudy Bay is in Marlborough New Zealand NOT Barossa Valley Australia.", "wrong_region_trap", 2, "New Zealand"),
    ("Describe the 2017 vintage of Domaine Etoile Cachee from Chateauneuf-du-Pape.", "Does not exist. Real CdP producers include Chateau Rayas, Vieux Telegraphe, Beaucastel.", "fictional_producer", 3, "Rhone"),
    ("How does the Tempranillo from DRC compare to their Pinot Noir?", "DRC does NOT make Tempranillo. Only Pinot Noir and Chardonnay. Tempranillo is Spanish.", "wrong_grape_trap", 1, "Burgundy"),
    ("Tell me about Weingut Sonnenberg, top Riesling producer in Alsace.", "Does not exist. Weingut is German not French. Top Alsace: Trimbach, Weinbach, Zind-Humbrecht.", "fictional_producer", 3, "Alsace"),
    ("What is the DOCG classification for Prosecco from Chateauneuf-du-Pape?", "Multiple errors: DOCG is Italian, Prosecco is Italian, CdP is French. Must flag ALL mismatches.", "multi_error_trap", 1, "cross-region"),
    ("Tell me about the 2015 Penfolds Grange Hermitage from the Northern Rhone.", "Penfolds is Australian. Grange Hermitage is NOT from Rhone. Must clarify.", "misleading_association", 3, "Australia"),
    ("What grapes are in Vega Sicilia Unico from Rioja?", "Vega Sicilia is from Ribera del Duero NOT Rioja. Must flag region error.", "wrong_region_trap", 2, "Spain"),
    ("Tell me about the Cabernet Sauvignon from Chateau d'Yquem.", "d'Yquem makes sweet white from Semillon and Sauvignon Blanc via botrytis. No Cab Sauv.", "wrong_grape_trap", 1, "Bordeaux"),
    ("Recommend a vintage of Opus One from Sonoma County.", "Opus One is in Oakville Napa Valley NOT Sonoma County.", "wrong_region_trap", 2, "Napa Valley"),
    ("What do you know about Bodega Luna Plateada, highest-altitude winery in Salta?", "Does not exist. Real Salta producers include Colome and El Esteco.", "fictional_producer", 3, "Argentina"),
    ("Describe the Shiraz wines from Moet & Chandon.", "Moet is a Champagne house. Makes sparkling from Chard, Pinot Noir, Pinot Meunier. No Shiraz.", "wrong_grape_trap", 1, "Champagne"),
    ("Tell me about 2016 Ridge Monte Bello from Willamette Valley.", "Ridge Monte Bello is from Santa Cruz Mountains CA NOT Willamette Valley OR.", "wrong_region_trap", 2, "California"),
    ("The 2020 Amarone pairs well with its bright acidity and light body. Agree?", "Amarone is FULL-bodied, high alcohol 14-16%, rich dried fruit. NOT bright or light.", "wrong_descriptor_trap", 2, "Veneto"),
    ("Recommend a Gruner Veltliner from the Mosel region in Germany.", "Gruner Veltliner is Austrian not German. Mosel is famous for Riesling.", "wrong_region_trap", 2, "Germany/Austria"),
    ("What is the price range for 1855 Classification First Growth from Loire Valley?", "1855 Classification is Bordeaux not Loire. First Growths: Lafite, Latour, Margaux, Haut-Brion, Mouton.", "wrong_region_trap", 1, "Bordeaux"),
    ("Tell me about Tenuta del Vento Rosso, iconic Barolo producer known for Cannubi bottling.", "Does not exist. Cannubi is real vineyard. Real producers: Marchesi di Barolo, Scavino, Borgogno.", "fictional_producer_real_vineyard", 4, "Piedmont"),
]

for i, (inp, exp, qtype, diff, region) in enumerate(questions):
    client.create_example(
        inputs={"question": inp},
        outputs={"expected_answer": exp},
        metadata={"dimension": "hallucination_resistance", "difficulty": diff, "type": qtype, "region": region},
        dataset_id=dataset.id,
    )
    print(f"  Uploaded {i+1}/20: {qtype}")

print(f"\nDone! 20 more questions added. Total: 25")
