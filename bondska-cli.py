#!/usr/bin/env python3
import sys
import re

# Pitemål (Pite Bondska) Translator CLI
# Version: 2.0 (Authentic Rule-Based Engine)

def translate_word(word):
    original = word
    word = word.lower()

    # 1. Particles & Dictionary (High Priority)
    dictionary = {
        "men": "män", "och": "å", "att": "at", "som": "som",
        "det": "hä", "den": "hä", "de": "döm", "dem": "döm",
        "vi": "ve", "ni": "je", "du": "dö", "dig": "dä", "mig": "mä", "sig": "sä",
        "min": "men", "mitt": "mett", "din": "den", "ditt": "dett",
        "från": "frå", "med": "wä", "till": "täll", "utan": "utan", "vid": "ve",
        "vem": "väm", "vad": "vo", "hur": "vöre", "sverige": "Schwerje",
        "vårt": "wåLt", "vissa": "nager", "trots": "fastän",
        "mycket": "myttje", "aldrig": "aldre", "inte": "int", "eller": "heller"
    }

    if word in dictionary:
        translated = dictionary[word]
        return capitalize_like(original, translated)

    # 2. Suffix Rules (Morphology)
    suffixes = [
        ("heten", "he"), ("het", "he"),
        ("naden", "na"), ("nad", "na"),
        ("ande", "an"),
        ("erna", "a"), ("arna", "a"), ("orna", "a"), # Plural def
        ("en", "n"), ("et", "e") # Singular def
    ]
    
    suffix_changed = False
    for suffix, replacement in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            word = word[:-len(suffix)] + replacement
            suffix_changed = True
            break

    # 3. Verb Apocope (Present Tense)
    # If ends in -ar or -er and didn't match a suffix rule (though -er is rare noun suffix too)
    if not suffix_changed and (word.endswith("ar") or word.endswith("er")) and len(word) > 3:
        word = word[:-2] # Drop the suffix

    # 4. Phonology & Thick L
    # Thick L rules
    word = re.sub(r'rd$', 'L', word)
    word = re.sub(r'rt$', 'Lt', word)
    word = re.sub(r'rn$', 'Rn', word)
    word = re.sub(r'rl$', 'L', word)
    
    # Consonants
    word = re.sub(r'^v', 'w', word)
    word = re.sub(r'sk$', 'sch', word)
    word = re.sub(r'sk(?=[eiyäö])', 'sch', word)
    
    # Vowels
    word = re.sub(r'o(?=[bdfgklmnpstv])', 'u', word) # O -> U mid-word
    word = re.sub(r'a(?=ng|nk)', 'å', word) # A -> Å before nk/ng

    # 5. General Apocope (Final -a)
    if not suffix_changed and word.endswith('a') and len(word) > 3:
        word = word[:-1]

    return capitalize_like(original, word)

def capitalize_like(original, translated):
    if original and original[0].isupper():
        return translated[0].upper() + translated[1:]
    return translated

def main():
    print("NordicVoices | Pitemål CLI v2.0")
    print("Type text to translate. Ctrl+C to exit.\n")
    
    try:
        while True:
            text = input("SV> ")
            if not text: continue
            
            # Split by words but keep delimiters
            tokens = re.split(r'(\s+|[.,!?:;-"\(\)])', text)
            translated_tokens = []
            
            for token in tokens:
                if re.match(r'[a-zA-ZåäöÅÄÖ]', token):
                    translated_tokens.append(translate_word(token))
                else:
                    translated_tokens.append(token)
            
            print(f"PM> {''.join(translated_tokens)}\n")
            
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
