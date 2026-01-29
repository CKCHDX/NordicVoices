# Testing Guidelines for Nordic Dialect Tools

## Quality Assurance Procedures for Translation Systems

This document outlines testing strategies, quality metrics, and validation procedures for Nordic dialect translation tools.

---

## Table of Contents

1. [Overview](#overview)
2. [Testing Levels](#testing-levels)
3. [Test Case Design](#test-case-design)
4. [Validation Procedures](#validation-procedures)
5. [Quality Metrics](#quality-metrics)
6. [CI/CD Integration](#cicd-integration)
7. [Native Speaker Validation](#native-speaker-validation)

---

## Overview

### Why Test?

Dialect translation is complex:
- **Linguistic accuracy** is critical
- **Edge cases** are common
- **Rule interactions** can cause bugs
- **Regressions** must be caught early
- **Native speaker trust** depends on quality

### Testing Philosophy

1. **Accuracy over coverage**: Better to handle 100 words correctly than 1000 words poorly
2. **Native speaker validation**: Technical tests are necessary but not sufficient
3. **Continuous improvement**: Add tests as you discover issues
4. **Documentation**: Test cases serve as examples for users

---

## Testing Levels

### Level 1: Unit Tests (Individual Rules)

**Purpose**: Test each transformation rule in isolation

**Scope**: Single rule application

**Example**:
```python
def test_pronoun_jag_to_ja():
    rule = PronounRule("jag", "ja")
    assert rule.apply("jag heter") == "ja heter"
    assert rule.apply("Jag") == "Ja"
    assert rule.apply("jagar") == "jagar"  # Should not match
```

**Coverage Goal**: 100% of all rules

**Test Cases Per Rule**: Minimum 5
- 2-3 positive (rule applies)
- 1-2 negative (rule doesn't apply)
- 1 edge case

### Level 2: Integration Tests (Rule Combinations)

**Purpose**: Test multiple rules working together

**Scope**: Full translation pipeline

**Example**:
```python
def test_translation_pipeline():
    translator = BondskaTranslator()
    
    # Test: pronoun + verb apocope
    assert translator.translate("jag talar") == "ja tala"
    
    # Test: pronoun + vowel shift + apocope
    assert translator.translate("jag äter sten") == "ja ät stein"
```

**Coverage Goal**: All common rule combinations

**Test Cases**: 20-50 multi-rule sentences

### Level 3: Acceptance Tests (Full Sentences)

**Purpose**: Test realistic usage scenarios

**Scope**: Complete sentences and paragraphs

**Example**:
```python
def test_greeting_conversation():
    translator = BondskaTranslator()
    
    swedish = "Hej, jag heter Anna och jag bor i Stockholm"
    expected = "Hej, ja heit Anna å ja bor i Stockholm"
    
    assert translator.translate(swedish) == expected
```

**Coverage Goal**: All use cases and user scenarios

**Test Categories**:
- Greetings
- Questions
- Statements
- Negations
- Descriptions
- Conversations

### Level 4: Regression Tests

**Purpose**: Ensure bugs don't reappear

**Scope**: Previously fixed issues

**Process**:
1. Bug is reported
2. Create test case that fails
3. Fix the bug
4. Test case now passes
5. Keep test case permanently

**Example**:
```python
def test_issue_42_sten_not_diphthongizing():
    """
    Regression test for GitHub issue #42
    'sten' was not being converted to 'stein'
    """
    translator = BondskaTranslator()
    assert translator.translate("sten") == "stein"
```

---

## Test Case Design

### Test Case Template

```json
{
  "test_id": "TEST_001",
  "category": "pronoun_substitution",
  "description": "First person pronoun 'jag' → 'ja'",
  "input": "Jag heter Alex",
  "expected_output": "Ja heter Alex",
  "actual_output": "",
  "status": "pass|fail|skip",
  "rules_tested": ["pron_jag_to_ja"],
  "phase": 1,
  "difficulty": "beginner",
  "notes": "",
  "verified_by_native_speaker": false,
  "date_created": "2025-12-01"
}
```

### Good Test Cases

#### Positive Tests (Rule Should Apply)
```json
{
  "input": "jag",
  "expected": "ja",
  "note": "Simple pronoun substitution"
}
```

#### Negative Tests (Rule Should NOT Apply)
```json
{
  "input": "jagar",
  "expected": "jagar",
  "note": "'jag' is part of larger word, no substitution"
}
```

#### Edge Cases
```json
{
  "input": "Jag!",
  "expected": "Ja!",
  "note": "Pronoun with punctuation"
}
```

#### Boundary Tests
```json
{
  "input": "jag jag jag",
  "expected": "ja ja ja",
  "note": "Multiple occurrences"
}
```

### Test Coverage Matrix

| Category | Beginner | Intermediate | Advanced | Total |
|----------|----------|--------------|----------|-------|
| **Pronouns** | 10 | 5 | 3 | 18 |
| **Vowel Shifts** | 8 | 12 | 6 | 26 |
| **Apocope** | 6 | 10 | 8 | 24 |
| **Consonants** | 4 | 8 | 10 | 22 |
| **Lexical** | 15 | 10 | 5 | 30 |
| **Full Sentences** | 20 | 15 | 10 | 45 |
| **Total** | 63 | 60 | 42 | **165** |

**Minimum Coverage Goal**: 100 test cases per dialect

---

## Validation Procedures

### Automated Validation

#### JSON Syntax Check
```bash
# Validate all JSON files
find . -name "*.json" -exec python3 -m json.tool {} \; > /dev/null
```

#### Rule Pattern Validation
```python
def validate_rule_patterns():
    """Ensure all regex patterns are valid"""
    import re
    for rule in rules:
        try:
            re.compile(rule['pattern'])
        except re.error as e:
            raise ValueError(f"Invalid pattern in {rule['rule_id']}: {e}")
```

#### Consistency Checks
```python
def check_consistency():
    """Verify examples match rule output"""
    for rule in rules:
        for example in rule['examples']:
            output = apply_rule(rule, example['input'])
            assert output == example['expected'], \
                f"Rule {rule['rule_id']} failed on example"
```

### Manual Validation

#### Linguistic Review Checklist

- [ ] **IPA accuracy**: Pronunciation notations correct
- [ ] **Old Norse etymology**: Historical connections verified
- [ ] **Regional variations**: Dialect-specific features documented
- [ ] **Exceptions**: Known irregular forms listed
- [ ] **Example quality**: Examples are natural and common

#### Code Quality Checklist

- [ ] **Readable code**: Clear variable names and structure
- [ ] **Comments**: Complex logic explained
- [ ] **Error handling**: Edge cases handled gracefully
- [ ] **Performance**: No obvious inefficiencies
- [ ] **Maintainability**: Easy for others to modify

---

## Quality Metrics

### Accuracy Metrics

#### Rule Accuracy
```
Rule Accuracy = Correct Outputs / Total Test Cases × 100%
```

**Target**: ≥ 95% per rule

#### Translation Accuracy
```
Translation Accuracy = Correct Translations / Total Sentences × 100%
```

**Target**: ≥ 90% for full sentences

#### Native Speaker Agreement
```
Native Speaker Agreement = Native Speaker Approved / Total Validated × 100%
```

**Target**: ≥ 85% (native speakers may disagree on regional variations)

### Coverage Metrics

#### Rule Coverage
```
Rule Coverage = Rules With Tests / Total Rules × 100%
```

**Target**: 100%

#### Code Coverage
```
Code Coverage = Lines Executed in Tests / Total Lines × 100%
```

**Target**: ≥ 80%

### Quality Scoring

```
Overall Quality Score = (
    Rule Accuracy × 0.30 +
    Translation Accuracy × 0.30 +
    Native Speaker Agreement × 0.25 +
    Rule Coverage × 0.10 +
    Code Coverage × 0.05
)
```

**Grading**:
- **A (90-100%)**: Production ready
- **B (80-89%)**: Good, minor improvements needed
- **C (70-79%)**: Functional, needs work
- **D (60-69%)**: Significant issues
- **F (<60%)**: Not ready for release

---

## CI/CD Integration

### GitHub Actions Workflow

```yaml
name: Dialect Translation Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Validate JSON
        run: |
          find . -name "*.json" | while read f; do
            python3 -m json.tool "$f" > /dev/null || exit 1
          done
      
      - name: Run Unit Tests
        run: |
          python3 -m pytest tests/unit/ -v
      
      - name: Run Integration Tests
        run: |
          python3 -m pytest tests/integration/ -v
      
      - name: Check Translation Accuracy
        run: |
          python3 tests/accuracy_check.py --threshold 0.90
      
      - name: Generate Coverage Report
        run: |
          python3 -m pytest --cov=. --cov-report=html
```

### Pre-Commit Hooks

```bash
# .git/hooks/pre-commit

#!/bin/bash

# Run quick tests before committing
echo "Running pre-commit tests..."

# Validate JSON
echo "Validating JSON files..."
find . -name "*.json" -exec python3 -m json.tool {} \; > /dev/null
if [ $? -ne 0 ]; then
    echo "❌ JSON validation failed"
    exit 1
fi

# Run fast unit tests
echo "Running unit tests..."
python3 -m pytest tests/unit/ -q
if [ $? -ne 0 ]; then
    echo "❌ Unit tests failed"
    exit 1
fi

echo "✅ Pre-commit tests passed"
exit 0
```

---

## Native Speaker Validation

### Validation Process

1. **Recruit Native Speakers**
   - Reach out to dialect communities
   - Contact local heritage societies
   - Engage academic linguists
   - Use social media (Swedish forums, Facebook groups)

2. **Prepare Validation Materials**
   ```
   - 50 translated sentences
   - Category coverage (greetings, questions, statements, etc.)
   - Difficulty range (beginner to advanced)
   - Context provided (who would say this, when, where)
   ```

3. **Validation Form**
   ```markdown
   ## Translation Validation
   
   **Sentence**: [Swedish text]
   **Translation**: [Dialect text]
   **Context**: [When/where/who]
   
   **Accuracy** (1-5):
   ○ 1 - Completely wrong
   ○ 2 - Mostly wrong
   ○ 3 - Partially correct
   ○ 4 - Mostly correct
   ○ 5 - Perfect
   
   **Naturalness** (1-5):
   ○ 1 - No one would say this
   ○ 2 - Very unnatural
   ○ 3 - Acceptable but awkward
   ○ 4 - Natural
   ○ 5 - Perfectly natural
   
   **Comments**: [Free text feedback]
   
   **Suggested Correction**: [If not perfect, how would you say it?]
   ```

4. **Review Feedback**
   - Aggregate scores
   - Identify patterns in corrections
   - Prioritize high-impact fixes
   - Update rules and examples

5. **Iterate**
   - Make improvements
   - Re-validate changed items
   - Track improvement over time

### Validation Metrics

```
Native Speaker Validation Score = (
    Average Accuracy + Average Naturalness
) / 2
```

**Target**: ≥ 4.0 / 5.0

### Handling Disagreements

Native speakers may disagree due to:
- **Regional variations**: Different areas have different forms
- **Generational differences**: Younger vs. older speakers
- **Personal preference**: Individual speech patterns
- **Formality level**: Casual vs. formal usage

**Solution**: Document variations
```json
{
  "swedish": "hej",
  "primary_form": "hej",
  "regional_variations": [
    {"region": "Coastal", "form": "hej"},
    {"region": "Inland", "form": "hei"},
    {"region": "Northern", "form": "höj"}
  ],
  "notes": "All forms are correct in their respective regions"
}
```

---

## Test Organization

### Directory Structure

```
tests/
├── unit/
│   ├── test_pronouns.py
│   ├── test_vowel_shifts.py
│   ├── test_apocope.py
│   └── test_consonants.py
├── integration/
│   ├── test_translation_pipeline.py
│   ├── test_rule_combinations.py
│   └── test_full_sentences.py
├── acceptance/
│   ├── test_user_scenarios.py
│   ├── test_conversations.py
│   └── test_real_texts.py
├── regression/
│   ├── test_issue_fixes.py
│   └── test_historical_bugs.py
├── data/
│   ├── test_cases.json
│   ├── validation_sentences.json
│   └── native_speaker_feedback.json
└── utils/
    ├── test_helpers.py
    └── accuracy_check.py
```

### Test Naming Conventions

```python
# Format: test_[component]_[behavior]_[expected_result]

def test_pronoun_jag_converts_to_ja():
    """Test that 'jag' pronoun converts to 'ja'"""
    pass

def test_vowel_e_diphthongizes_in_stem():
    """Test that 'e' becomes 'ei' in stem position"""
    pass

def test_apocope_drops_final_a():
    """Test that final '-a' is dropped from verbs"""
    pass
```

---

## Best Practices

### Do:
- ✅ Write tests BEFORE fixing bugs
- ✅ Test both successful and failure cases
- ✅ Keep tests simple and focused
- ✅ Use descriptive test names
- ✅ Add comments explaining WHY a test exists
- ✅ Run tests frequently during development
- ✅ Seek native speaker validation
- ✅ Document known issues and limitations

### Don't:
- ❌ Test implementation details (test behavior, not code)
- ❌ Make tests dependent on each other
- ❌ Skip tests because "it's obvious"
- ❌ Ignore failing tests
- ❌ Over-optimize test performance (readability > speed)
- ❌ Assume your output is correct without validation
- ❌ Forget to update tests when rules change

---

## Checklist for Release

Before releasing a new dialect version:

### Technical Validation
- [ ] All unit tests pass (100%)
- [ ] All integration tests pass (100%)
- [ ] All acceptance tests pass (≥90%)
- [ ] No regression test failures
- [ ] JSON files validate correctly
- [ ] Code coverage ≥80%
- [ ] No console errors or warnings

### Linguistic Validation
- [ ] IPA notations reviewed
- [ ] Etymology verified for key words
- [ ] Examples are natural and common
- [ ] Regional variations documented
- [ ] Exceptions listed and handled

### Native Speaker Validation
- [ ] At least 50 sentences validated
- [ ] Average accuracy score ≥4.0/5.0
- [ ] Major issues addressed
- [ ] Feedback incorporated
- [ ] Re-validation of changes complete

### Documentation
- [ ] README updated
- [ ] RULES.md complete and accurate
- [ ] EXAMPLES.md has sufficient examples
- [ ] ALPHABET.md has all phonetic information
- [ ] LEARNING-GUIDE.md follows 4-phase structure

### Community
- [ ] Contribution guidelines followed
- [ ] Changes announced in relevant channels
- [ ] Issues and PRs addressed
- [ ] Credits given to contributors

---

## Resources

### Testing Tools
- **pytest**: Python testing framework
- **unittest**: Python standard library
- **Jest**: JavaScript testing (for web apps)
- **GitHub Actions**: CI/CD automation

### Validation Resources
- **Native speaker communities**: Local heritage societies
- **Academic linguists**: University contacts
- **ISOF**: Swedish Language Institute
- **Dialect forums**: Online communities

---

## Conclusion

Quality testing ensures:
1. **Accuracy**: Translations are linguistically correct
2. **Reliability**: System behaves consistently
3. **Trust**: Users can depend on the tool
4. **Maintainability**: Future developers can improve safely

Follow these guidelines to build robust, trustworthy dialect translation systems.

---

**Version**: 1.0  
**Last Updated**: December 2025  
**Maintained by**: Nordic Dialects Preservation Project
