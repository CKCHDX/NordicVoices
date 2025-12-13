# Contributing to Nordic Dialects Preservation Suite

Thank you for your interest in preserving Nordic dialects! This guide will help you understand how to contribute effectively to this project.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Types of Contributions](#types-of-contributions)
4. [Contribution Workflow](#contribution-workflow)
5. [Submission Guidelines](#submission-guidelines)
6. [Style Guides](#style-guides)
7. [Pull Request Process](#pull-request-process)
8. [Recognition & Credits](#recognition--credits)

---

## Code of Conduct

### Our Pledge
We are committed to providing a welcoming and inspiring community for all people, regardless of background, experience level, or dialect knowledge. We pledge to:

- **Respect linguistic diversity**: All dialects are equally valuable
- **Honor native speakers**: Prioritize their knowledge and authority
- **Maintain accuracy**: Linguistic precision over simplification
- **Be inclusive**: Welcome contributors of all skill levels
- **Foster collaboration**: Support learning and peer review

### Expected Behavior
- Be respectful and constructive in all communications
- Give credit to native speakers and sources
- Ask questions when uncertain
- Provide evidence for linguistic claims
- Accept feedback graciously

### Unacceptable Behavior
- Dismissing or mocking any dialect
- Spreading misinformation about language origins
- Harassment of any kind
- Plagiarism without attribution
- Disrespect toward native speakers

---

## Getting Started

### Prerequisites
- **GitHub account**: Free at [github.com](https://github.com)
- **Git knowledge**: Basic familiarity with `git clone`, `git commit`, `git push`
- **Text editor**: Any editor (VS Code, Sublime, vim, etc.)
- **Python 3.8+** (optional, for CLI tool development)

### Fork & Clone the Repository

```bash
# 1. Fork the repository on GitHub
# Visit: https://github.com/CKCHDX/Nordic-Dialects
# Click "Fork" in the top-right corner

# 2. Clone your fork locally
git clone https://github.com/YOUR-USERNAME/Nordic-Dialects.git
cd Nordic-Dialects

# 3. Add upstream remote
git remote add upstream https://github.com/CKCHDX/Nordic-Dialects.git

# 4. Create a feature branch
git checkout -b feature/your-feature-name
```

### Sync with Main Repository

```bash
# Keep your fork in sync
git fetch upstream
git rebase upstream/main
git push origin main
```

---

## Types of Contributions

### 1. **Add Vocabulary** (Best for Native Speakers)

**What**: Submit authentic dialect words with translations and pronunciations.

**How**:
```bash
# Create or edit vocabulary.json in your dialect branch
# Example structure:
{
  "word": "gatt",
  "dialect": "bondska",
  "swedish": "måste",
  "english": "must",
  "pronunciation": "[ɡat]",
  "example_sentence": "I gatt gå heim",
  "audio_link": "https://...",
  "notes": "High-frequency word, archaic modal verb form",
  "submitted_by": "Your Name",
  "verified_by_native_speaker": true
}
```

**Submission**:
1. Edit or create `[dialect]/data/vocabulary.json`
2. Add 1-10 words per PR (easier to review)
3. Include native speaker verification if possible
4. Reference sources or personal knowledge

---

### 2. **Expand Rules & Algorithms**

**What**: Document exceptions, improve transformation algorithms, add dialect variations.

**How**:
```bash
# Edit [dialect]/data/rules.json
# Add new rule with test cases

{
  "rule_name": "Vowel Diphthongization - E to EI",
  "pattern": "short_e_in_monosyllabic_stem",
  "swedish_words": ["sten", "ben", "hem"],
  "bondska_words": ["stein", "bein", "heim"],
  "exceptions": [],
  "priority": 1,
  "test_cases": [
    {"input": "sten", "expected": "stein", "actual": "stein", "status": "pass"}
  ]
}
```

**Submission**:
1. Create or edit `[dialect]/RULES.md` with new rule details
2. Add test cases in `[dialect]/data/rules.json`
3. Explain linguistic rationale
4. Cite academic sources if available

---

### 3. **Create Content**

**What**: Educational materials, translations, stories, audio/video content.

**How**:

**For translations**:
```bash
# Add to [dialect]/EXAMPLES.md
# Format:
# #### Example N: [Title]
# 
# Swedish: [text]
# Dialect: [text]
# English: [translation]
# 
# Breakdown:
# - Word 1 → Word 2 (rule applied)
```

**For audio pronunciations**:
- Record native speaker pronunciation (if possible)
- Save as `.mp3` or `.wav` in `[dialect]/audio/`
- Add link to `vocabulary.json` entries

**For video tutorials**:
- Create YouTube or Vimeo videos
- Submit links in `[dialect]/PRONUNCIATION-GUIDE.md`
- Include timestamps and transcripts

**Submission**:
1. Create content file in appropriate location
2. Write clear descriptions and metadata
3. Include native speaker credits
4. Submit PR with content link

---

### 4. **Improve Code & Tools**

**What**: Bug fixes, feature additions, code optimization, new tools.

**How**:

**For bug fixes**:
```bash
# 1. Create issue first (if not already created)
# 2. Create feature branch
git checkout -b fix/issue-number-description

# 3. Make changes to [dialect]-cli.py or [dialect]-translator.html
# 4. Test thoroughly
python3 [dialect]-cli.py translate "Jag heter Alex"

# 5. Commit with clear message
git commit -m "Fix: Correct vowel shift for word 'sten' (Issue #123)"

# 6. Push and create PR
git push origin fix/issue-number-description
```

**For new features**:
```bash
# 1. Create issue proposing feature
# 2. Wait for approval before implementing
# 3. Create feature branch
git checkout -b feature/new-feature-name

# 4. Implement with tests
# 5. Update documentation
# 6. Create PR with description
```

**Submission**:
1. Test code locally before submitting
2. Follow code style (see below)
3. Include comments for complex logic
4. Update relevant documentation

---

### 5. **Build Community**

**What**: Organize learning groups, connect native speakers, document variations.

**How**:
```bash
# Update community files
vim community/LOCAL-GROUPS.md      # Add your local group
vim community/NATIVE-SPEAKERS.md   # Add speaker resources
vim community/LEARNING-PATHS.md    # Add learning strategy
```

**Submission**:
1. Edit community files with new information
2. Include contact information (if public)
3. Add your organization's mission & goals
4. Submit PR with description

---

## Contribution Workflow

### Step 1: Identify a Contribution Area

**Choose from**:
- Browse [GitHub Issues](../../issues) for requested features
- Read [ARCHITECTURE.md](shared/ARCHITECTURE.md) for system needs
- Pick a dialect needing more vocabulary
- Suggest a new feature via GitHub Discussion

### Step 2: Create an Issue (for anything beyond typos)

**Format**:
```markdown
## Title: [Brief description]

**Type**: [Bug / Feature / Documentation / Vocabulary / Other]

**Dialect**: [bondska / gutnish / etc]

**Description**:
[Detailed explanation of what you want to do]

**Why**:
[Why is this important for the project?]

**Resources**:
- [Link to relevant documentation]
- [Link to academic sources, if applicable]
```

### Step 3: Get Approval (for major changes)

- **Major features**: Wait for maintainer approval
- **Vocabulary**: Can proceed immediately (community review)
- **Documentation**: Can proceed immediately
- **Critical bugs**: Create issue first, then fix

### Step 4: Create Feature Branch

```bash
git checkout -b feature/description-of-change
# Branch naming: feature/, fix/, docs/, vocab/, etc.
```

### Step 5: Make Changes

- Edit files in your dialect branch
- Follow style guides (below)
- Add tests/examples as applicable
- Update documentation

### Step 6: Commit with Clear Messages

```bash
# Good commit messages
git commit -m "Add 20 new vocabulary words to Bondska"
git commit -m "Fix: Correct E→EI vowel shift for word 'ben'"
git commit -m "Docs: Add pronunciation guide for Gutnish"

# Bad commit messages
git commit -m "Update stuff"
git commit -m "WIP"
```

### Step 7: Push and Create Pull Request

```bash
git push origin feature/your-feature
# Then create PR on GitHub with description
```

### Step 8: Respond to Review

- Be open to feedback
- Discuss concerns constructively
- Make requested changes
- Re-push updates

### Step 9: Merge!

Once approved, maintainer merges to main branch.

---

## Submission Guidelines

### Vocabulary Submissions

**Requirements**:
- ✅ Authentic word in dialect
- ✅ Swedish translation
- ✅ English meaning
- ✅ IPA pronunciation (if possible)
- ✅ Example sentence
- ✅ Verified by native speaker (preferred)

**Preferred quantity**: 5-20 words per PR

**Format**:
```json
[
  {
    "word": "gatt",
    "dialect": "bondska",
    "swedish": "måste",
    "english": "must",
    "pronunciation": "[ɡat]",
    "example_sentence": "I gatt gå heim å ät grayt",
    "audio_link": "https://...",
    "sources": ["Native speaker", "Reference: Book Name"],
    "notes": "Archaic modal verb, high-frequency in dialect"
  }
]
```

### Documentation Submissions

**Requirements**:
- ✅ Clear, concise writing
- ✅ Proper markdown formatting
- ✅ Examples where applicable
- ✅ Links to sources
- ✅ Proper grammar & spelling

**Sections to update**:
- ALPHABET.md: New phonetic information
- RULES.md: New transformation rules
- EXAMPLES.md: Example translations
- LEARNING-GUIDE.md: Learning strategies
- HISTORY.md: Historical/cultural context

### Code Submissions

**Requirements**:
- ✅ Clean, readable code
- ✅ Proper comments for complex logic
- ✅ Tested locally
- ✅ No console errors/warnings
- ✅ Follows style guide (below)

**For Python**:
```python
# Good code
def translate_to_dialect(swedish_text: str) -> str:
    """
    Translate modern Swedish to dialect using transformation rules.
    
    Args:
        swedish_text: Modern Swedish text to translate
        
    Returns:
        Dialect version of the text
    """
    text = swedish_text.strip()
    text = apply_pronouns(text)
    text = apply_vowel_shifts(text)
    return text
```

**For HTML/CSS/JS**:
```html
<!-- Clear, semantic HTML -->
<div class="translator-section">
  <h2>Vocabulary</h2>
  <table class="vocabulary-table">
    <!-- Properly structured table -->
  </table>
</div>

<style>
  /* Organized CSS with comments */
  .translator-section {
    padding: var(--spacing-lg);
  }
</style>
```

---

## Style Guides

### Markdown Style

```markdown
# Main Heading (H1)

## Section Heading (H2)

### Subsection Heading (H3)

**Bold** for emphasis, *italic* for terms

- Bulleted list items
- One idea per bullet

1. Numbered lists
2. For sequences

> Block quotes for important notes or citations

`inline code` for variables/commands

\`\`\`language
code blocks
with syntax highlighting
\`\`\`

[Links](https://example.com) with descriptive text
```

### Python Style

Follow [PEP 8](https://pep8.org/):

```python
# Imports at top
import sys
from typing import Dict, List

# Constants in UPPERCASE
MAX_VOCABULARY_SIZE = 10000

# Classes in PascalCase
class BondskaNormalizer:
    """Class docstring."""
    
    def __init__(self):
        """Initialize the translator."""
        self.rules = {}
    
    def translate(self, text: str) -> str:
        """
        Translate text with detailed docstring.
        
        Args:
            text: Input text
            
        Returns:
            Translated text
        """
        # Comments for complex logic
        return processed_text

# Functions in snake_case
def apply_vowel_shifts(text: str) -> str:
    """Apply vowel transformation rules."""
    return text

# Use type hints
def process_vocabulary(words: List[str]) -> Dict[str, str]:
    """Process vocabulary list."""
    return {}
```

### JSON Style

```json
{
  "word": "gatt",
  "dialect": "bondska",
  "properties": {
    "swedish": "måste",
    "pronunciation": "[ɡat]"
  },
  "array_property": [
    "item1",
    "item2"
  ]
}
```

---

## Pull Request Process

### Before Submitting

- [ ] **Code tested locally**
  ```bash
  python3 [dialect]-cli.py translate "Test sentence"
  ```

- [ ] **Documentation updated**
  - README.md if changes affect overview
  - RULES.md if changing rules
  - EXAMPLES.md if adding examples
  - ALPHABET.md if adding phonetic info

- [ ] **Commit messages clear**
  ```bash
  git log --oneline origin/main..HEAD
  ```

- [ ] **No conflicts with main**
  ```bash
  git fetch upstream
  git rebase upstream/main
  ```

### PR Template

```markdown
## Description
Brief explanation of what this PR does.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Vocabulary addition
- [ ] Code refactoring

## Dialect(s) Affected
- bondska
- gutnish
- etc.

## Linked Issues
Closes #[issue-number]

## Testing Done
Describe testing performed:
- [ ] Translated 10+ test sentences
- [ ] Checked against native speaker feedback
- [ ] Verified no regressions

## Screenshots (if applicable)
[Include screenshots of web app changes, etc.]

## Checklist
- [ ] Code follows style guide
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Commits have clear messages
```

### Review Process

1. **Automated checks** run (CI/CD pipeline)
2. **Maintainers review** for quality & accuracy
3. **Native speakers review** (if applicable)
4. **Suggestions provided** in comments
5. **Author updates** based on feedback
6. **Approval & merge** when ready

---

## Recognition & Credits

### How Contributors are Recognized

- ✅ Name added to `CONTRIBUTORS.md`
- ✅ Credited in dialect-specific README
- ✅ Mentioned in release notes
- ✅ Highlighted in community updates
- ✅ Optional author bio in CONTRIBUTORS.md

### Example Contributor Entry

```markdown
## [Your Name]

**Role**: Native Speaker / Developer / Researcher

**Contributions**:
- Added 50 vocabulary words to Bondska
- Implemented vowel shift algorithm
- Created pronunciation video series

**Location**: Umeå, Sweden

**Contact**: [GitHub profile]

**Languages**: Bondska, Swedish, English
```

---

## Frequently Asked Questions

### Q: I'm not a native speaker. Can I contribute?

**A**: Absolutely! We welcome:
- Developers improving tools
- Researchers documenting history
- Linguists analyzing systems
- Learners adding examples
- Anyone passionate about preservation

Just ensure vocabulary submissions are verified by native speakers.

### Q: How much time should I commit?

**A**: Contribute what you can:
- **5 minutes**: Fix a typo, add one word
- **30 minutes**: Add 10 words, fix a bug
- **2 hours**: Create documentation, refactor code
- **Ongoing**: Maintain a dialect, lead community

### Q: Will my work be attributed?

**A**: Yes! All contributions are credited:
- In commits (git history)
- In CONTRIBUTORS.md
- In dialect-specific READMEs
- In release announcements

### Q: What if I want to help but don't know where to start?

**A**: Good options:
1. Check [open issues](../../issues) for suggestions
2. Read "Good first issue" label
3. Ask in [Discussions](../../discussions)
4. Contact maintainers directly
5. Start with vocabulary (easy, valuable)

### Q: Can I create a new dialect branch?

**A**: Yes! Process:
1. Open issue proposing new dialect
2. Describe status (living, endangered, extinct)
3. Provide linguistic sources
4. Get approval from maintainers
5. Create branch following naming convention
6. Submit initial content

---

## Resources

### Learning Git
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Learning Lab](https://lab.github.com/)
- [Atlassian Git Tutorial](https://www.atlassian.com/git)

### Linguistics
- [IPA Chart](https://www.internationalphoneticassociation.org/)
- [ISOF Resources](https://www.isof.se/)
- [Wikipedia: Nordic Languages](https://en.wikipedia.org/wiki/Nordic_languages)

### Open Source
- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [Open Source Etiquette](https://opensource.guide/starting-a-project/#setting-the-tone-for-your-project)

---

## Contact

Have questions? Reach out:

- **GitHub Issues**: [Create an issue](../../issues)
- **Discussions**: [Join the conversation](../../discussions)
- **Email**: dialect-preservation@example.com
- **Social**: @NordicDialects on Twitter/Instagram

---

**Thank you for helping preserve Nordic dialects! Your contribution, no matter how small, helps keep these voices alive.** 🇸🇪
