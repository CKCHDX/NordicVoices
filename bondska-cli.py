#!/usr/bin/env python3
"""
Bondska CLI Tool - Västerbottnian Dialect Translator
Nordic Dialects Preservation Suite (NDPS)
Version 1.0
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


class BondskaTranslator:
    """Bondska Swedish dialect translator"""

    def __init__(self):
        """Initialize the translator with data files"""
        self.data_dir = Path(__file__).parent / "data"
        self.vocabulary = {}
        self.rules = {}
        self.examples = []
        self.load_data()

    def load_data(self):
        """Load vocabulary, rules, and examples from JSON files"""
        try:
            # Load vocabulary
            vocab_file = self.data_dir / "vocabulary.json"
            if vocab_file.exists():
                with open(vocab_file, 'r', encoding='utf-8') as f:
                    vocab_data = json.load(f)
                    for word in vocab_data.get('words', []):
                        self.vocabulary[word['swedish']] = word

            # Load rules
            rules_file = self.data_dir / "rules.json"
            if rules_file.exists():
                with open(rules_file, 'r', encoding='utf-8') as f:
                    rules_data = json.load(f)
                    self.rules = {rule['id']: rule for rule in rules_data.get('rules', [])}

            # Load examples
            examples_file = self.data_dir / "examples.json"
            if examples_file.exists():
                with open(examples_file, 'r', encoding='utf-8') as f:
                    examples_data = json.load(f)
                    self.examples = examples_data.get('examples', [])
        except Exception as e:
            print(f"Warning: Could not load data files: {e}")

    def translate(self, swedish_text: str, phase: int = 3) -> str:
        """Translate Swedish text to Bondska"""
        if not swedish_text.strip():
            return ""

        words = swedish_text.split()
        result = []

        for word in words:
            bondska_word = self._translate_word(word, phase)
            result.append(bondska_word)

        return " ".join(result)

    def _translate_word(self, word: str, phase: int) -> str:
        """Translate a single word"""
        # Check if word exists in vocabulary
        if word.lower() in self.vocabulary:
            vocab_entry = self.vocabulary[word.lower()]
            if vocab_entry['phase'] <= phase:
                # Preserve case
                bondska = vocab_entry['bondska']
                if word[0].isupper():
                    bondska = bondska[0].upper() + bondska[1:]
                return bondska

        # Apply transformation rules
        result = word
        for rule_id, rule in self.rules.items():
            if rule['phase'] <= phase:
                pattern = rule['pattern']
                replacement = rule['replacement']
                result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)

        return result

    def get_alphabet(self) -> str:
        """Return Bondska alphabet guide"""
        alphabet = """
🇣️ BONDSKA ALPHABET & PRONUNCIATION

CONSONANTS:
B [b] - like English 'b'
D [d] - like English 'd'
F [f] - like English 'f'
G [g] - like English 'g' (hard)
H [h] - like English 'h'
J [j] - like English 'y' in 'yes'
K [k] - like English 'k'
L [l] - like English 'l'
M [m] - like English 'm'
N [n] - like English 'n'
P [p] - like English 'p'
R [r̤] - RETROFLEX R (characteristic of Bondska)
S [s] - like English 's'
SK [ʂ] - retroflexed 'sh' sound
T [t] - like English 't'
V [v] - like English 'v'

VOWELS:
A [aː] - like 'a' in 'father'
Ä [ɛː] - like 'a' in 'strangle'
Å [åː] - like 'o' in 'sport' (rounded)
E [eː] - like 'ay' without the 'y'
I [iː] - like 'ee' in 'feet'
O [uː] - like 'oo' in 'boot'
Ö [œː] - like French 'eu'
U [uː] - like 'oo' in 'boot'
Y [yː] - like French 'tu'
        """
        return alphabet.strip()

    def get_rules_summary(self, phase: int = None) -> str:
        """Get summary of transformation rules"""
        output = ""
        output += "\n🗙️ BONDSKA TRANSFORMATION RULES\n"
        output += "=" * 50 + "\n"

        for rule_id, rule in self.rules.items():
            if phase is None or rule['phase'] <= phase:
                output += f"\nPhase {rule['phase']}: {rule['name']}\n"
                output += f"  Pattern: {rule['pattern']} → {rule['replacement']}\n"
                output += f"  Explanation: {rule['explanation']}\n"
                if rule.get('examples'):
                    output += f"  Examples: {', '.join(rule['examples'])}\n"

        return output

    def lookup_word(self, word: str) -> str:
        """Look up a word in the dictionary"""
        word_lower = word.lower()
        if word_lower in self.vocabulary:
            entry = self.vocabulary[word_lower]
            output = f"""
📚 WORD LOOKUP: {entry['swedish']}

Bondska:   {entry['bondska']}
IPA:       {entry['ipa']}
English:   {entry['english']}
Category:  {entry['category']}
Phase:     {entry['phase']}
Frequency: {entry['frequency']}/5
Notes:     {entry['notes']}
            """
            return output.strip()
        else:
            return f"Word '{word}' not found in dictionary."

    def show_examples(self, phase: int = None) -> str:
        """Show example translations"""
        output = "\n📤 BONDSKA EXAMPLES\n"
        output += "=" * 70 + "\n"

        for example in self.examples:
            if phase is None or example['phase'] <= phase:
                output += f"\nSwedish:  {example['swedish']}\n"
                output += f"Bondska:  {example['bondska']}\n"
                output += f"English:  {example['english']}\n"
                output += f"Phase:    {example['phase']} | Category: {example['category']}\n"
                output += "-" * 70

        return output

    def interactive_mode(self):
        """Run interactive translation mode"""
        print("""
🇸🇪 BONDSKA INTERACTIVE TRANSLATOR
Nordic Dialects Preservation Suite (NDPS)

Commands:
  translate <text>  - Translate Swedish to Bondska
  alphabet          - Show alphabet guide
  rules [phase]     - Show transformation rules
  examples [phase]  - Show example translations
  lookup <word>     - Look up a word
  help              - Show this help message
  exit              - Exit the program
        """)

        while True:
            try:
                user_input = input("\n> ").strip()
                if not user_input:
                    continue

                if user_input.lower() == "exit":
                    print("\n*Hald fram Bondska!* (Keep Bondska alive!)\n")
                    break

                elif user_input.lower() == "alphabet":
                    print(self.get_alphabet())

                elif user_input.lower().startswith("rules"):
                    parts = user_input.split()
                    phase = int(parts[1]) if len(parts) > 1 else None
                    print(self.get_rules_summary(phase))

                elif user_input.lower().startswith("examples"):
                    parts = user_input.split()
                    phase = int(parts[1]) if len(parts) > 1 else None
                    print(self.show_examples(phase))

                elif user_input.lower().startswith("lookup"):
                    word = user_input[6:].strip()
                    print(self.lookup_word(word))

                elif user_input.lower().startswith("translate"):
                    text = user_input[9:].strip()
                    result = self.translate(text)
                    print(f"\nSwedish:  {text}")
                    print(f"Bondska:  {result}")

                elif user_input.lower() == "help":
                    print("Use 'translate <text>' to translate, 'alphabet' for pronunciation, etc.")

                else:
                    # Assume it's a translation request
                    result = self.translate(user_input)
                    print(f"\nSwedish:  {user_input}")
                    print(f"Bondska:  {result}")

            except KeyboardInterrupt:
                print("\n\n*Hald fram Bondska!*\n")
                break
            except Exception as e:
                print(f"Error: {e}")


def main():
    """Main entry point"""
    translator = BondskaTranslator()

    if len(sys.argv) < 2:
        # Interactive mode
        translator.interactive_mode()
    else:
        command = sys.argv[1].lower()

        if command == "translate" and len(sys.argv) > 2:
            text = " ".join(sys.argv[2:])
            result = translator.translate(text)
            print(f"Swedish:  {text}")
            print(f"Bondska:  {result}")

        elif command == "alphabet":
            print(translator.get_alphabet())

        elif command == "rules":
            phase = int(sys.argv[2]) if len(sys.argv) > 2 else None
            print(translator.get_rules_summary(phase))

        elif command == "examples":
            phase = int(sys.argv[2]) if len(sys.argv) > 2 else None
            print(translator.show_examples(phase))

        elif command == "lookup" and len(sys.argv) > 2:
            word = sys.argv[2]
            print(translator.lookup_word(word))

        elif command == "--help" or command == "-h":
            print("""
Bondska CLI Tool - Västerbottnian Dialect Translator

Usage:
  python3 bondska-cli.py translate <text>    Translate Swedish to Bondska
  python3 bondska-cli.py alphabet             Show alphabet guide
  python3 bondska-cli.py rules [phase]        Show transformation rules
  python3 bondska-cli.py examples [phase]     Show example translations
  python3 bondska-cli.py lookup <word>        Look up a word
  python3 bondska-cli.py                      Start interactive mode

Examples:
  python3 bondska-cli.py translate "Jag heter Alex"
  python3 bondska-cli.py alphabet
  python3 bondska-cli.py rules 1
  python3 bondska-cli.py lookup hus

For interactive mode with more options, run without arguments.
            """)
        else:
            print("Unknown command. Use --help for usage information.")
            sys.exit(1)


if __name__ == "__main__":
    main()
