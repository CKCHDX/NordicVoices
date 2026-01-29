# Template Guide: Creating a New Dialect Branch

## Using the Bondska Branch as Your Template

The **Bondska branch** serves as the complete, production-ready template for all dialect implementations. Instead of providing separate template files, we recommend using the Bondska branch directly as your starting point.

---

## Quick Start: Copy from Bondska

### Step 1: Create Your Dialect Branch

```bash
# From the main branch
git checkout -b [your-dialect-name]

# Example:
git checkout -b varmlandska
```

### Step 2: Copy Files from Bondska

```bash
# Fetch the Bondska branch
git fetch origin Bondska:Bondska

# Copy the complete file structure
git checkout Bondska -- bondska-translator.html
git checkout Bondska -- bondska-cli.py
git checkout Bondska -- data/
git checkout Bondska -- ALPHABET.md
git checkout Bondska -- RULES.md
git checkout Bondska -- EXAMPLES.md
git checkout Bondska -- LEARNING-GUIDE.md
git checkout Bondska -- HISTORY.md
git checkout Bondska -- PROJECT-SUMMARY.md
git checkout Bondska -- SETUP.md
```

### Step 3: Rename Files

```bash
# Rename to match your dialect
mv bondska-translator.html varmlandska-translator.html
mv bondska-cli.py varmlandska-cli.py
```

### Step 4: Customize Content

Now edit each file to replace Bondska-specific content with your dialect:

1. **HTML Translator**: Update dialect name, rules, vocabulary
2. **CLI Tool**: Update rules and dictionary
3. **Documentation**: Rewrite for your dialect's features
4. **Data Files**: Replace with your dialect's data

---

## What's in the Bondska Template

### 1. Web Translator (`bondska-translator.html`)

**Structure**:
- Header with dialect name
- Input/output text areas
- Rule toggle controls
- Debug panel showing transformations
- Inline CSS styling (cyberpunk theme)
- Complete JavaScript translation engine

**What to Customize**:
```javascript
// 1. Change dialect name in title and headers
<title>NordicVoices | [Your Dialect] Engine</title>
<h1>NordicVoices // <span>[Your Dialect]</span></h1>

// 2. Update particle rules (high-frequency words)
const particleRules = {
    "och": "[your_form]",
    "jag": "[your_form]",
    // ... add your dialect's words
};

// 3. Update suffix transformations
const suffixRules = [
    { suffix: "het", replace: "[your_form]", name: "..." },
    // ... your dialect's patterns
];

// 4. Update phonology rules
const phonologyRules = [
    { regex: /pattern/, replace: "[replacement]", name: "..." },
    // ... your dialect's sound changes
];
```

### 2. CLI Tool (`bondska-cli.py`)

**Structure**:
- Translation function with rule pipeline
- Dictionary of high-frequency words
- Suffix transformation rules
- Phonology and consonant shifts
- Interactive command-line interface

**What to Customize**:
```python
# 1. Update dialect name
print("NordicVoices | [Your Dialect] CLI v1.0")

# 2. Replace dictionary
dictionary = {
    "och": "[your_form]",
    "jag": "[your_form]",
    # ... your dialect's vocabulary
}

# 3. Update suffix rules
suffixes = [
    ("het", "[your_form]", "..."),
    # ... your dialect's suffixes
]

# 4. Update phonology rules
word = re.sub(r'pattern', '[replacement]', word)
# ... your dialect's sound rules
```

### 3. Documentation Files

#### ALPHABET.md
- **Purpose**: Complete phonetic reference with IPA
- **Content**: Consonants, vowels, special features
- **Customize**: Replace with your dialect's sounds

#### RULES.md
- **Purpose**: Detailed transformation rules
- **Content**: All 4 phases explained
- **Customize**: Document your dialect's rules

#### LEARNING-GUIDE.md
- **Purpose**: 4-phase learning progression
- **Content**: Week-by-week curriculum
- **Customize**: Adapt to your dialect's features

#### EXAMPLES.md
- **Purpose**: 50+ translation examples
- **Content**: Swedish → Dialect → English
- **Customize**: Create examples for your dialect

#### HISTORY.md
- **Purpose**: Linguistic and cultural history
- **Content**: Origins, development, significance
- **Customize**: Research your dialect's history

#### PROJECT-SUMMARY.md
- **Purpose**: Complete project overview
- **Content**: Features, statistics, documentation
- **Customize**: Update for your dialect

#### SETUP.md
- **Purpose**: Installation and usage guide
- **Content**: How to use the tools
- **Customize**: Adjust instructions as needed

### 4. Data Files

#### data/vocabulary.json
```json
[
  {
    "id": 1,
    "swedish": "hus",
    "dialect": "[your_form]",
    "ipa": "[pronunciation]",
    "english": "house",
    "category": "noun",
    "phase": 1,
    "frequency": 5,
    "notes": "..."
  }
]
```

#### data/rules.json
```json
[
  {
    "id": "p1_pronoun_jag",
    "name": "First person singular pronoun",
    "phase": 1,
    "pattern": "\\bjag\\b",
    "replacement": "[your_form]",
    "explanation": "...",
    "examples": [...]
  }
]
```

#### data/examples.json
```json
[
  {
    "id": 1,
    "swedish": "Hej, jag heter Alex",
    "dialect": "[your_translation]",
    "english": "Hi, my name is Alex",
    "phase": 1,
    "category": "greeting",
    "rules": [...]
  }
]
```

---

## Customization Checklist

### Phase 1: Basic Setup
- [ ] Create new branch with your dialect name
- [ ] Copy all files from Bondska branch
- [ ] Rename files to match your dialect
- [ ] Update README.md with dialect name

### Phase 2: Code Customization
- [ ] Update HTML translator title and branding
- [ ] Replace particle rules with your dialect's words
- [ ] Update suffix transformation rules
- [ ] Modify phonology rules
- [ ] Update CLI tool dictionary and rules
- [ ] Test translation with sample sentences

### Phase 3: Documentation
- [ ] Write ALPHABET.md for your dialect
- [ ] Document all rules in RULES.md
- [ ] Create LEARNING-GUIDE.md with examples
- [ ] Write 50+ examples in EXAMPLES.md
- [ ] Research and write HISTORY.md
- [ ] Update PROJECT-SUMMARY.md

### Phase 4: Data Files
- [ ] Create vocabulary.json (minimum 20 words)
- [ ] Define rules.json (minimum 10 rules)
- [ ] Generate examples.json (minimum 20 examples)

### Phase 5: Testing & Validation
- [ ] Test translator with various inputs
- [ ] Verify all rules work correctly
- [ ] Get native speaker feedback (if possible)
- [ ] Fix any issues found
- [ ] Run JSON validation

### Phase 6: Polish & Release
- [ ] Update all documentation for accuracy
- [ ] Ensure consistent styling
- [ ] Add credits and sources
- [ ] Create PR to main branch (optional)
- [ ] Announce in discussions

---

## Simplified Starter Template

If the full Bondska implementation is too complex, start with this minimal template:

### Minimal HTML Translator

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>[Your Dialect] Translator</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 50px auto; }
        textarea { width: 100%; height: 200px; font-size: 16px; }
        .panel { margin: 20px 0; }
    </style>
</head>
<body>
    <h1>[Your Dialect] Translator</h1>
    
    <div class="panel">
        <h3>Swedish</h3>
        <textarea id="input" oninput="translate()"></textarea>
    </div>
    
    <div class="panel">
        <h3>[Your Dialect]</h3>
        <textarea id="output" readonly></textarea>
    </div>
    
    <script>
        function translate() {
            let text = document.getElementById('input').value;
            
            // Add your translation rules here
            // Example: Simple word substitution
            text = text.replace(/\bjag\b/gi, '[your_form]');
            text = text.replace(/\boch\b/gi, '[your_form]');
            
            document.getElementById('output').value = text;
        }
    </script>
</body>
</html>
```

### Minimal Python CLI

```python
#!/usr/bin/env python3

def translate(text):
    """Translate Swedish to [Your Dialect]"""
    
    # Add your translation rules here
    # Example: Simple word substitution
    text = text.replace('jag', '[your_form]')
    text = text.replace('och', '[your_form]')
    
    return text

def main():
    print("[Your Dialect] Translator")
    print("Type text to translate (Ctrl+C to exit)\n")
    
    try:
        while True:
            swedish = input("Swedish: ")
            dialect = translate(swedish)
            print(f"[Dialect]: {dialect}\n")
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
```

---

## Tips for Success

### Start Small
- Begin with 10-20 high-frequency words
- Add 5-10 basic rules
- Test thoroughly before expanding

### Be Systematic
- Follow the 4-phase learning system
- Document as you go
- Test each rule individually

### Get Feedback
- Share with native speakers early
- Iterate based on feedback
- Accept corrections gracefully

### Stay Consistent
- Use the same naming conventions as Bondska
- Follow the same file structure
- Maintain the same documentation style

---

## Resources

### Bondska Branch
- **View online**: [https://github.com/CKCHDX/NordicVoices/tree/Bondska](https://github.com/CKCHDX/NordicVoices/tree/Bondska)
- **Clone locally**: `git clone https://github.com/CKCHDX/NordicVoices.git && git checkout Bondska`

### Shared Resources
- **Phonetic Standards**: `shared/docs/PHONETIC-STANDARDS.md`
- **Rule Framework**: `shared/docs/RULE-FRAMEWORK.md`
- **Testing Guidelines**: `shared/docs/TESTING-GUIDELINES.md`
- **Learning System**: `shared/framework/learning-system.md`

### Community
- **GitHub Discussions**: Ask questions, get help
- **Issues**: Report problems, request features
- **Contributors**: Connect with other developers

---

## Need Help?

If you're working on a new dialect:

1. **Open a discussion** on GitHub
2. **Use the "New Dialect" issue template**
3. **Contact maintainers** via email
4. **Join the community** chat

We're here to help you preserve your dialect!

---

*Last Updated: December 2025*  
*Nordic Dialects Preservation Project*  
*Build on proven foundations. Create with confidence.*
