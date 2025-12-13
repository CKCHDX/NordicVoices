# 🇸🇪 Nordic Dialects Preservation Suite
## Reviving Endangered Languages & Dialects of Scandinavia

> A systematic effort to document, preserve, and revive endangered Nordic dialects through open-source technology, linguistic research, and community engagement.

**Status**: 🚀 Active Development | **Last Updated**: December 2025 | **Branches**: 20+ Dialects

---

## 📋 Project Overview

This is a **comprehensive dialect preservation initiative** using GitHub branches to organize work on 20+ endangered and archaic Nordic languages and dialects. Each dialect gets its own dedicated branch with translation tools, documentation, learning systems, and community resources.

### Mission
To prevent linguistic extinction by creating:
- ✅ Interactive translators (Swedish ↔ Dialect)
- ✅ Comprehensive documentation & phonetic guides
- ✅ Structured learning systems (4-phase progression)
- ✅ Community resources for native speakers and learners
- ✅ Open-source, freely available tools for everyone

### Key Features
- **Multi-dialect support**: 20+ Nordic languages in one ecosystem
- **Modular architecture**: Each dialect is self-contained on its own branch
- **Unified standards**: Consistent tools, documentation, and learning systems across all dialects
- **Open-source**: MIT License, welcome community contributions
- **No dependencies**: Web apps work offline, CLI tools require only Python 3.8+

---

## 📊 Dialect Coverage Map

### By Region

#### **Götaland / West Sweden** (8 dialects)
| Dialect | Status | Geographic Region | Branch |
|---------|--------|-------------------|--------|
| **Bondska** | 🟢 Active | Bohuslän Coast | `bondska` |
| **Värmländska** | 🟡 Archaic | Rural Värmland | `vermlandska` |
| **Jämtska** | 🟡 Endangered | Jämtland (older forms) | `jamtska` |
| **Elfdalska** | 🟡 Endangered | Älvdalen, Dalecarlian | `elfdalska` |
| **Södra Bohuslänska** | 🔴 Historical | South Bohuslän coast | `sodra-bohuslanska` |
| **Västra Härad (Småland)** | 🟡 Endangered | Småland/Njudung region | `vestra-harad` |
| **Värend** | 🟡 Endangered | South Småland | `varend` |
| **Gotländska** | 🟡 Endangered | Gotland island | `gotlandska` |

#### **Svealand / Central Sweden** (4 dialects)
| Dialect | Status | Geographic Region | Branch |
|---------|--------|-------------------|--------|
| **Uppländska** | 🟡 Archaic | Uppland (old forms) | `upplandsaka` |
| **Västmanländska** | 🔴 Historical | Västmanland (rural) | `vastmannlandska` |
| **Roslagsmål** | 🟡 Endangered | Roslagen archipelago | `roslagsmal` |
| **Stockholmska** | 🟢 Living | Stockholm dialect | `stockholmska` |

#### **Norrland / Northern Sweden** (4 dialects)
| Dialect | Status | Geographic Region | Branch |
|---------|--------|-------------------|--------|
| **Västerbottniska** | 🟢 Active | Västerbotten (Bondska variant) | `vasterbottniska` |
| **Pitemål** | 🟡 Endangered | Piteå (Bondska variant) | `pitemal` |
| **Ångermanländska** | 🟡 Archaic | Ångermanland (old forms) | `angermanlandska` |
| **Haparandamål** | 🔴 Historical | Haparanda (Finnish-Swedish) | `haparandamal` |

#### **Gotland & Islands** (3 dialects)
| Dialect | Status | Geographic Region | Branch |
|---------|--------|-------------------|--------|
| **Gutnish (Modern)** | 🟢 Endangered | Gotland island | `gutnish` |
| **Fårömål** | 🔴 Nearly Extinct | Fårö island | `faromal` |
| **Gutar** | 🔴 Historical | Old Gotlandic | `gutar` |

#### **Baltic & Historical Swedish** (4 dialects)
| Dialect | Status | Geographic Region | Branch |
|---------|--------|-------------------|--------|
| **Estlandssvenska** | 🔴 Extinct (1950s) | Estonia | `estlandssvenska` |
| **Runö Svenska** | 🔴 Extinct | Runö island, Estonia | `runo-svenska` |
| **Öselsvenska** | 🔴 Extinct | Ösel island, Estonia | `oselsvenska` |
| **Ålands Svenska** | 🟡 Archaic | Åland (old forms) | `alands-svenska` |

#### **Legend**
- 🟢 **Active/Living**: Still spoken by native communities
- 🟡 **Endangered/Archaic**: Few speakers, specialized knowledge needed
- 🔴 **Historical/Extinct**: No native speakers; documentation & reconstruction only

---

## 🏗️ Repository Structure

```
Nordic-Dialects/
├── README.md                          # This master file
├── CONTRIBUTING.md                    # Contribution guidelines (all dialects)
├── LICENSE                            # MIT License
├── ARCHITECTURE.md                    # System design & standards
├── PROJECT-TIMELINE.md                # Roadmap and milestones
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── new_dialect.md
│   │   └── vocabulary_submission.md
│   └── workflows/
│       └── validate-translations.yml  # CI/CD pipeline
│
├── shared/
│   ├── framework/
│   │   ├── bondska-translator.html    # Template web app (reusable)
│   │   ├── dialect-cli-template.py    # Template CLI tool
│   │   └── learning-system.md         # Standard 4-phase system
│   │
│   ├── data/
│   │   ├── phonetic-guide.json        # Universal IPA reference
│   │   ├── common-vocabulary.json     # Shared Old Norse roots
│   │   └── transformation-rules.json  # Core linguistic rules
│   │
│   └── docs/
│       ├── PHONETIC-STANDARDS.md      # IPA conventions
│       ├── RULE-FRAMEWORK.md          # How to build translation rules
│       └── TESTING-GUIDELINES.md      # Quality assurance
│
├── dialects/
│   ├── [BRANCH: bondska]
│   │   ├── README.md                  # Dialect-specific overview
│   │   ├── bondska-translator.html    # Interactive web tool
│   │   ├── bondska-cli.py             # CLI translator
│   │   ├── ALPHABET.md                # Complete phonetic guide
│   │   ├── RULES.md                   # Transformation rules
│   │   ├── LEARNING-GUIDE.md          # 4-phase progression
│   │   ├── EXAMPLES.md                # 50+ example translations
│   │   ├── HISTORY.md                 # Linguistic history
│   │   └── data/
│   │       ├── vocabulary.json        # Dialect-specific vocab
│   │       ├── rules.json             # Translation algorithms
│   │       └── examples.json          # Test pairs
│   │
│   ├── [BRANCH: gutnish]
│   │   ├── README.md
│   │   ├── gutnish-translator.html
│   │   ├── gutnish-cli.py
│   │   └── ... (same structure)
│   │
│   ├── [BRANCH: elfdalska]
│   │   └── ... (same structure)
│   │
│   └── [OTHER BRANCHES...]
│
└── community/
    ├── NATIVE-SPEAKERS.md            # Resources for native speakers
    ├── LEARNING-PATHS.md             # Multi-dialect learning strategies
    ├── PRONUNCIATION-GUIDE.md        # Audio & video links
    └── LOCAL-GROUPS.md               # Community organizations & contacts
```

---

## 🌳 Branch Strategy

### Main Branch (`main`)
- **Content**: This master README + shared resources
- **Purpose**: Project overview, navigation, shared standards
- **Update Frequency**: Monthly

### Feature Branches (Per Dialect)
Each dialect gets its own dedicated branch:

```
bondska/              → Västerbottniska (Umeå/Skellefteå area)
gutnish/              → Gotlandic (Old Gutnish)
elfdalska/            → Dalecarlian (Älvdalen, Dalarna)
jamtska/              → Jämtlandic (older forms)
vermlandska/          → Värmlandic (older rural forms)
gotlandska/           → Modern Gotlandic dialect
vasterbottniska/      → Västerbotten variants
pitemal/              → Piteå dialect (Bondska variant)
angermanlandska/      → Ångermanland (archaic forms)
estlandssvenska/      → Estonian Swedish (extinct)
runo-svenska/         → Runö Swedish (extinct)
oselsvenska/          → Ösel Swedish (extinct)
alands-svenska/       → Åland Swedish (older forms)
stockholmska/         → Stockholm dialect (living)
roslagsmal/           → Roslagen archipelago
upplandsaka/          → Uppland (archaic forms)
... (and more)
```

### Branch Naming Convention
- **Lowercase**: `dialect-name`
- **Hyphens**: Separate multi-word dialects
- **Consistent**: Use the standard dialect name (not abbreviations)

### How to Work on a Dialect

```bash
# Clone the repo
git clone https://github.com/CKCHDX/Nordic-Dialects.git
cd Nordic-Dialects

# Create or switch to dialect branch
git checkout -b bondska
# OR if branch exists:
git checkout bondska

# Make changes to files in that dialect
vim bondska-translator.html
vim bondska-cli.py

# Commit and push
git add .
git commit -m "Add new vocabulary to Bondska"
git push origin bondska

# Create Pull Request to main (optional, for review)
# or merge directly if you're the maintainer
```

---

## 🎯 Quick Start by Dialect

### Find Your Dialect

**Want to learn/use a specific dialect?**

1. **Find your dialect** in the map above
2. **Click the branch name** → Go to that branch
3. **Follow the README.md** in that branch
4. **Use the tools**:
   - Web app: Open `.html` file in browser
   - CLI: Run Python script in terminal

### Example: Getting Started with Bondska
```bash
# Go to Bondska branch
git checkout bondska

# Open the web app
open bondska-translator.html

# Or use CLI
python3 bondska-cli.py translate "Jag heter Alex"

# Read the documentation
cat README.md
cat ALPHABET.md
cat LEARNING-GUIDE.md
```

### Example: Learning Multiple Dialects
```bash
# Each dialect has the same structure, so learning is consistent
# Phase 1 is always: Pronoun substitution
# Phase 2 is always: Vowel shifts
# Phase 3 is always: Apocope & consonant changes
# Phase 4 is always: Grammar & fluency

# Switch between dialects
git checkout bondska        # Västerbotten dialect
git checkout gutnish        # Gotlandic dialect
git checkout elfdalska      # Dalecarlian dialect

# All use the same learning methodology
```

---

## 📚 Shared Resources (Main Branch)

Files available in `main` branch for all dialects:

### Documentation
- **ARCHITECTURE.md**: System design & how dialects relate
- **PHONETIC-STANDARDS.md**: Universal IPA conventions
- **RULE-FRAMEWORK.md**: How to build transformation rules
- **TESTING-GUIDELINES.md**: Quality assurance procedures

### Templates
- **bondska-translator.html**: Template web app (reusable pattern)
- **dialect-cli-template.py**: Template CLI tool
- **learning-system.md**: Standard 4-phase progression system

### Data
- **phonetic-guide.json**: IPA reference for all dialects
- **common-vocabulary.json**: Shared Old Norse roots
- **transformation-rules.json**: Base linguistic rules

### Community
- **NATIVE-SPEAKERS.md**: Resources for native communities
- **LEARNING-PATHS.md**: Multi-dialect learning strategies
- **PRONUNCIATION-GUIDE.md**: Audio/video resources
- **LOCAL-GROUPS.md**: Community organizations

---

## 🛠️ Standardized Tools (All Dialects)

Every dialect branch includes:

### 1. **Interactive Web Translator** (HTML/CSS/JS)
- **File**: `[dialect]-translator.html`
- **Features**:
  - Real-time bidirectional translation
  - 4 integrated tabs (Rules, Alphabet, Vocabulary, Learning Guide)
  - Offline functionality
  - Mobile-responsive design
- **Usage**: Open in any browser, no dependencies

### 2. **Command-Line Tool** (Python 3.8+)
- **File**: `[dialect]-cli.py`
- **Features**:
  - Interactive & batch modes
  - Translation history tracking
  - Alphabet display with IPA
  - Rule inspection
- **Usage**: `python3 [dialect]-cli.py translate "text"`

### 3. **Comprehensive Documentation**
- **README.md**: Overview & features
- **ALPHABET.md**: Complete phonetic reference
- **RULES.md**: All transformation rules explained
- **LEARNING-GUIDE.md**: 4-phase mastery progression
- **EXAMPLES.md**: 50+ example translations
- **HISTORY.md**: Linguistic & cultural history

### 4. **Data Files** (JSON)
- **vocabulary.json**: Expandable word dictionary
- **rules.json**: Translation algorithms
- **examples.json**: Test pairs for validation

---

## 🎓 Learning System (Universal Across All Dialects)

All dialects follow the same **4-Phase Progression**:

### Phase 1: Pronoun Shift (Week 1)
Master high-frequency word substitutions
- Replace main pronouns
- Learn negation & basic verbs
- Goal: Automatic substitution

### Phase 2: Vowel Shifts (Week 2)
Apply phonetic transformations
- Diphthongization (restore Old Norse sounds)
- Vowel darkening
- Goal: Recognize vowel patterns

### Phase 3: Apocope & Consonants (Week 3)
Master word endings & consonant changes
- Word chopping (drop weak endings)
- Palatalization (soft consonants)
- Goal: Build complete sentences

### Phase 4: Grammar & Fluency (Week 4+)
Advanced features
- Gender system (Han/Hon/He)
- Dative case (locations)
- Melody & intonation
- Goal: Internal monologue in dialect

---

## 📈 Project Statistics

### Coverage
- **Total Dialects**: 23 (active + archaic)
- **Living/Endangered**: 15
- **Archaic/Historical**: 8
- **Extinct (documented)**: 4

### Development Status
```
Bondska        ████████████████████ 100% (Production Ready)
Gutnish        ████████████░░░░░░░░  60% (Core features done)
Elfdalska      ████████░░░░░░░░░░░░  40% (In progress)
Jämtska        ████░░░░░░░░░░░░░░░░  20% (Foundation)
Värmländska    ███░░░░░░░░░░░░░░░░░  15% (Planning)
Others         ░░░░░░░░░░░░░░░░░░░░   5% (Backlog)
```

### Vocabulary Targets
- **Bondska**: 2,000+ words (active)
- **Gutnish**: 1,500+ words (target)
- **Elfdalska**: 1,200+ words (target)
- **Others**: 500-1,000 words each

---

## 🤝 Contributing

### Ways to Help

#### 1. **Add Vocabulary**
- Native speakers: Submit authentic dialect words
- Submit corrections & variations
- Add phonetic pronunciations

#### 2. **Expand Rules**
- Report exceptions to transformation rules
- Document dialect variations (village-specific)
- Improve algorithms

#### 3. **Create Content**
- Record audio pronunciations
- Create video tutorials
- Translate historical texts
- Contribute stories in the dialect

#### 4. **Improve Code**
- Port tools to other languages
- Build mobile apps
- Create browser extensions
- Develop learning games

#### 5. **Community Building**
- Create learning groups
- Organize meetups
- Connect native speakers
- Document endangered variants

### Contribution Process

1. **Fork the repository**
   ```bash
   git clone https://github.com/CKCHDX/Nordic-Dialects.git
   cd Nordic-Dialects
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/bondska-new-vocabulary
   ```

3. **Make your changes**
   - Follow standards in ARCHITECTURE.md
   - Update relevant files
   - Add tests/examples if applicable

4. **Submit a Pull Request**
   - Describe your changes
   - Reference related issues
   - Include native speaker validation if possible

5. **Review & Merge**
   - Community review (linguists, native speakers)
   - Automated testing via CI/CD
   - Merge to main branch

### Code of Conduct
- Respect native speakers & their knowledge
- Prioritize linguistic accuracy over simplification
- Welcome all skill levels & backgrounds
- Maintain academic rigor & community inclusivity

---

## 📞 Support & Communication

### Contact Channels
- **GitHub Issues**: Report bugs, suggest features
- **Discussions**: Ask questions, share knowledge
- **Email**: [dialect-preservation@example.com]
- **Social Media**: @NordicDialects (Twitter, Instagram)

### Community Links
- **ISOF (Swedish Language Institute)**: https://www.isof.se
- **Local Heritage Societies**: See COMMUNITY/LOCAL-GROUPS.md
- **Academic Resources**: Listed in each dialect's HISTORY.md
- **Native Speaker Groups**: Contact info in NATIVE-SPEAKERS.md

---

## 📖 Documentation Index

### For Learners
- Start here: [Main dialect README in your chosen branch]
- Week 1: [LEARNING-GUIDE.md] → Phase 1
- Week 2: [LEARNING-GUIDE.md] → Phase 2
- Anytime: [ALPHABET.md] for reference
- Examples: [EXAMPLES.md] for context

### For Developers
- Architecture: [shared/ARCHITECTURE.md]
- Standards: [shared/PHONETIC-STANDARDS.md]
- Rules: [shared/RULE-FRAMEWORK.md]
- Testing: [shared/TESTING-GUIDELINES.md]

### For Linguists
- History: [HISTORY.md] in each dialect branch
- Rules detail: [RULES.md] in each dialect branch
- Phonetics: [ALPHABET.md] in each dialect branch
- Academic sources: Listed in each dialect

### For Native Speakers
- Community: [community/NATIVE-SPEAKERS.md]
- Validation: See CONTRIBUTING.md
- Recognition: Credited in each dialect's contributors list

---

## 🎯 Milestones & Roadmap

### Phase 1: Foundation (Now - Q1 2025)
✅ Bondska MVP (v1.0)
🔄 Gutnish core system
🔄 Elfdalska framework
📋 Project documentation

### Phase 2: Expansion (Q2-Q3 2025)
📋 5+ additional dialects
📋 Mobile app prototypes
📋 Community validation
📋 Academic partnerships

### Phase 3: Community (Q4 2025+)
📋 Native speaker network
📋 Learning platform integration
📋 Audio pronunciation database
📋 Multi-dialect learning paths

### Phase 4: Legacy (2026+)
📋 Archival integration (national archives)
📋 Academic publication
📋 Educational institution adoption
📋 International dialect preservation network

---

## 📜 License

All code, documentation, and resources are released under the **MIT License**.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

See LICENSE file for full text.

---

## 🙏 Acknowledgments

### Contributors & Advisors
- Native speakers of Västerbotten, Gotland, Jämtland, and other regions
- **ISOF (Institutet för språk och folkminnen)** for research guidance
- **Linguistic community** for support in preservation efforts
- **Open-source community** for tools and inspiration

### Cultural Partners
- Västerbottens Museum (Umeå)
- Gotland Museum & Archives
- Local heritage societies throughout Nordic region
- National archives of Sweden, Norway, Finland, Estonia

### Dedicated to
All speakers of endangered Nordic dialects, past and present. May their voices be heard and preserved for generations to come.

---

## 🔗 Quick Links

### Getting Started
- [Bondska (Main Project)](../../tree/bondska)
- [Gutnish/Gotlandic](../../tree/gutnish)
- [Elfdalska/Dalecarlian](../../tree/elfdalska)
- [All Dialects Map](#-dialect-coverage-map)

### Documentation
- [Contributing Guide](CONTRIBUTING.md)
- [Architecture & Standards](shared/ARCHITECTURE.md)
- [Learning System](shared/docs/learning-system.md)
- [Phonetic Standards](shared/PHONETIC-STANDARDS.md)

### Community
- [Native Speakers Resources](community/NATIVE-SPEAKERS.md)
- [Local Groups & Organizations](community/LOCAL-GROUPS.md)
- [Multi-Dialect Learning](community/LEARNING-PATHS.md)

### External
- [ISOF - Swedish Language Institute](https://www.isof.se)
- [GitHub Issues - Report or Discuss](../../issues)
- [GitHub Discussions - Community Chat](../../discussions)

---

## 📊 Status Dashboard

| Component | Status | Progress |
|-----------|--------|----------|
| **Bondska** | 🟢 Ready | v1.0 Complete |
| **Gutnish** | 🟡 In Progress | 60% |
| **Elfdalska** | 🟡 In Progress | 40% |
| **Framework** | 🟢 Ready | Standardized |
| **Documentation** | 🟢 Ready | Comprehensive |
| **Community** | 🟡 Growing | Expanding |
| **CI/CD Pipeline** | 🟢 Ready | Automated |

---

**Last Updated**: December 2025 | **Version**: 1.0 | **Maintained by**: Bondska Revival Project

🇸🇪 *"Hald fram nasar sork!"* (Keep the languages alive!) 🇸🇪

**Next step**: Choose a dialect, clone the branch, and start learning or contributing!
