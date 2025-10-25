# Scryfall Card List Generator

Query the Scryfall API to search for Magic: The Gathering cards and export results to CSV or Excel format.

## 🎯 Purpose

This skill enables you to:
- Search for Magic: The Gathering cards using Scryfall's powerful search syntax
- Export search results to CSV or Excel (XLS/XLSX) format
- Customize which card fields to include in the export
- Handle large result sets with automatic pagination
- Get price data, legality information, and card metadata

## 📋 Prerequisites

### Required Python Packages
```bash
pip install requests openpyxl
```

- `requests`: For making HTTP requests to the Scryfall API
- `openpyxl`: For creating Excel files (.xlsx)

### Optional
- Basic familiarity with Magic: The Gathering terminology
- Understanding of Scryfall search syntax (the skill can help with this)

## 🚀 Usage

### Basic Usage

Simply describe what cards you're looking for:

```
"I want to export all red legendary creatures to CSV"
```

```
"Get me a list of all cards in the Dominaria set with prices"
```

```
"Export all counterspells legal in Standard to Excel"
```

### Advanced Usage

Specify exact search parameters and fields:

```
"Search for 'c:blue t:instant cmc<=3' and export to CSV with fields: name, set, mana_cost, oracle_text, prices.usd"
```

### Supported Export Formats

- **CSV** (`.csv`): Comma-separated values, opens in Excel and text editors
- **Excel** (`.xlsx`): Native Excel format with proper formatting

## 🔍 Search Syntax

The skill uses Scryfall's search syntax. Here are common patterns:

### By Color
- `c:red` - Red cards
- `c:wr` - White and red cards
- `c>=bug` - At least blue, black, and green
- `c:c` - Colorless cards

### By Type
- `t:creature` - Creatures
- `t:instant` - Instants
- `t:legendary` - Legendary cards
- `t:"legendary creature"` - Legendary creatures

### By Set
- `set:dom` - Dominaria (use set code)
- `set:war` - War of the Spark
- `e:dom` - Exact set match

### By Rarity
- `r:mythic` - Mythic rare
- `r:rare` - Rare
- `r:uncommon` - Uncommon
- `r:common` - Common

### By Oracle Text
- `o:"draw a card"` - Cards that say "draw a card"
- `o:flying` - Cards with flying
- `o:/draw.*cards/` - Regular expressions

### By Mana Cost
- `cmc=3` - Converted mana cost exactly 3
- `cmc<=2` - CMC 2 or less
- `mv>=5` - Mana value 5 or more
- `m:{2}{u}{u}` - Specific mana cost

### By Power/Toughness
- `pow>=5` - Power 5 or greater
- `tou<=2` - Toughness 2 or less
- `pow=tou` - Power equals toughness

### By Format Legality
- `f:standard` - Legal in Standard
- `f:commander` - Legal in Commander
- `f:modern` - Legal in Modern

### Combinations
Combine multiple criteria:
```
c:blue t:creature cmc<=2 f:standard
```
"Blue creatures with CMC 2 or less that are Standard legal"

## 📊 Available Fields

### Core Fields
- `name` - Card name
- `mana_cost` - Mana cost (e.g., "{2}{U}{U}")
- `cmc` - Converted mana cost (numeric)
- `type_line` - Full type line
- `oracle_text` - Rules text
- `colors` - Color array
- `color_identity` - Color identity

### Set Information
- `set` - Set code
- `set_name` - Full set name
- `collector_number` - Collector number
- `rarity` - Rarity (common/uncommon/rare/mythic)
- `released_at` - Release date

### Creature Stats
- `power` - Power
- `toughness` - Toughness
- `keywords` - Array of keywords

### Prices
- `prices.usd` - Price in USD
- `prices.usd_foil` - Foil price in USD
- `prices.eur` - Price in EUR
- `prices.tix` - MTGO TIX price

### Other
- `artist` - Artist name
- `edhrec_rank` - EDHREC ranking
- `legalities.standard` - Standard legality
- `legalities.commander` - Commander legality
- `scryfall_uri` - Link to Scryfall page
- `image_uris.normal` - Image URL

## 📦 Default Field Sets

The skill provides useful defaults for different use cases:

### Basic (default)
`name, set, rarity, type_line, mana_cost`

### Creatures
`name, set, type_line, mana_cost, power, toughness, rarity`

### Prices
`name, set, rarity, prices.usd, prices.eur, prices.tix`

### Commander
`name, type_line, color_identity, cmc, rarity, edhrec_rank`

### Collection Management
`name, set_name, collector_number, rarity, artist`

## 💡 Examples

See the [examples](./examples/) directory for:
- Sample queries and outputs
- Common use cases
- Advanced filtering techniques
- Custom field configurations

## ⚙️ Configuration

### Rate Limiting
The Scryfall API requests a 50-100ms delay between requests. This skill automatically handles rate limiting.

### Pagination
Results are automatically paginated. The skill will fetch all pages and provide progress updates for large result sets.

### Multi-Face Cards
Cards with multiple faces (e.g., double-faced cards) are handled automatically. The skill can extract data from specific faces if needed.

## 🔧 Troubleshooting

### No Results Found
- Check your search syntax
- Try broader search terms
- Verify set codes and format names

### API Errors
- Wait a moment and retry
- Check your internet connection
- Verify the Scryfall API status

### Missing Prices
- Not all cards have price data
- Prices may be null for unreleased or promotional cards
- Consider using multiple price sources (USD, EUR, TIX)

### Excel Export Issues
- Ensure `openpyxl` is installed
- Check file permissions in the target directory
- Verify you have disk space

## 📚 Resources

- [Scryfall API Documentation](https://scryfall.com/docs/api)
- [Scryfall Search Syntax Guide](https://scryfall.com/docs/syntax)
- [Card Object Reference](https://scryfall.com/docs/api/cards)

## 🤝 Contributing

To improve this skill:
1. Test with various search queries
2. Add more example use cases
3. Suggest additional default field sets
4. Report issues or edge cases

## 📄 License

This skill uses the Scryfall API, which is provided free for non-commercial use. Please review [Scryfall's API Terms](https://scryfall.com/docs/api) before using this skill commercially.

## 🏷️ Tags

`magic-the-gathering` `mtg` `scryfall` `api` `csv` `excel` `data-export` `card-search` `gaming` `collectibles`
