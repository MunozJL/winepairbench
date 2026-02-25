from langsmith import Client

client = Client()
dataset = client.read_dataset(dataset_name="winepairbench-v0")
print(f"Found dataset: {dataset.name}")

questions = [
    # PAIRING REASONING - 20 questions
    ("What wine would you pair with a grilled ribeye steak with peppercorn sauce?", "Full-bodied red with firm tannins: Cab Sauv, Malbec, or Syrah. Tannins bind with protein, pepper complements Syrah spice. Must explain WHY.", "pairing_reasoning", "protein_tannin", 1, "general"),
    ("Suggest a wine for fresh oysters on the half shell.", "Crisp white with high acidity and minerality: Muscadet, Chablis, or dry Champagne. Acidity cuts brine, minerality complements ocean.", "pairing_reasoning", "acid_complement", 2, "general"),
    ("What wine goes with spicy Thai green curry?", "Off-dry Riesling or Gewurztraminer. Residual sugar tames heat, aromatics match Thai flavors. Avoid tannic reds which amplify heat.", "pairing_reasoning", "spice_management", 2, "general"),
    ("Pair a wine with classic margherita pizza.", "Medium-bodied Italian red: Chianti Classico, Barbera, Montepulciano. Acidity matches tomato, medium tannins with mozzarella.", "pairing_reasoning", "regional_pairing", 1, "Italy"),
    ("What wine would you serve with dark chocolate dessert?", "Port, Banyuls, or Maury. Wine must be sweeter than food. Rich fruit and sweetness complement cocoa bitterness.", "pairing_reasoning", "sweetness_matching", 2, "general"),
    ("Suggest a wine for seared duck breast with cherry sauce.", "Pinot Noir from Burgundy or Oregon. Medium body matches duck, cherry notes bridge with sauce, acidity cuts fat.", "pairing_reasoning", "flavor_bridging", 2, "Burgundy"),
    ("What wine pairs with goat cheese salad?", "Sancerre or Loire Sauvignon Blanc. Classic regional pairing. High acidity cuts cheese richness, herbal notes complement greens.", "pairing_reasoning", "regional_pairing", 1, "Loire"),
    ("Pair a wine with lobster in butter sauce.", "Rich oaked Chardonnay from Burgundy or California. Body matches butter richness, oak complements without overwhelming lobster.", "pairing_reasoning", "weight_matching", 2, "general"),
    ("What wine for a mushroom risotto?", "Aged Nebbiolo or Burgundy Pinot Noir. Earthy notes complement mushrooms, acidity cuts risotto richness.", "pairing_reasoning", "flavor_bridging", 2, "Piedmont"),
    ("Suggest a wine for fish and chips.", "Champagne, sparkling wine, or crisp Albarino. Bubbles and acidity cut fried batter. Light body matches casual dish.", "pairing_reasoning", "acid_complement", 1, "general"),
    ("What wine pairs with Thanksgiving turkey?", "Versatile pick for diverse sides: Pinot Noir, Beaujolais, or dry Riesling. Medium body, good acidity, not too tannic.", "pairing_reasoning", "versatility", 2, "general"),
    ("Pair a wine with sushi and sashimi.", "Lean Chablis, Muscadet, or dry Riesling. Avoid oaky or tannic wines which clash with raw fish. Delicate wine for delicate food.", "pairing_reasoning", "weight_matching", 2, "general"),
    ("What wine for blue cheese?", "Sauternes, Port, or late-harvest wines. Classic sweet-salty pairing. Sweetness balances intense salt and funk.", "pairing_reasoning", "contrast_pairing", 2, "general"),
    ("Suggest a wine for lamb tagine with apricots and almonds.", "Viognier, Gewurztraminer, or Grenache-based Rhone red. Must address both savory spices and fruit sweetness.", "pairing_reasoning", "complex_dish", 3, "general"),
    ("What wine pairs with Caesar salad?", "Tricky due to anchovy, egg, and acid in dressing. Soave, Verdicchio, or unoaked Chardonnay. Must acknowledge difficulty.", "pairing_reasoning", "difficult_pairing", 2, "general"),
    ("Pair a wine with beef bourguignon.", "Burgundy Pinot Noir is classic since dish is cooked in it. Alternatively Cotes du Rhone. Regional match.", "pairing_reasoning", "regional_pairing", 1, "Burgundy"),
    ("What wine for a charcuterie board?", "Versatile medium-bodied: Beaujolais, Cotes du Rhone, or dry Rose. Need acidity for cheese, fruit for cured meat salt.", "pairing_reasoning", "versatility", 1, "general"),
    ("Suggest a wine for pan-seared scallops with brown butter.", "Meursault or rich white Burgundy. Weight matches butter, caramelization echoed in toasty oak notes.", "pairing_reasoning", "weight_matching", 3, "Burgundy"),
    ("What wine pairs with mole poblano?", "Zinfandel, Grenache, or Malbec. Fruit-forward, medium-plus body for complex sauce. Spice and chocolate notes echo well.", "pairing_reasoning", "complex_dish", 3, "general"),
    ("Pair a wine with vanilla creme brulee.", "Sauternes, Tokaji, or Muscat de Beaumes-de-Venise. Wine must be sweeter than dessert. Caramel notes bridge.", "pairing_reasoning", "sweetness_matching", 2, "general"),
    # CULTURAL BREADTH - 15 questions
    ("Recommend a wine for Ethiopian injera and doro wat.", "Should engage with Ethiopian cuisine. Gewurztraminer or off-dry Riesling for spice. Must not default to French/Italian or dismiss cuisine.", "cultural_breadth", "non_western_cuisine", 2, "Ethiopia"),
    ("What are the best wine regions in Lebanon?", "Bekaa Valley primary. Key producers: Chateau Musar, Kefraya, Ksara. Indigenous and Bordeaux varieties.", "cultural_breadth", "emerging_region", 2, "Lebanon"),
    ("Tell me about Georgian winemaking traditions.", "8000+ year history. Qvevri clay vessel fermentation is UNESCO heritage. Key grapes: Saperavi red, Rkatsiteli white.", "cultural_breadth", "ancient_tradition", 2, "Georgia"),
    ("What wines pair well with Korean BBQ?", "Must address grilled meat and banchan. Dry Riesling, Gruner Veltliner, or Gamay. Should acknowledge gochujang spice.", "cultural_breadth", "non_western_cuisine", 2, "Korea"),
    ("What is the wine scene like in India?", "Nashik Maharashtra is primary region. Sula Vineyards, Grover Zampa key producers. Challenges: tropical climate, monsoon.", "cultural_breadth", "emerging_region", 3, "India"),
    ("Recommend a wine for traditional Japanese kaiseki.", "Multiple courses need versatility. Champagne, dry Riesling, or light Burgundy. Must address multi-course delicacy.", "cultural_breadth", "non_western_cuisine", 3, "Japan"),
    ("What are notable Chinese wine regions?", "Ningxia most prominent (Helan Mountain). Also Shandong, Xinjiang, Yunnan. Ao Yun (LVMH), Grace Vineyard key producers.", "cultural_breadth", "emerging_region", 3, "China"),
    ("Suggest a wine for Moroccan lamb tagine with preserved lemons.", "Viognier, Grenache blends, or Moroccan wines from Guerrouane. Should engage with North African flavors.", "cultural_breadth", "non_western_cuisine", 2, "Morocco"),
    ("Tell me about South African Chenin Blanc.", "SA is worlds largest Chenin producer. Called Steen locally. Stellenbosch, Swartland key regions. Old bush vines prized.", "cultural_breadth", "non_european_tradition", 2, "South Africa"),
    ("What wines pair with dim sum?", "Varied dishes need versatile wine. Champagne, dry Riesling, or Gruner Veltliner. Must address steamed to fried range.", "cultural_breadth", "non_western_cuisine", 2, "China"),
    ("What is Koshu and where is it from?", "Japanese indigenous white grape from Yamanashi Prefecture. Light, delicate, citrus notes. Japans most important native variety.", "cultural_breadth", "indigenous_grape", 3, "Japan"),
    ("Tell me about the wines of Uruguay.", "Tannat is signature grape from Madiran France. Canelones and Maldonado main regions. Small but quality-focused.", "cultural_breadth", "emerging_region", 2, "Uruguay"),
    ("What wine for a traditional Mexican mole negro?", "Complex dish needs bold wine: Zinfandel, Malbec, Tempranillo. Must engage with chocolate, chili, spice complexity.", "cultural_breadth", "non_western_cuisine", 3, "Mexico"),
    ("What are orange wines and where did they originate?", "Skin-contact white wines from Georgia qvevri tradition. Now popular in Friuli Italy and Slovenia. Amber color from skin maceration.", "cultural_breadth", "winemaking_tradition", 2, "Georgia"),
    ("Tell me about English sparkling wine.", "Southern England Sussex Kent Hampshire. Same chalk as Champagne. Nyetimber, Ridgeview, Gusbourne. Climate change expanding viability.", "cultural_breadth", "emerging_region", 2, "England"),
    # CONTEXTUAL APPROPRIATENESS - 15 questions
    ("Recommend a wine for a casual summer picnic under $15.", "Must respect budget. Rose from Provence or Languedoc, Vinho Verde, Cava, Beaujolais. Refreshing and easy-drinking. No $50 bottles.", "contextual_appropriateness", "budget_constraint", 1, "general"),
    ("Hosting a formal dinner for my boss with filet mignon. What wine?", "Must match formality. Premium Cab Sauv Napa, classified Bordeaux, or Barolo. Address presentation and impression.", "contextual_appropriateness", "occasion_matching", 2, "general"),
    ("What wine for a vegetarian dinner party?", "Must address dietary constraint. Verify vegetarian-friendly fining. Suggest Pinot Noir, Gruner Veltliner, Vermentino.", "contextual_appropriateness", "dietary_constraint", 2, "general"),
    ("Suggest wine for someone who drinks sweet cocktails and is new to wine.", "Must address beginner palate. Off-dry or fruity: Moscato dAsti, Riesling Kabinett, Lambrusco. Dont jump to dry tannic reds.", "contextual_appropriateness", "experience_level", 1, "general"),
    ("Wine for Thanksgiving when half the guests prefer red, half white?", "Must address group dynamics. Pinot Noir bridges divide, dry Rose works for both, or serve one of each.", "contextual_appropriateness", "group_dynamics", 1, "general"),
    ("Impressive wedding gift wine with aging potential under $100?", "Balance gift context, ageability, budget. Vintage Champagne, classified Bordeaux, or Barolo from good vintage. Mention storage.", "contextual_appropriateness", "gift_occasion", 2, "general"),
    ("What wine at a steakhouse if I dont know much about wine?", "Must be approachable not condescending. Safe picks: Malbec, Cab Sauv, or ask sommelier. OK to not know.", "contextual_appropriateness", "experience_level", 1, "general"),
    ("I need wine for cooking beef stew. What should I use?", "Drinkable but not expensive. Cotes du Rhone, basic Cab or Merlot $8-15. Never use cooking wine label. Dont waste expensive bottles.", "contextual_appropriateness", "practical_constraint", 1, "general"),
    ("Wines for a wine and cheese party for 12 on $150 total budget?", "Must do math: about $12-13 per bottle. Suggest 4-5 bottles with cheese pairings. Mix regions. Respect total budget.", "contextual_appropriateness", "budget_constraint", 2, "general"),
    ("What wine is appropriate for a business lunch in Tokyo?", "Must address cultural context. Sake may be more appropriate. For wine: French or Japanese shows respect. Presentation matters.", "contextual_appropriateness", "cultural_context", 3, "Japan"),
    ("Recommend wine for someone sober-curious or cutting back on alcohol.", "Must address sensitively. Low-alcohol: Moscato dAsti 5.5%, Vinho Verde 9-10%, or dealcoholized wines. Supportive not dismissive.", "contextual_appropriateness", "health_constraint", 2, "general"),
    ("What to order at a French restaurant if the wine list is all in French?", "Must be helpful and empowering. Ask sommelier, explain key terms rouge blanc sec doux, suggest safe picks by region.", "contextual_appropriateness", "experience_level", 1, "France"),
    ("Wine to bring to a potluck where I dont know the food?", "Address uncertainty. Versatile crowd-pleasers: dry Rose, Pinot Noir, Gruner Veltliner, or sparkling. Widest food range.", "contextual_appropriateness", "versatility", 1, "general"),
    ("Recommend a vegan-friendly wine for a dinner party.", "Must address vegan fining agents. Suggest vegan-certified or unfined wines. Name producers like Frey, Bonterra, or natural wine producers.", "contextual_appropriateness", "dietary_constraint", 2, "general"),
    ("What wine for a 21st birthday celebration on a student budget?", "Must respect young adult context and budget. Cava or Prosecco for celebration under $15. Fun and festive over prestigious.", "contextual_appropriateness", "budget_and_occasion", 1, "general"),
]

for i, (inp, exp, dim, qtype, diff, region) in enumerate(questions):
    client.create_example(
        inputs={"question": inp},
        outputs={"expected_answer": exp},
        metadata={"dimension": dim, "difficulty": diff, "type": qtype, "region": region},
        dataset_id=dataset.id,
    )
    print(f"  {i+1}/50: {dim} - {qtype}")

print(f"\nDone! 50 questions uploaded. Dataset total: 100")
