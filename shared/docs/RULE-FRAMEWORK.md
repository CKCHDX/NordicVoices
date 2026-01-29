# Rule Framework for Nordic Dialect Translation

## Building Transformation Rules for Dialect Translation Systems

This guide explains how to design, implement, and test linguistic transformation rules for Nordic dialect translation engines.

---

## Table of Contents

1. [Overview](#overview)
2. [Rule Structure](#rule-structure)
3. [Rule Categories](#rule-categories)
4. [Priority & Application Order](#priority--application-order)
5. [Pattern Matching](#pattern-matching)
6. [Testing Rules](#testing-rules)
7. [Documentation Standards](#documentation-standards)
8. [Common Pitfalls](#common-pitfalls)

---

## Overview

### What Are Transformation Rules?

Transformation rules are systematic patterns that convert Standard Swedish to a specific dialect. They encode linguistic knowledge about:

- **Phonological changes** (sound shifts)
- **Morphological changes** (word structure)
- **Lexical substitutions** (word replacements)
- **Syntactic patterns** (grammar changes)

### Rule-Based vs. Dictionary Approach

**Rule-Based (Recommended)**:
- ✅ Handles unseen words
- ✅ Captures systematic patterns
- ✅ Smaller data footprint
- ✅ Linguistically motivated

**Dictionary-Only**:
- ❌ Limited to known words
- ❌ Misses regular patterns
- ❌ Large data requirements
- ❌ No generalization

**Best Practice**: Combine both approaches - use rules for systematic changes and dictionaries for irregular high-frequency words.

---

## Rule Structure

### Basic Rule Template

```json
{
  "rule_id": "unique_identifier",
  "name": "Human-readable name",
  "category": "rule_category",
  "phase": 1-4,
  "priority": "high|medium|low",
  "pattern": "regex_pattern",
  "replacement": "replacement_string",
  "condition": "when this rule applies",
  "examples": [
    {"swedish": "input", "dialect": "output", "english": "meaning"}
  ],
  "exceptions": ["list", "of", "exceptions"],
  "linguistic_rationale": "why this rule exists"
}
```

### Required Fields

1. **rule_id**: Unique identifier (e.g., `p1_pronoun_jag`, `vowel_e_to_ei`)
2. **name**: Descriptive name (e.g., "First person pronoun substitution")
3. **category**: Rule type (see categories below)
4. **phase**: Learning phase (1-4)
5. **pattern**: Regular expression or search pattern
6. **replacement**: What to replace the pattern with

### Optional But Recommended

- **priority**: For conflict resolution
- **condition**: Context where rule applies
- **examples**: 3-5 demonstration cases
- **exceptions**: Known exceptions to document
- **linguistic_rationale**: Old Norse origin, phonetic reason, etc.

---

## Rule Categories

### 1. Pronoun Substitution (Phase 1)

**Purpose**: Replace high-frequency pronouns

**Example**:
```json
{
  "rule_id": "pron_jag_to_ja",
  "category": "pronoun",
  "pattern": "\\bjag\\b",
  "replacement": "ja",
  "examples": [
    {"swedish": "Jag heter Anna", "dialect": "Ja heter Anna"}
  ]
}
```

**Pattern Tips**:
- Use `\\b` for word boundaries
- Case-insensitive matching: `(?i)jag`
- Capture context if needed: `(\\w+)jag(\\w+)`

### 2. Vowel Transformation (Phase 2)

**Purpose**: Systematic vowel shifts

**Types**:
- **Diphthongization**: `e → ei`, `ö → øy`
- **Monophthongization**: `au → å`
- **Vowel darkening**: `a → å`
- **Vowel raising/lowering**: `o → u`, `e → i`

**Example**:
```json
{
  "rule_id": "vowel_e_to_ei",
  "category": "vowel_shift",
  "pattern": "([^aeiouåäö])e([^aeiouåäö])",
  "replacement": "$1ei$2",
  "condition": "short e in monosyllabic stems",
  "examples": [
    {"swedish": "sten", "dialect": "stein"},
    {"swedish": "ben", "dialect": "bein"}
  ]
}
```

**Pattern Tips**:
- Capture surrounding consonants: `([^vowels])vowel([^vowels])`
- Preserve context with capture groups: `$1`, `$2`
- Consider syllable boundaries
- Check for word endings: `e(?!$)`

### 3. Apocope (Phase 3)

**Purpose**: Drop final unstressed vowels

**Types**:
- **Verb -a deletion**: `tala → tal`
- **Verb -er deletion**: `talar → tala`
- **Noun -e deletion**: `pojke → pojk`

**Example**:
```json
{
  "rule_id": "apocope_verb_a",
  "category": "apocope",
  "pattern": "a$",
  "replacement": "",
  "condition": "infinitive and present tense verbs",
  "examples": [
    {"swedish": "tala", "dialect": "tal"},
    {"swedish": "äta", "dialect": "ät"}
  ],
  "exceptions": ["vara", "ha", "få"]
}
```

**Pattern Tips**:
- End of word: `a$`
- Multiple endings: `(a|e|er)$`
- Preserve root: `^(.+?)(a|er)$` → `$1`

### 4. Consonant Shifts (Phase 3)

**Purpose**: Change consonant pronunciation

**Types**:
- **Retroflexion**: `rd → ɖ`, `rl → ɭ`, `rn → ɳ`
- **Palatalization**: `k → ɕ`, `g → j` (before front vowels)
- **Lenition**: `t → d`, `k → g` (between vowels)

**Example**:
```json
{
  "rule_id": "retroflex_rd_to_L",
  "category": "consonant_shift",
  "pattern": "rd\\b",
  "replacement": "L",
  "condition": "word-final position in Thick L dialects",
  "examples": [
    {"swedish": "bord", "dialect": "boL"},
    {"swedish": "gård", "dialect": "gåL"}
  ]
}
```

### 5. Lexical Substitution (Phase 1)

**Purpose**: Replace entire words

**Example**:
```json
{
  "rule_id": "lex_och_to_a",
  "category": "lexical",
  "pattern": "\\boch\\b",
  "replacement": "å",
  "linguistic_rationale": "From Old Norse 'ok'",
  "examples": [
    {"swedish": "du och jag", "dialect": "du å jag"}
  ]
}
```

### 6. Morphological (Phase 4)

**Purpose**: Grammar and word structure changes

**Types**:
- Definite article changes
- Case preservation (dative)
- Gender system variations

---

## Priority & Application Order

### Why Order Matters

Rules interact with each other. Apply in wrong order → wrong output.

**Example Problem**:
```
Input: "äta"

Wrong order:
1. Apocope first: äta → ät
2. Vowel shift: ät → ät (no 'a' to shift!)

Right order:
1. Vowel shift: äta → äta (check if vowel shift applies)
2. Apocope: äta → ät
```

### Standard Application Order

```
Phase 1: High-frequency word substitutions
├── 1.1 Pronouns (jag, du, vi...)
├── 1.2 Particles (och, inte, men...)
└── 1.3 Common verbs (vara, ha, måste...)

Phase 2: Vowel transformations
├── 2.1 Diphthongization (e→ei, ö→øy)
├── 2.2 Monophthongization (au→å)
└── 2.3 Vowel darkening/lightening

Phase 3: Consonants and endings
├── 3.1 Consonant shifts (rd→ɖ, k→ɕ)
├── 3.2 Verb apocope (-a, -er deletion)
└── 3.3 Noun apocope (-e deletion)

Phase 4: Advanced morphology
├── 4.1 Definite articles
├── 4.2 Case system
└── 4.3 Complex grammar
```

### Priority Levels

When rules conflict:

1. **High priority**: Exceptions, irregular forms, high-frequency words
2. **Medium priority**: Regular phonological rules
3. **Low priority**: Optional or stylistic variations

**Example**:
```json
{
  "rule_id": "exception_vara",
  "pattern": "\\bvara\\b",
  "replacement": "vara",
  "priority": "high",
  "note": "Don't apply apocope to 'vara'"
}
```

---

## Pattern Matching

### Regular Expression Basics

#### Word Boundaries
```regex
\b        - Word boundary
\bjag\b   - Matches "jag" but not "jagar"
```

#### Character Classes
```regex
[aeiou]     - Any vowel
[^aeiou]    - Any non-vowel
[a-z]       - Any lowercase letter
```

#### Quantifiers
```regex
a?          - 0 or 1 'a'
a*          - 0 or more 'a'
a+          - 1 or more 'a'
a{2,4}      - 2 to 4 'a's
```

#### Capture Groups
```regex
(stem)(ending)      - Capture two parts
$1$2                - Reference in replacement
```

### Dialect-Specific Patterns

#### Match Swedish vowels
```regex
[aeiouåäö]
```

#### Match consonants
```regex
[bcdfghjklmnpqrstvwxyz]
```

#### Match diphthongs
```regex
(ei|øy|au)
```

#### Retroflexion patterns
```regex
r[dlnst]     - rd, rl, rn, rs, rt
```

---

## Testing Rules

### Test Case Structure

```json
{
  "test_id": "test_001",
  "rule_id": "vowel_e_to_ei",
  "input": "sten",
  "expected": "stein",
  "actual": "",
  "status": "pass|fail",
  "notes": ""
}
```

### Testing Strategy

1. **Positive tests**: Rule should apply
   ```
   Input: "sten"
   Expected: "stein"
   Rule: e → ei
   ```

2. **Negative tests**: Rule should NOT apply
   ```
   Input: "tre" (ends with 'e', weak ending)
   Expected: "tre" (not "trei")
   Rule: e → ei should not apply to final unstressed 'e'
   ```

3. **Edge cases**: Boundaries, exceptions
   ```
   Input: "hemma" (double consonant)
   Rule: e → ei
   Check: Should become "heimma" or stay "hemma"?
   ```

4. **Integration tests**: Multiple rules together
   ```
   Input: "jag äter hemma"
   Rules: pronoun, apocope, vowel shift
   Expected: "ja ät heimm" (or appropriate output)
   ```

### Test Coverage Goals

- ✅ At least 5 test cases per rule
- ✅ Cover all examples in rule documentation
- ✅ Include known exceptions
- ✅ Test rule interactions
- ✅ Verify with native speaker if possible

---

## Documentation Standards

### Rule Documentation Template

```markdown
## Rule: E → EI Diphthongization

**Rule ID**: `vowel_e_to_ei`

**Category**: Vowel Transformation

**Phase**: 2

**Description**: 
Short /e/ in stressed syllables becomes the diphthong [eɪ], restoring the Old Norse diphthong 'ei'.

**Pattern**: `([^aeiouåäö])e([^aeiouåäö])`

**Replacement**: `$1ei$2`

**Linguistic Background**:
Old Norse had the diphthong 'ei' (as in 'steinn' = stone), which was simplified to 'e' in Modern Swedish ('sten'). Many dialects preserve this original diphthong.

**Examples**:
| Swedish | Dialect | English | Old Norse |
|---------|---------|---------|-----------|
| sten | stein | stone | steinn |
| ben | bein | leg/bone | bein |
| hem | heim | home | heim |

**Exceptions**:
- Final unstressed 'e' is not diphthongized
- Foreign loanwords may not follow this pattern
- Some proper names remain unchanged

**Test Cases**:
- sten → stein ✓
- ben → bein ✓
- tre → tre (final 'e', no change) ✓
```

---

## Common Pitfalls

### 1. Over-Application

**Problem**: Rule applies too broadly
```
Rule: a → å everywhere
Result: "tala" → "tålå" (wrong!)
```

**Solution**: Add context constraints
```
Rule: a → å in specific contexts (before r, l, n)
Result: "tala" → "tala" but "var" → "vår" ✓
```

### 2. Under-Application

**Problem**: Rule misses valid cases
```
Rule: \bsten\b → stein (only exact match "sten")
Miss: "stenarna" (the stones)
```

**Solution**: Use flexible patterns
```
Rule: sten → stein (anywhere in word)
Result: "stenarna" → "steinarna" ✓
```

### 3. Wrong Order

**Problem**: Rules applied in wrong sequence
```
Order: Apocope before vowel shift
Input: "tala"
1. Apocope: tala → tal
2. Vowel shift: tal → tål (wrong!)
```

**Solution**: Document and enforce order
```
Order: Vowel shift before apocope
Input: "tala"
1. Vowel shift: tala → tåla
2. Apocope: tåla → tål ✓
```

### 4. Missing Exceptions

**Problem**: Irregular words follow regular rule
```
Rule: All verbs drop -a
Input: "vara" (to be)
Output: "var" (was) - wrong meaning!
```

**Solution**: Document and handle exceptions
```
Exceptions: ["vara", "ha", "få"]
Priority: High-priority exception list checked first
```

### 5. Case Sensitivity

**Problem**: Case not handled properly
```
Rule: jag → ja
Input: "Jag"
Output: "Jag" (no change!)
```

**Solution**: Case-insensitive pattern or multiple patterns
```
Rule: (?i)jag → ja (case insensitive)
OR
Rules: {
  "Jag": "Ja",
  "jag": "ja"
}
```

---

## Best Practices

### Do:
- ✅ Test rules with at least 10 example sentences
- ✅ Document linguistic rationale (Old Norse origin, phonetic reason)
- ✅ Include IPA pronunciation in examples
- ✅ Specify application phase and priority
- ✅ List known exceptions explicitly
- ✅ Validate with native speakers when possible

### Don't:
- ❌ Create overly complex regex that's hard to maintain
- ❌ Forget to test rule interactions
- ❌ Apply rules in arbitrary order
- ❌ Ignore exceptions and edge cases
- ❌ Skip documentation because "the code is self-explanatory"

---

## Tools & Resources

### Regular Expression Testers
- [Regex101](https://regex101.com/) - Test patterns online
- [RegExr](https://regexr.com/) - Visual regex tester

### Linguistic References
- Old Norse dictionaries for etymology
- IPA charts for phonetic notation
- Academic papers on dialect features
- ISOF (Swedish Language Institute) resources

### Validation
- Native speaker consultation (essential!)
- Academic linguistic sources
- Historical texts and recordings
- Cross-reference with other dialects

---

## Example: Building a Complete Rule

Let's build a rule for "E → EI diphthongization" step by step.

### Step 1: Identify the Pattern
- **Observation**: "sten" is pronounced "stein" in many dialects
- **Pattern**: Short 'e' becomes 'ei'
- **Context**: In monosyllabic stems, stressed syllables

### Step 2: Define the Rule
```json
{
  "rule_id": "vowel_e_to_ei",
  "name": "E to EI diphthongization",
  "category": "vowel_shift",
  "phase": 2
}
```

### Step 3: Create the Pattern
```json
{
  "pattern": "([^aeiouåäö])e([^aeiouåäö])",
  "replacement": "$1ei$2"
}
```
Matches: consonant + e + consonant

### Step 4: Add Examples
```json
{
  "examples": [
    {"swedish": "sten", "dialect": "stein", "english": "stone"},
    {"swedish": "ben", "dialect": "bein", "english": "leg"},
    {"swedish": "hem", "dialect": "heim", "english": "home"}
  ]
}
```

### Step 5: Document Exceptions
```json
{
  "exceptions": [
    "Final unstressed 'e' (tre, inte)",
    "Some loanwords (fem, fem)"
  ]
}
```

### Step 6: Add Linguistic Context
```json
{
  "old_norse_origin": "steinn",
  "ipa": "[steɪn]",
  "linguistic_rationale": "Restores Old Norse diphthong 'ei'"
}
```

### Step 7: Test
```json
{
  "tests": [
    {"input": "sten", "expected": "stein", "status": "pass"},
    {"input": "ben", "expected": "bein", "status": "pass"},
    {"input": "tre", "expected": "tre", "status": "pass"}
  ]
}
```

### Step 8: Verify with Native Speaker
Get confirmation from someone who speaks the dialect!

---

## Conclusion

Building effective transformation rules requires:
1. **Linguistic knowledge** - understanding the patterns
2. **Technical skill** - writing good regex and code
3. **Testing discipline** - thorough validation
4. **Documentation** - clear explanations for maintainers

Follow this framework to create rules that are:
- **Accurate**: Produce correct dialect forms
- **Maintainable**: Easy for others to understand and modify
- **Testable**: Can be validated systematically
- **Documented**: Well-explained with examples

---

**Version**: 1.0  
**Last Updated**: December 2025  
**Maintained by**: Nordic Dialects Preservation Project
