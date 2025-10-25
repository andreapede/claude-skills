# Scryfall Card List Examples

This directory contains practical examples demonstrating how to use the Scryfall Card List Generator skill.

## 📁 Files

### `basic_usage.md`
Common use cases with step-by-step examples:
- Searching by color and type
- Price lists for sets
- Commander deck building
- Collection management
- Format legality checks
- Custom field selection

### `python_implementation.py`
Complete Python implementation showing:
- API integration with rate limiting
- CSV export functionality
- Excel export with formatting
- Field extraction and formatting
- Pagination handling
- Multiple working examples

**To run:**
```bash
pip install requests openpyxl
python python_implementation.py
```

### `advanced_queries.md`
Advanced search techniques including:
- Complex color combinations
- Multi-criteria filters
- Format-specific searches
- Price and market analysis
- Text and rules searches
- Collection queries
- Statistical analysis

## 🚀 Quick Start

### Example 1: Simple Search
Ask Claude:
```
Export all blue instants in Standard to CSV
```

### Example 2: Price Check
Ask Claude:
```
Get prices for all mythics in March of the Machine
```

### Example 3: Commander Deck
Ask Claude:
```
Find green creatures with CMC 3 or less for Commander with EDHREC rankings
```

## 💡 Tips

1. **Start Simple**: Begin with basic searches before moving to complex queries
2. **Use Presets**: Mention your use case (commander, prices, collection) for appropriate defaults
3. **Review Samples**: Claude will show you a preview before exporting
4. **Iterate**: Refine your search based on the preview results

## 📚 Additional Resources

- [Scryfall Search Syntax](https://scryfall.com/docs/syntax)
- [API Documentation](https://scryfall.com/docs/api)
- Parent [README.md](../README.md) for full documentation
