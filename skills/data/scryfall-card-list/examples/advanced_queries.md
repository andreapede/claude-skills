# Advanced Search Queries

This document provides advanced examples of Scryfall search queries for complex card-finding scenarios.

## Table of Contents
1. [Complex Color Combinations](#complex-color-combinations)
2. [Multi-Criteria Filters](#multi-criteria-filters)
3. [Format-Specific Searches](#format-specific-searches)
4. [Price and Market Queries](#price-and-market-queries)
5. [Text and Rules Searches](#text-and-rules-searches)
6. [Collection and Set Queries](#collection-and-set-queries)
7. [Statistical Analysis Queries](#statistical-analysis-queries)

---

## Complex Color Combinations

### Exactly Two Colors
```
c:RG -c:W -c:U -c:B
```
Cards that are exactly red and green (no other colors)

### Colorless Cards Only
```
c:c
```
Truly colorless cards (not just artifacts)

### Mono-Color with Colorless Costs
```
c:R m:{C}
```
Red cards with colorless mana requirements ({C})

### Three-Color Combinations (Shards/Wedges)
```
c:WUB -c:R -c:G
```
Esper cards (White, Blue, Black only)

### Commander Color Identity
```
id:wubr t:legendary
```
Commanders with 4-color identity (no green)

---

## Multi-Criteria Filters

### Budget Commander Staples
```
f:commander edhrec:<=500 usd<3 -t:basic
```
Top 500 EDHREC cards under $3 (excluding basics)

### Efficient Creatures for Limited
```
t:creature cmc<=3 (pow>=2 or tou>=3) r<=uncommon
```
Cheap creatures with good stats at common/uncommon

### Removal Spells
```
(o:destroy o:target or o:exile o:target) t:instant cmc<=3 f:modern
```
Cheap instant-speed removal in Modern

### Card Advantage Engines
```
(o:"draw a card" or o:"draw two" or o:"draw three") -t:land cmc<=4
```
Low-cost card draw effects

---

## Format-Specific Searches

### Standard Meta Cards
```
f:standard (r:rare or r:mythic) usd>5
```
Expensive rares/mythics legal in Standard

### Pioneer Combo Pieces
```
f:pioneer (o:infinite or o:"any number" or o:copy o:spell)
```
Potential combo enablers in Pioneer

### Modern Sideboard Cards
```
f:modern t:instant (o:exile or o:destroy or o:counter) cmc<=3
```
Flexible sideboard options for Modern

### Commander Hidden Gems
```
f:commander usd<1 edhrec:>=5000 (r:rare or r:mythic)
```
Underplayed commander cards with potential

### Pauper Staples
```
f:pauper r:common (o:"draw a card" or o:counter or o:destroy)
```
Common cards that are Pauper-legal

---

## Price and Market Queries

### Best Value Cards
```
edhrec:<=1000 usd<2 (r:rare or r:mythic)
```
Popular commander cards that are cheap

### Recent Price Spikes
```
date>=2024-01 usd>10
```
Cards printed recently that are expensive

### Investment Targets
```
r:mythic is:reserved usd<50
```
Reserved list mythics under $50

### Foil Premium Analysis
```
usd>5 is:foil (usdfoil-usd)>10
```
Cards where foil costs $10+ more than non-foil

### Format Staple Comparison
```
f:modern f:pioneer f:commander usd<10
```
Multi-format staples under $10

---

## Text and Rules Searches

### Keyword Ability Search
```
o:flying o:vigilance o:lifelink t:creature
```
Creatures with multiple keyword abilities

### Mana Ability Search
```
o:"add" o:"{" o:"mana" -t:land
```
Non-land mana sources

### Counter-Related Cards
```
o:"+1/+1 counter" o:"whenever" t:creature
```
Creatures that synergize with +1/+1 counters

### Tribal Support
```
(o:wizard o:"you control" or o:wizard o:card) -t:wizard
```
Cards that support Wizard tribal (but aren't wizards)

### ETB Effects
```
o:"when" o:"enters the battlefield" o:"draw" t:creature cmc<=4
```
Creatures with card draw ETB triggers

### Graveyard Interaction
```
(o:graveyard o:exile or o:graveyard o:return) t:instant cmc<=3
```
Low-cost graveyard hate or recursion

### Stack Interaction
```
o:split o:second
```
Cards referencing the split second mechanic

---

## Collection and Set Queries

### Masterpiece Series
```
is:masterpiece
```
All masterpiece/special showcase cards

### Extended Art Variants
```
is:extendedart set:mh2
```
Extended art cards from Modern Horizons 2

### Full Art Lands
```
t:land is:fullart
```
Full art basic and special lands

### Specific Artist Collection
```
a:"Seb McKinnon"
```
All cards illustrated by Seb McKinnon

### Set Completion Gaps
```
set:mom -is:promo -is:extendedart r:rare
```
Regular rare cards from March of the Machine

### Promo Versions
```
is:promo name:"Lightning Bolt"
```
All promo printings of Lightning Bolt

### First Printings
```
is:firstprint year:2023
```
Cards that debuted in 2023

---

## Statistical Analysis Queries

### Power/Toughness Analysis
```
t:creature pow=tou cmc<=3
```
Creatures with equal power and toughness (low CMC)

### High Power Density
```
t:creature pow>=5 cmc<=4 f:standard
```
Efficient beaters in Standard

### Mana Efficiency
```
t:creature (pow+tou)>=8 cmc<=4
```
Creatures where combined stats are twice the CMC

### Format Legality Comparison
```
-f:standard f:pioneer -is:reprint
```
Cards legal in Pioneer but not Standard (excluding reprints)

### Color Pip Analysis
```
c:U devotion>=3 t:creature
```
Blue creatures with high devotion (UUU or more in cost)

### Rarity Distribution
```
set:one (r:rare or r:mythic) usd<1
```
Bulk rares/mythics from a set

### Release Date Analysis
```
date>=2024-01-01 date<=2024-12-31 r:mythic
```
All mythics released in 2024

---

## Combined Complex Queries

### Commander Deck Brewing
```
id:g t:creature (o:landfall or o:"whenever a land") cmc<=5 edhrec:<=2000
```
Green landfall creatures for Commander

### Budget Modern Deck
```
f:modern usd<2 -t:basic (o:"draw" or o:"search your library")
```
Cheap card advantage for Modern

### Limited Bomb Uncommons
```
r:uncommon (t:planeswalker or (t:creature (pow>=4 or tou>=4)))
```
Powerful uncommons for draft

### Foil Showcase Hunter
```
is:foil is:showcase usd<10 (set:snc or set:neo or set:one)
```
Affordable foil showcase cards from recent sets

### Tribal Commander Options
```
t:legendary t:elf id<=bg
```
Golgari or mono-color legendary elves for commander

---

## Tips for Advanced Searching

### Use Parentheses for Logic
```
(c:R or c:G) t:creature pow>=5
```
Red OR green creatures with power 5+

### Negate with Minus
```
f:standard -f:pioneer
```
Legal in Standard but not in Pioneer

### Comparison Operators
- `=` equal to
- `!=` not equal to
- `<` less than
- `<=` less than or equal
- `>` greater than
- `>=` greater than or equal

### Regular Expressions
```
o:/draw.*cards/
```
Oracle text matching a pattern

### Combine Multiple Criteria
```
c:U t:instant cmc<=2 f:modern usd<1 (o:counter or o:draw)
```
Budget blue interaction for Modern

---

## Performance Notes

- Very broad searches (10,000+ results) will take longer due to pagination
- Price queries are current at the time of search
- Some fields may be null for certain cards (especially older cards)
- Consider using `unique:prints` if you want all printings, or `unique:cards` for unique cards only

---

## Resources

- [Scryfall Syntax Guide](https://scryfall.com/docs/syntax)
- [Card Object Reference](https://scryfall.com/docs/api/cards)
- [Regular Expression Tester](https://regex101.com/)
