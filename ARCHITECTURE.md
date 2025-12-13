# Architecture & System Design

## Nordic Dialects Preservation Suite - Technical Architecture

This document describes the system architecture, standardized patterns, and design principles used across all dialect implementations.

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Core Components](#core-components)
3. [Translation Pipeline](#translation-pipeline)
4. [File Structure (Per Dialect)](#file-structure-per-dialect)
5. [Data Formats](#data-formats)
6. [Standardized Tools](#standardized-tools)
7. [Integration Points](#integration-points)
8. [Scalability & Maintenance](#scalability--maintenance)

---

## System Overview

### Design Philosophy

The Nordic Dialects suite uses a **modular, template-based architecture** where:

1. **Each dialect is independent**: Complete, self-contained implementation on its own branch
2. **Templates are shared**: Common patterns, tools, and documentation formats across all dialects
3. **Standards are enforced**: Consistent phonetic conventions, rule structures, and learning systems
4. **Extensibility is built-in**: Easy to add new dialects using existing templates

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│             Nordic Dialects Preservation Suite          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Main Branch (shared/)                           │  │
│  │  - Master README                                │  │
│  │  - Contributing Guidelines                      │  │
│  │  - Shared Templates                             │  │
│  │  - Phonetic Standards                           │  │
│  │  - Architecture Documentation                   │  │
│  └──────────────────────────────────────────────────┘  │
│                         ▲                               │
│                         │ (references)                  │
│                         │                               │
│  ┌──────────┬──────────┬──────────┬──────────┐         │
│  │          │          │          │          │         │
│  ▼          ▼          ▼          ▼          ▼         │
│ ┌───┐    ┌───┐     ┌───┐     ┌───┐     ┌───┐         │
│ │   │    │   │     │   │     │   │     │   │         │
│ │Bon│    │Gut│    │Elf│    │Jam│    │...│         │
│ │dsk│    │nis│    │dal│    │tsk│    │   │         │
│ │a  │    │h  │    │sk │    │a  │    │   │         │
│ │   │    │   │     │   │     │   │     │   │         │
│ └───┘    └───┘     └───┘     └───┘     └───┘         │
│  [Dialect Branches - Each with tools, docs, data]     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Core Components

### 1. Web Translator Application

**File**: `[dialect]-translator.html`

**Purpose**: Interactive, browser-based translation tool

**Technology**: HTML5 + CSS3 + JavaScript (vanilla, no frameworks)

**Architecture**:
```
HTML Structure:
├── Header (branding, navigation)
├── Main Content Area
│   ├── Input Panel (Swedish textarea)
│   ├── Output Panel (Dialect textarea)
│   └── Tab Navigation
│       ├── Transformation Rules
│       ├── Alphabet & Phonetics
│       ├── Key Vocabulary
│       └── Learning Guide
└── Footer (links, credits)

JavaScript Logic:
├── Translation Engine
│   ├── Rule Manager (phonetic rules)
│   ├── Vocabulary Mapper (word substitutions)
│   ├── Grammar Processor (special cases)
│   └── Output Formatter
├── UI Controller
│   ├── Tab Manager
│   ├── Text Handler
│   ├── Copy Manager
│   └── Storage Manager
└── Utilities
    ├── Regex Processor
    ├── Text Normalizer
    └── Error Handler

CSS Design System:
├── Root Variables (colors, spacing, typography)
├── Layout Components (card, grid, flex)
├── Interactive Elements (buttons, inputs, tabs)
└── Responsive Design (mobile, tablet, desktop)
```

**Key Features**:
- ✅ No external dependencies
- ✅ Offline functionality
- ✅ Mobile-responsive
- ✅ Copy-to-clipboard
- ✅ Real-time translation
- ✅ Integrated learning guides

### 2. Command-Line Interface Tool

**File**: `[dialect]-cli.py`

**Purpose**: Terminal-based translator and rule inspector

**Technology**: Python 3.8+

**Architecture**:
```
Python Structure:
├── Main Class (CLI Manager)
│   └── BondskaCLI
│       ├── print_banner()
│       ├── print_help()
│       ├── run_interactive()
│       └── run_batch()
│
├── Translation Engine
│   └── [Dialect]Normalizer
│       ├── __init__() [load rules]
│       ├── apply_rule_a() [vowel shifts]
│       ├── apply_rule_b() [apocope]
│       ├── apply_rule_c() [consonants]
│       ├── apply_rule_d() [pronouns]
│       ├── apply_rule_e() [vocabulary]
│       └── translate_to_dialect()
│
├── Data Layer
│   ├── vowel_shifts (dict)
│   ├── consonant_shifts (dict)
│   ├── apocope_rules (dict)
│   ├── pronouns_and_words (dict)
│   └── key_vocabulary (dict)
│
└── Utilities
    ├── get_transformation_log()
    ├── validate_input()
    └── format_output()
```

**Command Interface**:
```bash
# Interactive mode
python3 [dialect]-cli.py

# Batch operations
python3 [dialect]-cli.py translate "Text"
python3 [dialect]-cli.py alphabet
python3 [dialect]-cli.py rules
python3 [dialect]-cli.py examples
python3 [dialect]-cli.py history
```

---

## Translation Pipeline

### Rule Application Order (CRITICAL)

Rules are applied sequentially. **Order matters because earlier rules affect later ones**.

```
Input: "Jag måste gå hem och äta gröt"
  │
  ├─→ Step 1: Pronouns & Basic Words
  │   Jag → I, måste (pending), gå → gå, hem → hem, och → å, äta → äta, gröt → gröt
  │   Output: "I måste gå hem å äta gröt"
  │
  ├─→ Step 2: Key Vocabulary
  │   måste → gatt, gå → gå, hem → hem, äta → äta, gröt → gröt
  │   Output: "I gatt gå hem å äta gröt"
  │
  ├─→ Step 3: Vowel Shifts
  │   gatt (no shift), gå → gaa, hem → heim, äta → äta, gröt → grayt
  │   Output: "I gatt gaa heim å äta grayt"
  │
  ├─→ Step 4: Consonant Shifts
  │   (no soft K/G/Sk in this example)
  │   Output: "I gatt gaa heim å äta grayt"
  │
  ├─→ Step 5: Apocope (Final)
  │   äta → ät (drop -a)
  │   Output: "I gatt gaa heim å ät grayt"
  │
  └─→ Output: "I gatt gaa heim å ät grayt"
```

### Why Order Matters

```
❌ WRONG ORDER: Apply Apocope first
   "äta" → "ät" → then vocabulary rules don't find "äta"

✅ RIGHT ORDER: Vocabulary → Apocope
   "äta" → identified for substitution → then shortened
```

---

## File Structure (Per Dialect)

Every dialect branch follows this standardized structure:

```
[dialect-branch]/
│
├── README.md                         # Overview & quick start
├── ALPHABET.md                       # Complete phonetic guide with IPA
├── RULES.md                         # All transformation rules explained
├── LEARNING-GUIDE.md                # 4-phase progression system
├── EXAMPLES.md                      # 50+ translation examples
├── HISTORY.md                       # Linguistic & cultural history
│
├── [dialect]-translator.html         # Interactive web tool
├── [dialect]-cli.py                 # Command-line translator
│
├── data/
│   ├── vocabulary.json              # Dialect-specific vocabulary
│   ├── rules.json                   # Rule definitions & test cases
│   ├── examples.json                # Translation pairs for testing
│   └── metadata.json                # Dialect metadata
│
└── audio/                           # (Optional)
    ├── pronunciation_guide.mp3
    └── native_speaker_samples/
```

### File Descriptions

| File | Purpose | Owner |
|------|---------|-------|
| **README.md** | Project overview, features, quick start | Maintainer |
| **ALPHABET.md** | Phonetic reference with IPA, special chars | Linguist |
| **RULES.md** | Detailed rule documentation with linguistic rationale | Linguist |
| **LEARNING-GUIDE.md** | 4-phase structured progression system | Educator |
| **EXAMPLES.md** | 50+ real translation examples with breakdown | Community |
| **HISTORY.md** | Historical context, cultural significance, academic sources | Historian |
| **vocabulary.json** | Expandable word database | Community/Native speakers |
| **rules.json** | Algorithm definitions & test cases | Developers |
| **examples.json** | Test pairs for validation & CI/CD | QA/Testers |
| **[dialect]-translator.html** | Interactive web app | Developer |
| **[dialect]-cli.py** | Terminal translator & rule inspector | Developer |

---

## Data Formats

### vocabulary.json Structure

```json
[
  {
    "word": "gatt",
    "dialect": "bondska",
    "word_type": "verb_modal",
    "swedish": "måste",
    "english": "must (archaic modal form)",
    "pronunciation": {
      "ipa": "[ɡat]",
      "description": "Hard G at beginning, short A with retroflex flap"
    },
    "frequency": "very_high",
    "example_sentences": [
      "I gatt gå heim" 
    ],
    "notes": "High-frequency modal verb, archaic form of 'måste'",
    "sources": [
      "Native speaker (Jan Eriksson)",
      "Reference: Västerbotten Dialect Dictionary (1985)"
    ],
    "verified_by": "Native speaker validation required",
    "date_added": "2025-01-15",
    "submitted_by": "Community"
  }
]
```

### rules.json Structure

```json
{
  "rule_id": "vowel_e_to_ei",
  "rule_name": "Short E to EI Diphthongization",
  "category": "vowel_shift",
  "priority": 1,
  "description": "Restore Old Norse diphthong: short /e/ becomes /eɪ/",
  "pattern": {
    "language": "regex",
    "value": "\\b(\\w*)e(\\w*)\\b"
  },
  "conditions": [
    "Applies to short 'e' in monosyllabic stems",
    "Does not apply to final -e in weak syllables"
  ],
  "examples": [
    {
      "swedish": "sten",
      "bondska": "stein",
      "english": "stone"
    },
    {
      "swedish": "ben",
      "bondska": "bein",
      "english": "leg"
    }
  ],
  "exceptions": [
    "Proper names usually unchanged",
    "Some borrowed words may not shift"
  ],
  "test_cases": [
    {
      "input": "sten",
      "expected": "stein",
      "status": "pass"
    }
  ]
}
```

### examples.json Structure

```json
{
  "examples": [
    {
      "id": 1,
      "title": "Identity - Who are you?",
      "swedish": "Jag heter Alex och jag kommer från Sverige.",
      "dialect": "I heit Alex å i kôm från Sverje.",
      "english": "I am called Alex and I come from Sweden.",
      "difficulty": "beginner",
      "phase": 1,
      "rules_applied": ["pronoun_jag_to_i", "verb_heter_to_heit", "vocab_och_to_a"],
      "breakdown": [
        {"word": "Jag", "shift": "I", "rule": "pronoun_jag_to_i"},
        {"word": "heter", "shift": "heit", "rule": "verb_apocope_er"},
        {"word": "och", "shift": "å", "rule": "vocab_och_to_a"}
      ]
    }
  ]
}
```

---

## Standardized Tools

### Template Web App

**File**: `shared/framework/bondska-translator.html` (reusable pattern)

**Purpose**: Template for all dialect web apps

**Features**:
- Pre-built UI structure
- Configurable translation engine
- CSS variables for theming
- Built-in responsive design
- Tab system for guides

**How to customize**:
1. Copy template to `[dialect]-translator.html`
2. Update dialect-specific rules in JavaScript
3. Modify dialect name & branding
4. Test in browser

### Template CLI Tool

**File**: `shared/framework/dialect-cli-template.py`

**Purpose**: Template for all dialect CLI tools

**Features**:
- CLI argument parsing
- Interactive mode
- Rule inspection commands
- Translation history
- Help system

**How to customize**:
1. Copy template to `[dialect]-cli.py`
2. Populate `vowel_shifts`, `consonant_shifts`, etc. dicts
3. Add dialect-specific vocabulary
4. Update help text & examples
5. Test in terminal

---

## Integration Points

### GitHub Workflows (CI/CD)

**File**: `.github/workflows/validate-translations.yml`

**Purpose**: Automated testing on every commit

**Tests**:
```yaml
validate-translations:
  - Lint all JSON files (vocabulary, rules, examples)
  - Test 10+ translation pairs
  - Check for duplicate vocabulary entries
  - Validate rule structures
  - Run CLI tool with sample inputs
  - Check HTML validity
```

### Issue Templates

**Files**: `.github/ISSUE_TEMPLATE/`
- `bug_report.md`: Report translation errors
- `new_dialect.md`: Propose new dialect
- `vocabulary_submission.md`: Submit words

### Pull Request Templates

**File**: `.github/pull_request_template.md`

**Format**:
```markdown
## Description
## Type of Change
## Dialect(s) Affected
## Testing Done
## Checklist
```

---

## Scalability & Maintenance

### Adding a New Dialect

**Process**:
1. Create new branch: `git checkout -b my-new-dialect`
2. Copy template files from `shared/framework/`
3. Populate `vocabulary.json` with 100+ words
4. Define rules in `rules.json`
5. Write documentation (ALPHABET.md, RULES.md, etc.)
6. Create PR to main with new dialect info

**Estimated effort**: 20-40 hours for complete implementation

### Updating Main Documentation

**Process**:
1. Edit files in `main` branch
2. Update README.md with any new standards
3. Add new resources to `community/`
4. All dialect branches reference these standards

**Update frequency**: Monthly or as needed

### Performance Considerations

**Web App**:
- Translation happens instantly (< 100ms)
- No external API calls
- Works offline
- Tested on mobile (slow connections)

**CLI Tool**:
- Pure Python (no dependencies)
- Startup time: < 500ms
- Memory usage: < 10MB
- Scalable to 100,000+ word vocabulary

---

## Future Architecture Enhancements

### Planned Improvements

1. **ML-based Rule Learning**
   - Automatically detect transformation patterns
   - Improve accuracy with more data

2. **Audio Integration**
   - Linked pronunciation for all words
   - TTS (Text-to-Speech) fallback

3. **Mobile Apps**
   - Native iOS/Android apps
   - Offline sync capabilities
   - Progress tracking

4. **Community Platform**
   - User accounts & progress
   - Social learning features
   - Leaderboards (gamification)

5. **Academic Integration**
   - University partnership tools
   - Research dataset export
   - Citation support

---

**Last Updated**: December 2025 | **Version**: 1.0 | **Architect**: Nordic Dialects Team
