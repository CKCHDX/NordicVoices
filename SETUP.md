# 🚀 Bondska NDPS System - Setup & Usage Guide
## Complete Setup Instructions for the Nordic Dialects Preservation Suite

---

## 🌟 What's Been Created

### Documentation Files
- **README.md** - Project overview and quick start
- **ALPHABET.md** - Complete phonetic guide with IPA reference
- **RULES.md** - All 90+ transformation rules organized by phase
- **LEARNING-GUIDE.md** - 4-phase progression system with exercises
- **EXAMPLES.md** - 50+ real-world translation examples
- **HISTORY.md** - Linguistic history and cultural context
- **SETUP.md** - This file

### Tools & Programs
- **bondska-cli.py** - Command-line tool (Python 3.8+)
- **bondska-translator.html** - Web application (open in any browser)

### Data Files
- **data/vocabulary.json** - 20+ words with phonetics (expandable to 500+)
- **data/rules.json** - 18+ transformation rules database
- **data/examples.json** - 20+ test/learning examples

---

## 🚀 Quick Start (5 minutes)

### Option 1: Web App (Recommended for Beginners)

1. **Download** `bondska-translator.html`
2. **Open** in your web browser (Chrome, Firefox, Safari, Edge)
3. **Start translating** - No installation needed!

```bash
# Or from command line:
open bondska-translator.html          # macOS
start bondska-translator.html         # Windows
xdg-open bondska-translator.html      # Linux
```

**Features Available:**
- 🗙️ Translator tab - Real-time Swedish to Bondska translation
- 🗣️ Alphabet tab - Full pronunciation guide with IPA
- 🗙️ Rules tab - View transformation rules by phase
- 📚 Vocabulary tab - Searchable word dictionary
- 🎓 Learning tab - 4-phase guided learning system
- 📤 Examples tab - 50+ translation examples

### Option 2: Command-Line Tool (Developers)

1. **Requirements:** Python 3.8 or higher
   ```bash
   python3 --version
   ```

2. **Check Python is installed:**
   ```bash
   # If you see a version number, you're good to go!
   # If not, install Python from python.org
   ```

3. **Run the CLI:**
   ```bash
   python3 bondska-cli.py
   ```

4. **See available commands:**
   ```bash
   python3 bondska-cli.py --help
   ```

---

## 💶 Python CLI Tool Usage

### Interactive Mode

```bash
# Start interactive translator
python3 bondska-cli.py

# You'll see:
# 🇸🇪 BONDSKA INTERACTIVE TRANSLATOR
# Commands:
#   translate <text>  - Translate Swedish to Bondska
#   alphabet          - Show alphabet guide
#   rules [phase]     - Show transformation rules
#   examples [phase]  - Show example translations
#   lookup <word>     - Look up a word
#   help              - Show this help message
#   exit              - Exit the program

# Then type commands:
# > translate Jag heter Alex
# > alphabet
# > rules 2
# > examples 1
# > lookup hus
```

### Command Line Mode

```bash
# Translate Swedish text
python3 bondska-cli.py translate "Jag heter Alex"
# Output:
# Swedish:  Jag heter Alex
# Bondska:  ja héter Alex

# Show alphabet guide
python3 bondska-cli.py alphabet

# Show rules for Phase 1-2
python3 bondska-cli.py rules 2

# Show example translations
python3 bondska-cli.py examples 3

# Look up a word
python3 bondska-cli.py lookup hus

# Get help
python3 bondska-cli.py --help
```

---

## 🌏 Web App Features

### Translator Tab
- **Input:** Type any Swedish text
- **Phase Selector:** Choose learning phase (1-4)
- **Output:** See Bondska translation in real-time
- **Copy Button:** Save translations to clipboard

### Alphabet Tab
- **Consonants:** All Bondska consonants with IPA
- **Vowels:** All Bondska vowels with pronunciation
- **Sound Characteristics:** Unique features of Bondska phonology
- **Examples:** Each letter with real word examples

### Rules Tab
- **Phase 1:** Pronoun shift rules
- **Phase 2:** Vowel transformation rules
- **Phase 3:** Apocope and consonant changes
- **Phase 4:** Grammar and advanced features

### Vocabulary Tab
- **Search:** Find words in English or Swedish
- **Dictionary:** 20+ words with IPA and translations
- **Categories:** Nouns, verbs, adjectives, pronouns, particles

### Learning Tab
- **Phase 1:** Pronouns and basic substitutions (Week 1)
- **Phase 2:** Vowel shifts (Week 2)
- **Phase 3:** Apocope and consonants (Week 3)
- **Phase 4:** Grammar and fluency (Week 4+)
- **Exercises:** Practice tasks for each phase

### Examples Tab
- **50+ Translations:** Real-world Swedish to Bondska
- **Filtered By Phase:** Focus on specific learning level
- **Categories:** Greetings, questions, statements, negation, etc.

---

## 📚 Documentation Guide

### For Learners

1. **Start with:** README.md (overview)
2. **Then read:** LEARNING-GUIDE.md (4-phase system)
3. **Reference:** ALPHABET.md (pronunciation)
4. **Practice:** EXAMPLES.md (50+ sentences)
5. **Understand:** RULES.md (why rules work)

### For Developers

1. **Architecture:** Check data/ directory (JSON files)
2. **Integration:** See bondska-cli.py structure
3. **Expansion:** Add more entries to vocabulary.json
4. **Customization:** Modify bondska-translator.html

### For Linguists

1. **History:** Read HISTORY.md
2. **Rules:** Study RULES.md in detail
3. **Phonetics:** Reference ALPHABET.md
4. **Validation:** Check EXAMPLES.md for accuracy

---

## 📊 Data Files Guide

### vocabulary.json Structure

```json
{
  "swedish": "hus",
  "bondska": "hus",
  "ipa": "[hʉːs]",
  "english": "house",
  "category": "noun",
  "phase": 1,
  "frequency": 5,
  "notes": "No change needed"
}
```

### rules.json Structure

```json
{
  "id": "p1_pronoun_jag",
  "phase": 1,
  "pattern": "\\bjag\\b",
  "replacement": "ja",
  "explanation": "First person pronoun reduction",
  "examples": ["Jag heter" → "ja héter"],
  "exceptions": "None"
}
```

### examples.json Structure

```json
{
  "phase": 1,
  "swedish": "Jag heter Alex",
  "bondska": "ja héter Alex",
  "english": "My name is Alex",
  "category": "greeting",
  "rules": ["jag → ja"]
}
```

---

## 🔧 Expansion Guide

### Add More Vocabulary

1. **Open:** `data/vocabulary.json`
2. **Add entry:**
   ```json
   {
     "swedish": "mår",
     "bondska": "mår",
     "ipa": "[måːr]",
     "english": "month",
     "category": "noun",
     "phase": 2,
     "frequency": 3,
     "notes": "No change in Bondska"
   }
   ```
3. **Save and test** with the translator

### Add More Rules

1. **Open:** `data/rules.json`
2. **Add rule:**
   ```json
   {
     "id": "p2_vowel_y_to_o",
     "phase": 2,
     "pattern": "y",
     "replacement": "ö",
     "explanation": "Y vowel shift in some contexts",
     "examples": ["ny" → "nö"],
     "exceptions": "Variable - use carefully"
   }
   ```
3. **Test** with example sentences

### Add Examples

1. **Open:** `data/examples.json`
2. **Add example:**
   ```json
   {
     "phase": 2,
     "swedish": "Min mor leker",
     "bondska": "Mín mör läker",
     "english": "My mother plays",
     "category": "statement",
     "rules": ["min → mín", "o → ö", "e → ä"]
   }
   ```
3. **Reload** the web app to see it

---

## 🔠 Troubleshooting

### Web App Issues

**Problem:** Page won't load in browser
- **Solution:** Ensure file is saved as `.html` and opened with a web browser
- **Check:** Make sure JavaScript is enabled in your browser

**Problem:** Translator not working
- **Solution:** Check that data files exist in `data/` directory
- **Check:** Browser console for errors (F12 > Console tab)

**Problem:** Data not showing
- **Solution:** Reload the page (Ctrl+R or Cmd+R)
- **Check:** Data files are in JSON format without errors

### Python CLI Issues

**Problem:** "python3 not found"
- **Solution:** Install Python 3.8+ from python.org
- **Check:** `python3 --version` should show version number

**Problem:** "No module named 'json'"
- **Solution:** This is built-in - check your Python installation
- **Check:** Try `python3 -c "import json; print('OK')"`

**Problem:** Data files not loading
- **Solution:** Ensure `data/` directory exists with JSON files
- **Check:** Run from the directory containing `bondska-cli.py`

### General Troubleshooting

**Check file structure:**
```
Bondska/
  README.md
  ALPHABET.md
  RULES.md
  LEARNING-GUIDE.md
  EXAMPLES.md
  HISTORY.md
  bondska-cli.py
  bondska-translator.html
  data/
    vocabulary.json
    rules.json
    examples.json
```

---

## 🏃 Getting Started Steps

### Day 1: Try the Tools

1. Open `bondska-translator.html` in browser
2. Translate: "Jag heter Alex"
3. Click Alphabet tab - see phonetics
4. Try Python: `python3 bondska-cli.py translate "Hej"`

### Day 2: Learn Phase 1

1. Read LEARNING-GUIDE.md - Phase 1
2. Study EXAMPLES.md examples 1-15
3. Practice with web app Translator
4. Try exercises from LEARNING-GUIDE.md

### Day 3-4: Learn Phases 2-4

1. Advance one phase per day
2. Read corresponding section in LEARNING-GUIDE.md
3. Study relevant EXAMPLES.md
4. Practice in translator

### Day 5+: Fluency Work

1. Read HISTORY.md for context
2. Study RULES.md for understanding
3. Practice conversations with examples
4. Create your own sentences

---

## 🙋 Contributing

### How to Help

1. **Add Words:** Contribute authentic Bondska vocabulary
2. **Improve Rules:** Refine transformation algorithms
3. **Create Examples:** Write real Bondska sentences
4. **Record Audio:** Contribute pronunciations
5. **Fix Bugs:** Report issues and suggest improvements

### Contributing Workflow

1. Make changes locally
2. Test with both tools
3. Commit: `git commit -m "Add 20 new Bondska words"`
4. Push: `git push origin Bondska`
5. Create pull request to main branch

---

## 📜 License & Attribution

**License:** MIT License - Free to use, modify, and distribute

**How to Cite:**
```
Bondska Translator. Nordic Dialects Preservation Suite (NDPS).
Version 1.0, December 2025.
https://github.com/CKCHDX/NordicVoices
```

---

## 🙏 Support & Resources

### Documentation
- **Main Guide:** README.md
- **Learning:** LEARNING-GUIDE.md
- **Pronunciation:** ALPHABET.md
- **Rules:** RULES.md
- **History:** HISTORY.md

### External Resources
- **ISOF:** https://www.isof.se (Swedish Language Institute)
- **University of Umeå:** Regional research center
- **Västerbottens Museum:** Cultural heritage

### Community
- **GitHub Issues:** Report bugs, suggest features
- **GitHub Discussions:** Ask questions, share knowledge
- **Social Media:** @NordicDialects

---

## 🚀 Next Steps

**What to do now:**

1. ✅ Open `bondska-translator.html` in your browser
2. ✅ Try translating: "Hej! Jag heter..." (Hi! I'm...)
3. ✅ Read Phase 1 in LEARNING-GUIDE.md
4. ✅ Practice the exercises
5. ✅ Share your progress with others!

**Your Bondska journey starts today!**

---

**Last Updated:** December 2025 | **Version:** 1.0 | **Maintained by:** Bondska Revival Project

🇸🇪 *"Hald fram Bondska!"* (Keep Bondska alive!)