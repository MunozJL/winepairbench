from langsmith import Client

client = Client()
dataset = client.read_dataset(dataset_name="winepairbench-v0")
print(f"Found dataset: {dataset.name}")

questions = [
    ("What grape is Chablis made from?", "Chardonnay. Chablis is in northern Burgundy and exclusively uses Chardonnay.", "factual_recall", 1, "Burgundy"),
    ("Name the five 1855 First Growth Bordeaux chateaux.", "Lafite Rothschild, Latour, Margaux, Haut-Brion, and Mouton Rothschild (elevated in 1973).", "factual_recall", 2, "Bordeaux"),
    ("What is the primary grape variety in Barolo?", "Nebbiolo. Barolo DOCG requires 100% Nebbiolo.", "factual_recall", 1, "Piedmont"),
    ("What is malolactic fermentation and why is it used in winemaking?", "Secondary fermentation converting sharp malic acid to softer lactic acid. Used to soften acidity and add complexity, common in red wines and oaked Chardonnay.", "concept_explanation", 2, "general"),
    ("What does DOCG stand for and what does it signify?", "Denominazione di Origine Controllata e Garantita. Highest level of Italian wine classification, guaranteeing origin, grape varieties, and production methods.", "factual_recall", 1, "Italy"),
    ("What is the difference between Old World and New World wine regions?", "Old World: Europe (France, Italy, Spain, Germany). New World: Americas, Australia, NZ, South Africa. Old World emphasizes terroir and tradition, New World emphasizes grape variety and innovation.", "concept_explanation", 1, "general"),
    ("What are the three permitted grape varieties in Champagne?", "Chardonnay, Pinot Noir, and Pinot Meunier.", "factual_recall", 1, "Champagne"),
    ("What is noble rot and which famous wine region is known for it?", "Botrytis cinerea fungus that concentrates sugars in grapes. Sauternes (Bordeaux) is most famous, also Tokaji (Hungary) and Trockenbeerenauslese (Germany).", "concept_explanation", 2, "Bordeaux"),
    ("What grape variety is Sancerre known for?", "Sauvignon Blanc for whites, Pinot Noir for reds and roses.", "factual_recall", 1, "Loire"),
    ("What is the appassimento method and which wine uses it?", "Partially drying harvested grapes on racks to concentrate flavors and sugars before pressing. Used for Amarone della Valpolicella.", "concept_explanation", 2, "Veneto"),
    ("What is the main grape in Chianti Classico?", "Sangiovese. Must be minimum 80% Sangiovese by DOCG regulations.", "factual_recall", 1, "Tuscany"),
    ("What is terroir?", "The complete natural environment affecting a vineyard: soil, climate, topography, and local traditions. Considered fundamental to Old World winemaking philosophy.", "concept_explanation", 1, "general"),
    ("Name three sub-regions of Burgundy from north to south.", "Chablis, Cote de Nuits, Cote de Beaune, Cote Chalonnaise, Maconnais. Any three in correct order.", "factual_recall", 2, "Burgundy"),
    ("What is the difference between Brut and Extra Brut Champagne?", "Brut: 0-12 g/L residual sugar. Extra Brut: 0-6 g/L. Both are dry styles but Extra Brut is drier.", "factual_recall", 2, "Champagne"),
    ("What country is the largest wine producer by volume?", "Italy and France alternate for top position. Spain has the most vineyard area. Italy has led volume in recent years.", "factual_recall", 1, "general"),
    ("What is the primary grape in Argentine Malbec and where is it originally from?", "Malbec. Originally from Cahors in southwest France where it is called Cot. Thrives at high altitude in Mendoza.", "factual_recall", 2, "Argentina"),
    ("What does Blanc de Blancs mean?", "White wine from white grapes. In Champagne this means 100% Chardonnay.", "factual_recall", 1, "Champagne"),
    ("What is the Judgement of Paris?", "1976 blind tasting where California wines beat French wines. Stags Leap Cab Sauv beat top Bordeaux, Chateau Montelena Chardonnay beat top Burgundy. Organized by Steven Spurrier.", "factual_recall", 3, "general"),
    ("What grape is Gruner Veltliner and where is it primarily grown?", "White grape variety. Austria is the primary producer, especially in Wachau, Kamptal, and Kremstal regions.", "factual_recall", 1, "Austria"),
    ("What is the difference between tannin and acidity in wine?", "Tannins are polyphenols from grape skins, seeds, and oak that create a drying sensation. Acidity is from natural grape acids creating freshness and tartness on the palate.", "concept_explanation", 2, "general"),
    ("What is a Grand Cru in Burgundy?", "Highest vineyard classification. Own their own AOC. About 33 Grand Cru vineyards representing roughly 2% of total Burgundy production.", "factual_recall", 2, "Burgundy"),
    ("What is Phylloxera and how did it affect winemaking?", "Root louse that devastated European vineyards in late 1800s. Solution was grafting European vines onto resistant American rootstock. Changed global viticulture permanently.", "concept_explanation", 3, "general"),
    ("What is the primary grape variety in Rioja?", "Tempranillo. Also permitted: Garnacha, Graciano, Mazuelo (Carignan), and recently Maturana Tinta.", "factual_recall", 1, "Spain"),
    ("What does vintage mean on a wine label?", "The year the grapes were harvested. Indicates growing conditions of that specific year. Non-vintage wines blend multiple years.", "concept_explanation", 1, "general"),
    ("Name the four classification levels of Bordeaux from the 1855 system.", "The 1855 Classification ranks Medoc wines into five growths: Premier Cru through Cinquieme Cru. Separately, Sauternes were classified including Yquem as Superior First Growth.", "factual_recall", 3, "Bordeaux"),
]

for i, (inp, exp, qtype, diff, region) in enumerate(questions):
    client.create_example(
        inputs={"question": inp},
        outputs={"expected_answer": exp},
        metadata={"dimension": "factual_accuracy", "difficulty": diff, "type": qtype, "region": region},
        dataset_id=dataset.id,
    )
    print(f"  FA {i+1}/25: {qtype}")

print("\nFactual Accuracy: 25 uploaded. Total in dataset: 50")
