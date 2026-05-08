import json

# 1. Load data directly from the current folder
with open('pokedex.json', 'r', encoding='utf-8') as f:
    pokedex = json.load(f)

with open('type_chart.json', 'r', encoding='utf-8') as f:
    type_chart = json.load(f)

print("--- Pokémon Calculator ---")

while True:
    # 2. Get user input
    name = input("\nEnter name (or 'q' to quit): ").strip().lower()

    if name == 'q':
        break

    # 3. Find Pokémon (Matches fanzeyi's ['name']['english'] structure)
    pokemon = next((p for p in pokedex if p['name']['english'].lower() == name), None)

    if not pokemon:
        print("Not found! Try again.")
        continue

    # 4. Calculate
    pkmn_types = pokemon['type'] # e.g. ["Grass", "Poison"]
    weak, resist, immune = [], [], []

    for attacker, multipliers in type_chart.items():
        score = 1.0
        for p_type in pkmn_types:
            # Matches type case to your chart (e.g., "Fire")
            score *= multipliers.get(p_type, 1.0)

        if score > 1: weak.append(f"{attacker} ({score}x)")
        elif score == 0: immune.append(attacker)
        elif score < 1: resist.append(f"{attacker} ({score}x)")

    # 5. Output
    print(f"Types: {'/'.join(pkmn_types)}")
    print(f"Weak: {', '.join(weak)}")
    print(f"Resist: {', '.join(resist)}")
    if immune: print(f"Immune: {', '.join(immune)}")
