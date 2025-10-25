#!/usr/bin/env python3
"""
Scryfall Card List Generator - Python Implementation Example

This script demonstrates how to query the Scryfall API and export results
to CSV or Excel format.

Requirements:
    pip install requests openpyxl
"""

import requests
import time
import csv
import json
from typing import List, Dict, Any, Optional
from pathlib import Path


class ScryfallCardExporter:
    """Export Magic: The Gathering cards from Scryfall API to CSV/Excel."""

    BASE_URL = "https://api.scryfall.com"
    RATE_LIMIT_DELAY = 0.1  # 100ms between requests

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'ScryfallCardExporter/1.0'
        })

    def search_cards(
        self,
        query: str,
        order: str = "name",
        unique: str = "cards",
        include_extras: bool = False
    ) -> List[Dict[str, Any]]:
        """
        Search for cards using Scryfall API.

        Args:
            query: Scryfall search query
            order: Sort order (name, set, released, etc.)
            unique: Uniqueness strategy (cards, art, prints)
            include_extras: Include extra cards (tokens, etc.)

        Returns:
            List of card dictionaries
        """
        url = f"{self.BASE_URL}/cards/search"
        params = {
            "q": query,
            "order": order,
            "unique": unique,
            "include_extras": str(include_extras).lower()
        }

        all_cards = []
        page = 1

        print(f"Searching for: {query}")

        while True:
            response = self.session.get(url, params=params)

            if response.status_code != 200:
                error_data = response.json()
                raise Exception(f"API Error: {error_data.get('details', 'Unknown error')}")

            data = response.json()

            if data.get("object") == "error":
                raise Exception(f"Search Error: {data.get('details', 'Unknown error')}")

            # Add cards from this page
            cards = data.get("data", [])
            all_cards.extend(cards)

            print(f"  Page {page}: {len(cards)} cards (Total: {len(all_cards)})")

            # Check if there are more pages
            if not data.get("has_more", False):
                break

            # Get next page URL
            url = data.get("next_page")
            params = None  # Next page URL includes all params
            page += 1

            # Rate limiting
            time.sleep(self.RATE_LIMIT_DELAY)

        print(f"Found {len(all_cards)} total cards\n")
        return all_cards

    def extract_field(self, card: Dict[str, Any], field: str) -> Any:
        """
        Extract a field from a card object, supporting nested fields.

        Args:
            card: Card dictionary
            field: Field name (supports dot notation like 'prices.usd')

        Returns:
            Field value or empty string if not found
        """
        if "." in field:
            # Handle nested fields
            keys = field.split(".")
            value = card
            for key in keys:
                if isinstance(value, dict):
                    value = value.get(key, "")
                else:
                    return ""
            return value
        else:
            # Handle card_faces for double-faced cards
            if field in ["oracle_text", "mana_cost", "type_line"] and field not in card:
                if "card_faces" in card and len(card["card_faces"]) > 0:
                    # Get from first face
                    return card["card_faces"][0].get(field, "")
            return card.get(field, "")

    def format_value(self, value: Any) -> str:
        """Format a value for CSV/Excel export."""
        if value is None:
            return ""
        elif isinstance(value, list):
            return ", ".join(str(v) for v in value)
        elif isinstance(value, dict):
            return json.dumps(value)
        else:
            return str(value)

    def export_to_csv(
        self,
        cards: List[Dict[str, Any]],
        output_file: str,
        fields: List[str]
    ) -> None:
        """
        Export cards to CSV file.

        Args:
            cards: List of card dictionaries
            output_file: Output CSV file path
            fields: List of field names to include
        """
        output_path = Path(output_file)

        with output_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()

            for card in cards:
                row = {}
                for field in fields:
                    value = self.extract_field(card, field)
                    row[field] = self.format_value(value)
                writer.writerow(row)

        print(f"Exported {len(cards)} cards to {output_file}")

    def export_to_excel(
        self,
        cards: List[Dict[str, Any]],
        output_file: str,
        fields: List[str]
    ) -> None:
        """
        Export cards to Excel file.

        Args:
            cards: List of card dictionaries
            output_file: Output Excel file path
            fields: List of field names to include
        """
        try:
            from openpyxl import Workbook
        except ImportError:
            raise Exception("openpyxl is required for Excel export. Install with: pip install openpyxl")

        wb = Workbook()
        ws = wb.active
        ws.title = "Cards"

        # Write headers
        ws.append(fields)

        # Write data
        for card in cards:
            row = []
            for field in fields:
                value = self.extract_field(card, field)
                row.append(self.format_value(value))
            ws.append(row)

        # Auto-adjust column widths
        for column in ws.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = min(max_length + 2, 50)
            ws.column_dimensions[column_letter].width = adjusted_width

        wb.save(output_file)
        print(f"Exported {len(cards)} cards to {output_file}")


# Field presets
FIELD_PRESETS = {
    "basic": ["name", "set", "rarity", "type_line", "mana_cost"],
    "creatures": ["name", "set", "type_line", "mana_cost", "power", "toughness", "rarity"],
    "prices": ["name", "set", "rarity", "prices.usd", "prices.usd_foil", "prices.eur", "prices.tix"],
    "commander": ["name", "type_line", "color_identity", "cmc", "rarity", "edhrec_rank", "prices.usd"],
    "collection": ["name", "set_name", "set", "collector_number", "rarity", "artist", "released_at"],
}


def main():
    """Example usage of the ScryfallCardExporter."""

    exporter = ScryfallCardExporter()

    # Example 1: Export red legendary creatures to CSV
    print("=" * 60)
    print("Example 1: Red Legendary Creatures")
    print("=" * 60)

    cards = exporter.search_cards("c:red t:legendary t:creature")
    exporter.export_to_csv(
        cards,
        "red_legendary_creatures.csv",
        FIELD_PRESETS["creatures"]
    )

    # Show preview
    print("\nPreview of first 5 cards:")
    for i, card in enumerate(cards[:5]):
        print(f"  {i+1}. {card.get('name')} ({card.get('set').upper()}) - {card.get('mana_cost', 'N/A')}")

    print("\n")

    # Example 2: Export cards from a set with prices to Excel
    print("=" * 60)
    print("Example 2: March of the Machine Prices")
    print("=" * 60)

    cards = exporter.search_cards("set:mom")
    exporter.export_to_excel(
        cards,
        "march_of_the_machine_prices.xlsx",
        FIELD_PRESETS["prices"]
    )

    print("\n")

    # Example 3: Custom fields - counterspells in Standard
    print("=" * 60)
    print("Example 3: Standard Counterspells")
    print("=" * 60)

    custom_fields = ["name", "set", "mana_cost", "oracle_text", "rarity", "prices.usd"]

    cards = exporter.search_cards("o:counter o:target o:spell f:standard")
    exporter.export_to_csv(
        cards,
        "standard_counterspells.csv",
        custom_fields
    )

    print("\n")

    # Example 4: Commander staples under $5
    print("=" * 60)
    print("Example 4: Budget Commander Staples")
    print("=" * 60)

    cards = exporter.search_cards("f:commander usd<5 edhrec:<=1000")
    exporter.export_to_excel(
        cards,
        "budget_commander_staples.xlsx",
        FIELD_PRESETS["commander"]
    )

    print("\n")
    print("All exports completed successfully!")


if __name__ == "__main__":
    main()
