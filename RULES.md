# 🗙️ Bondska Transformation Rules
## Comprehensive Linguistic Rules for Swedish ↔ Bondska Translation

---

## Overview

Bondska transformation rules are organized into 4 phases matching the learning system:
- **Phase 1**: Pronoun Shift (basic substitutions)
- **Phase 2**: Vowel Shifts (phonetic transformations)
- **Phase 3**: Apocope & Consonants (word endings & consonants)
- **Phase 4**: Grammar & Fluency (advanced features)

Each rule includes:
- **Pattern**: Regular expression for matching
- **Replacement**: What to transform to
- **Explanation**: Why this rule exists linguistically
- **Examples**: Real Bondska examples
- **Exceptions**: Words that don't follow the rule

---

## 🔢 Phase 1: Pronoun Shift (Week 1)

High-frequency word substitutions - the foundation of Bondska.

### 1.1 First Person Singular Pronoun

**Pattern**: `\bjag\b` (word boundary)
**Replacement**: `ja`
**Explanation**: The Swedish "jag" (I) becomes "ja" in Bondska - a common reduction of unstressed pronouns.
**Examples**:
- Swedish: "Jag heter Alex"
- Bondska: "ja héterålex"
- English: "My name is Alex"

**Exceptions**: None - consistent across all contexts

### 1.2 Second Person Singular Pronoun

**Pattern**: `\bdu\b`
**Replacement**: `dö`
**Explanation**: Swedish "du" (you-sing.) becomes "dö" with vowel shift.
**Examples**:
- Swedish: "Du är här"
- Bondska: "dö är här"
- English: "You are here"

**Exceptions**: None

### 1.3 Third Person Singular Pronouns

**Pattern A**: `\bhan\b` (he)
**Replacement**: `han`
**Explanation**: "han" remains the same in Bondska

**Pattern B**: `\bhon\b` (she)
**Replacement**: `hon`
**Explanation**: "hon" remains the same

**Pattern C**: `\bden\b` (it - common gender)
**Replacement**: `de` or `dén`
**Explanation**: Can be reduced or kept as "dén"

### 1.4 Plural Pronouns

**Pattern A**: `\bvi\b` (we)
**Replacement**: `vó`
**Explanation**: Swedish "vi" becomes "vó" in Bondska
**Examples**:
- Swedish: "Vi går här"
- Bondska: "vó går här"

**Pattern B**: `\bni\b` (you-pl.)
**Replacement**: `nó`
**Explanation**: Swedish "ni" becomes "nó"

**Pattern C**: `\bde\b` (they)
**Replacement**: `dö`
**Explanation**: Swedish "de" becomes "dö" with vowel shift
**Examples**:
- Swedish: "De går nu"
- Bondska: "dö gå nå"

### 1.5 Reflexive Pronoun

**Pattern**: `\bsig\b` (self)
**Replacement**: `séɡ` or `sej`
**Explanation**: Swedish "sig" becomes "séj" in Bondska with reduction
**Examples**:
- Swedish: "Han tvingar sig"
- Bondska: "han tvi̇ar séj"

### 1.6 Possessive Pronouns

| Swedish | Bondska | Pattern | Notes |
|---------|---------|---------|-------|
| min | mín | `\bmin\b` → `mín` | Vowel shift |
| din | dín | `\bdin\b` → `dín` | Vowel shift |
| hans | hans | unchanged | Remains same |
| hennes | héns | `\bhennes\b` → `héns` | Apocope |
| dess | des | `\bdess\b` → `des` | Apocope |
| vår | vår | unchanged | Remains same |
| er | ér | `\ber\b` → `ér` | Vowel shift |
| deras | dér | `\bderas\b` → `dér` | Apocope + vowel |

### 1.7 Basic Verbs

**To be (vara)**

| Swedish | Bondska | Pattern | Notes |
|---------|---------|---------|-------|
| är | är | unchanged | No change needed |
| var | vär | `\bvar\b` → `vär` | Vowel shift to ä |
| varit | värét | `varit` → `värét` | Apocope + shift |

**To go (gå)**

| Swedish | Bondska | Pattern | Notes |
|---------|---------|---------|-------|
| gå | gå | unchanged | Remains same |
| går | gå | `\bgår\b` → `gå` | Apocope (-r removed) |
| gick | gåck | vowel shift | Past tense vowel |
| gått | gått | unchanged | Participle |

**Negation (inte)**

**Pattern**: `\binte\b`
**Replacement**: `ikk` or `inté`
**Explanation**: Swedish negation "inte" becomes "ikk" in Bondska
**Examples**:
- Swedish: "Jag inte kan"
- Bondska: "ja ikk kan"
- English: "I cannot"

### 1.8 Common Question Words

| Swedish | Bondska | Pattern | Example |
|---------|---------|---------|----------|
| vad | vatt | `\bvad\b` → `vatt` | Vatt hätt? (What happened?) |
| vem | vem | unchanged | Vem kom? (Who came?) |
| var | vär | `\bvar\b` → `vär` | Vär är du? (Where are you?) |
| när | när | unchanged | När kom ni? (When did you come?) |
| hur | húr | `\bhur\b` → `húr` | Húr går det? (How are you?) |
| vilken | viĺk | `\bvilken\b` → `viĺk` | Vilk är bäst? (Which is best?) |

---

## 💧 Phase 2: Vowel Shifts (Week 2)

Phonetic transformations of vowels, reflecting Old Norse heritage.

### 2.1 A → Å Shift

**Pattern**: `a` in stressed syllables (selective)
**Replacement**: `å`
**Explanation**: Open front /a/ becomes open back rounded /å/ - characteristic of Northern Swedish dialects
**Examples**:
- Swedish: "kar" (beloved)
- Bondska: "kår"
- Swedish: "nat" (night)
- Bondska: "nåt"

**Exceptions**:
- Before /r/: "kar" → "kår" (applies)
- Initial position: Variable (kar → kår or kar)
- Affricates: Often preserved

### 2.2 E → Ä Shift

**Pattern**: `e` in open syllables
**Replacement**: `ä`
**Explanation**: Close-mid front /e/ opens to open-mid front /ä/
**Examples**:
- Swedish: "le" (smile)
- Bondska: "lä"
- Swedish: "se" (see)
- Bondska: "sä"

**Exceptions**:
- In final position: Often preserved as /e/
- Before fricatives: Variable

### 2.3 O → U Shift

**Pattern**: `o` in stressed syllables
**Replacement**: `u`
**Explanation**: Mid back /o/ closes to close back /u/
**Examples**:
- Swedish: "bok" (book)
- Bondska: "buk"
- Swedish: "not" (note)
- Bondska: "nut"

**Exceptions**:
- Before velars: Variable (bok → buk or bok)
- Initial position: Often preserved

### 2.4 Ö → Ô Shift

**Pattern**: `ö` in stressed syllables
**Replacement**: `ô` (or `ɔ`)
**Explanation**: Open-mid front rounded /ö/ lowers to open back rounded
**Examples**:
- Swedish: "söck" (search)
- Bondska: "sôck"
- Swedish: "kör" (run)
- Bondska: "kôr"

### 2.5 Y → Ö Shift

**Pattern**: `y` in some contexts
**Replacement**: `ö`
**Explanation**: Close front rounded /y/ opens to mid front rounded /ö/ in certain positions
**Examples**:
- Swedish: "ny" (new)
- Bondska: "nö" (or "ny")
- Variable in speech

### 2.6 Vowel Lengthening

**Pattern**: Short vowels in stressed syllables (selective)
**Replacement**: Lengthened vowel [Vː]
**Explanation**: Bondska tends to lengthen stressed vowels for emphasis
**Examples**:
- Swedish: "mat" (food) - [mat]
- Bondska: "måt" - [måːt]
- Swedish: "bad" (bath) - [baːd]
- Bondska: "båd" - [båːd]

### 2.7 I → É Shift (Archaic)

**Pattern**: `i` in unstressed syllables (rare)
**Replacement**: `é`
**Explanation**: Close front /i/ reduces to mid /é/ in weak positions (archaic feature)
**Examples**: Rare in modern Bondska

---

## ✍️ Phase 3: Apocope & Consonants (Week 3)

Word-ending omission and consonant changes.

### 3.1 Apocope (-ER → -ÄR or ∅)

**Pattern**: `-er` suffix (plural/verb present)
**Replacement**: `-är` or dropped
**Explanation**: Unstressed suffix deletion or vowel shift
**Examples**:
- Swedish: "kattar" (cats)
- Bondska: "katt" or "kätt"
- Swedish: "gåer" (goes - archaic)
- Bondska: "gå"

**Context**:
- Plural nouns: Often dropped
- Present tense: Often shifted to är
- Adjectives: Varies

### 3.2 Apocope (-ER → -É)

**Pattern**: `-er` suffix in certain positions
**Replacement**: `-é` (schwa-like)
**Explanation**: Sometimes reduced to single vowel sound
**Examples**:
- Swedish: "hett" (hot)
- Bondska: "hétt"

### 3.3 Word-Final Consonant Retention

Unlike Standard Swedish, Bondska preserves final consonants:

**D** at word-end
**Pattern**: Final `-d`
**Replacement**: Pronounced [d]
**Explanation**: Final /d/ is sounded in Bondska (Swedish often omits it)
**Examples**:
- Swedish: "ord" [uɔr] (word)
- Bondska: "uɔrd" [uɔrd]
- Swedish: "god" [guː] (good)
- Bondska: "gôd" [gôːd]

**T** at word-end
**Pattern**: Final `-t`
**Replacement**: Pronounced [t]
**Examples**:
- Swedish: "det" [deː] (it)
- Bondska: "dett" [detːt]
- Swedish: "att" [atː] (that)
- Bondska: "att" [atːt]

### 3.4 Consonant Softening (Palatalization)

**T → J Before Front Vowels**

**Pattern**: `/t/ + /i, e, y/`
**Replacement**: `[tj]` or `[ç]`
**Explanation**: Alveolar stop becomes palatal before front vowels
**Examples**:
- Swedish: "tio" (ten)
- Bondska: "tjo" or "cjo"
- Swedish: "tie" (nothing)
- Bondska: "tje"

**Exceptions**:
- In some words, preserved as /t/
- Varies by speaker and region

**D → J Before Front Vowels**

**Pattern**: `/d/ + /i, e, y/`
**Replacement**: `[dj]`
**Explanation**: Alveolar stop becomes palatal
**Examples**:
- Swedish: "Djur" (animal)
- Bondska: "djúr"

**N → NJ Before Front Vowels**

**Pattern**: `/n/ + /i, e, y/`
**Replacement**: `[nj]`
**Examples**:
- Swedish: "nisse" (gnome)
- Bondska: "njiss"

### 3.5 Consonant Cluster Simplification

**Pattern A**: `nd` → `n` (reduction)
**Explanation**: Alveolar nasal-stop cluster simplifies
**Examples**:
- Swedish: "land" (country)
- Bondska: "lan" (reduced)

**Pattern B**: `ng` → `ng` (preserved)
**Explanation**: Velar nasal-stop cluster preserved in Bondska
**Examples**:
- Swedish: "lång" (long)
- Bondska: "lång" (same)

**Pattern C**: `sk` → `ʂ` (retroflexed)
**Explanation**: Alveolar-velar cluster becomes retroflexed fricative
**Examples**:
- Swedish: "ska" (shall)
- Bondska: "ʂa"

### 3.6 Apocope of Final Vowels

**Pattern**: Final unstressed `-e`
**Replacement**: Dropped or retained
**Explanation**: Weak word-final -e may be omitted
**Examples**:
- Swedish: "huse" (houses)
- Bondska: "hus" (often dropped)
- Swedish: "ute" (outside)
- Bondska: "ut" or "utə"

**Exceptions**:
- In careful speech, often retained
- Varies by region

---

## 📜 Phase 4: Grammar & Fluency (Week 4+)

Advanced linguistic features and grammatical nuances.

### 4.1 Gender System Markers

Bondska maintains Old Norse gender distinctions:

**Masculine** (Han)
- Article: "en" → "en"
- Examples: "en håst" (a horse)

**Feminine** (Hun)
- Article: "en" → "en" (same)
- But noun takes feminine agreement
- Examples: "en häst" (a mare - archaic)

**Neuter** (It)
- Article: "ett" → "ett"
- Examples: "ett hus" (a house)

### 4.2 Definite Article Suffixes

**Singular Definite**

| Gender | Swedish | Bondska | Example |
|--------|---------|---------|----------|
| Masc. | hunden | hundan | the dog |
| Fem. | hästen | hästan | the mare |
| Neut. | huset | husét | the house |

**Plural Definite**

| Gender | Swedish | Bondska | Example |
|--------|---------|---------|----------|
| All | hundarna | hundar | the dogs |

### 4.3 Case System (Dative)

Bondska retains dative case in some contexts:

**Nominative**: Subject position
- "Hunden läugar" (The dog runs)

**Accusative**: Direct object
- "Jag ser hundan" (I see the dog)

**Dative**: Indirect object (location/direction)
- "Jag går husan" (I go to the house)

**Genitive**: Possession
- "Hundens håret" (The dog's hair)

### 4.4 Verb Conjugation

**Present Tense**

| Person | Swedish | Bondska | Pattern |
|--------|---------|---------|----------|
| 1st sing. | går | gå | Apocope |
| 2nd sing. | går | gå | Apocope |
| 3rd sing. | går | gå | Apocope |
| 1st plural | går | gå | Apocope |
| 2nd plural | går | gå | Apocope |
| 3rd plural | går | gå | Apocope |

**Past Tense**

| Pattern | Swedish | Bondska | Notes |
|---------|---------|---------|-------|
| Weak -ade | gick | gåck | Apocope of -e, vowel shift |
| Weak -ede | drog | drög | Similar pattern |
| Strong | var | vär | Vowel shift |

### 4.5 Adjective Agreement

**Indefinite**

| Gender | Swedish | Bondska | Example |
|--------|---------|---------|----------|
| Masc./Fem. | en stor hund | en stôr hund | a big dog |
| Neut. | ett stort hus | ett stôrt hus | a big house |
| Plural | stora hundar | stôra hundar | big dogs |

**Definite**
- Adds suffix: "en stora hundan" (the big dog)

### 4.6 Negation Patterns

**Simple Negation**
- Swedish: "Jag inte kan"
- Bondska: "ja ikk kan"

**Double Negation** (common in dialects)
- Bondska: "ja ikk kan ikk" (I cannot not)
- Emphasis through repetition

### 4.7 Tonal Accent Patterns

Bondska uses word tones to distinguish meaning:

**Accent 1** (Single peak): Monosyllabic and simple words
- "k̩aː" (cat) - rising-falling

**Accent 2** (Double peak): Compound words
- "k̩̩aːtor" (cats) - rising-falling-rising

These affect:
- Word meaning
- Grammatical function
- Dialect variation

### 4.8 Dialectal Variations

**Coastal Bondska** (Bohuslän)
- More conservative
- Clearer articulation
- More urban Swedish influence

**Inland Bondska** (Västerbotten)
- More innovative
- Softer consonants
- More archaic features
- More melodic

### 4.9 Archaic Features

Some Bondska speakers retain Old Norse features:

**Dual Number**: Few instances
- "Vi två" (we two) - archaic

**Subjunctive Mood**: Rare
- "Om jag vore" (if I were) - mostly Standard Swedish form

**Infinitive Forms**: Varying endings
- "att gå" (to go) - standard
- "gå" (to go) - reduced infinitive

---

## 🔉 Rule Application Algorithm

When translating Swedish → Bondska, apply rules in this order:

1. **Tokenize** the Swedish text into words
2. **Apply Phase 1 rules** (pronouns, basic words)
3. **Apply Phase 2 rules** (vowel shifts)
4. **Apply Phase 3 rules** (apocope, consonants)
5. **Apply Phase 4 rules** (grammar, tones) if advanced
6. **Combine** tokens back into text
7. **Output** Bondska text

---

## 📱 Testing & Validation

Each rule should be validated with:
- Native speaker confirmation
- Multiple example sentences
- Exception documentation
- Regional variation notes
- Historical references

---

**Last Updated**: December 2025 | **Version**: 1.0

*Hald fram Bondska!* (Keep Bondska alive!)