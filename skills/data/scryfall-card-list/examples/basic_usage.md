# Basic Usage Examples

This file demonstrates common use cases for the Scryfall Card List Generator skill.

## Example 1: Search by Color and Type

### Request
```
Export all red legendary creatures to CSV
```

### What Happens
- Claude translates to Scryfall query: `c:red t:legendary t:creature`
- Queries the API with pagination
- Uses the "creatures" field preset
- Exports to `red_legendary_creatures.csv`

### Expected Fields
- name
- set
- type_line
- mana_cost
- power
- toughness
- rarity

### Sample Output
```csv
name,set,type_line,mana_cost,power,toughness,rarity
"Zurgo Helmsmasher",ktk,"Legendary Creature — Orc Warrior",{2}{R}{W}{B},7,2,mythic
"Krenko, Mob Boss",m13,"Legendary Creature — Goblin Warrior",{2}{R}{R},3,3,rare
"Purphoros, God of the Forge",ths,"Legendary Enchantment Creature — God",{3}{R},6,5,mythic
```

---

## Example 2: Price List for a Set

### Request
```
Get me all cards from March of the Machine with their prices in Excel format
```

### What Happens
- Scryfall query: `set:mom`
- Uses "prices" field preset
- Exports to `march_of_the_machine_prices.xlsx`

### Expected Fields
- name
- set
- rarity
- prices.usd
- prices.usd_foil
- prices.eur
- prices.tix

### Sample Output
```
| name                    | set | rarity | prices.usd | prices.usd_foil | prices.eur | prices.tix |
|------------------------|-----|--------|------------|-----------------|------------|------------|
| Invasion of Ravnica    | mom | mythic | 25.99      | 32.50           | 24.00      | 15.00      |
| Archangel Elspeth      | mom | mythic | 18.50      | 24.99           | 17.00      | 12.00      |
| Monastery Mentor       | mom | rare   | 8.99       | 12.50           | 8.50       | 5.00       |
```

---

## Example 3: Commander Deck Building

### Request
```
Find all green creatures with CMC 3 or less that are commander legal, export with EDHREC rankings
```

### What Happens
- Scryfall query: `c:green t:creature cmc<=3 f:commander`
- Uses "commander" field preset
- Exports to `green_commander_creatures.csv`

### Expected Fields
- name
- type_line
- color_identity
- cmc
- rarity
- edhrec_rank
- prices.usd

### Sample Output
```csv
name,type_line,color_identity,cmc,rarity,edhrec_rank,prices.usd
"Llanowar Elves","Creature — Elf Druid","G",1,common,45,0.25
"Eternal Witness","Creature — Human Shaman","G",3,uncommon,12,1.99
"Birds of Paradise","Creature — Bird","G",1,rare,8,5.99
```

---

## Example 4: Collection Management

### Request
```
Export all cards I own from Dominaria with collector numbers and artist names
```

### What Happens
- Scryfall query: `set:dom`
- Uses "collection" field preset
- Exports to `dominaria_collection.csv`

### Expected Fields
- name
- set_name
- set
- collector_number
- rarity
- artist
- released_at

### Sample Output
```csv
name,set_name,set,collector_number,rarity,artist,released_at
"Teferi, Hero of Dominaria",Dominaria,dom,207,mythic,"Chris Rallis",2018-04-27
"Lyra Dawnbringer",Dominaria,dom,26,mythic,"Chase Stone",2018-04-27
"Karn, Scion of Urza",Dominaria,dom,1,mythic,"Chris Rallis",2018-04-27
```

---

## Example 5: Standard Format Analysis

### Request
```
Show me all counterspells legal in Standard
```

### What Happens
- Scryfall query: `o:counter o:target o:spell f:standard`
- Uses "basic" field preset
- Exports to `standard_counterspells.csv`

### Expected Fields
- name
- set
- rarity
- type_line
- mana_cost

### Sample Output
```csv
name,set,rarity,type_line,mana_cost
"Counterspell",dmu,uncommon,Instant,{U}{U}
"Negate",mid,common,Instant,{1}{U}
"Make Disappear",snc,common,Instant,{1}{U}
```

---

## Example 6: Custom Fields

### Request
```
Search for all planeswalkers and export with these fields: name, type_line, loyalty, oracle_text, scryfall_uri
```

### What Happens
- Scryfall query: `t:planeswalker`
- Custom field selection
- Exports to `planeswalkers.csv`

### Sample Output
```csv
name,type_line,loyalty,oracle_text,scryfall_uri
"Jace, the Mind Sculptor","Legendary Planeswalker — Jace",3,"+2: Look at the top card...",https://scryfall.com/card/wwk/31
"Liliana of the Veil","Legendary Planeswalker — Liliana",3,"+1: Each player discards...",https://scryfall.com/card/uma/104
```

---

## Example 7: Bulk Price Check

### Request
```
I need prices for all mythic rares released in the last year
```

### What Happens
- Scryfall query: `r:mythic date>=2024-10-25` (dynamically calculated)
- Uses "prices" field preset
- Exports to `recent_mythics_prices.xlsx`

---

## Example 8: Power Level Analysis

### Request
```
Export all creatures with power 10 or greater
```

### What Happens
- Scryfall query: `t:creature pow>=10`
- Uses "creatures" field preset
- Exports to `high_power_creatures.csv`

### Sample Output
```csv
name,set,type_line,mana_cost,power,toughness,rarity
"Emrakul, the Aeons Torn",roe,"Legendary Creature — Eldrazi",{15},15,15,mythic
"Blightsteel Colossus",mbs,"Artifact Creature — Phyrexian Golem",{12},11,11,mythic
"Marit Lage Token",t2xm,"Legendary Creature — Avatar",,,20,20,special
```

---

## Example 9: Format Legality Export

### Request
```
Give me all cards legal in both Standard and Pioneer with legality information
```

### What Happens
- Scryfall query: `f:standard f:pioneer`
- Custom fields including legalities
- Exports to `multi_format_legal.csv`

---

## Example 10: Artist Collection

### Request
```
Show me all cards illustrated by Rebecca Guay
```

### What Happens
- Scryfall query: `a:"Rebecca Guay"`
- Uses "collection" field preset
- Exports to `rebecca_guay_cards.csv`

### Sample Output
```csv
name,set_name,set,collector_number,rarity,artist,released_at
"Path to Exile",con,"Conflux",015,uncommon,"Rebecca Guay",2009-02-06
"Enchantress's Presence",ons,"Onslaught",261,rare,"Rebecca Guay",2002-10-07
```

---

## Tips for Better Results

1. **Be Specific**: More specific queries yield better results
   - Good: `c:blue t:instant cmc<=2 f:standard`
   - Less good: `blue cards`

2. **Use Presets**: Mention a use case to get appropriate fields
   - "for my commander deck" → uses commander preset
   - "with prices" → uses prices preset
   - "for my collection" → uses collection preset

3. **Combine Criteria**: Layer multiple search parameters
   - Color + Type + Format + Price range

4. **Check Examples**: The config.json has preset examples you can reference

5. **Pagination Notice**: Large searches (>175 cards) will take longer due to API rate limiting
