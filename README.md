# NordicVoices: Pitemål (Bondska)
## Authentic Westrobothnian Dialect Engine

> **Current Status:** 🟢 Active (v2.5)
> **Region:** Piteå, Norrbotten/Västerbotten
> **Engine:** Rule-Based (No Dictionary Dependency)

This branch hosts the **Pitemål** dialect preservation project. Pitemål is one of the most distinct varieties of the Westrobothnian (Bondska) dialect group.

---

## 🛠️ Components

### 1. Web Translator (`bondska-translator.html`)
A standalone, cyberpunk-themed web tool that translates Standard Swedish into authentic Pitemål using a sophisticated rule-based engine.
*   **Live Preview:** Drag and drop the HTML file into any browser.
*   **Features:**
    *   **Thick L:** Automatic conversion of *rd/rl/rt* → **L**.
    *   **Apocope:** Authentic dropping of final vowels.
    *   **Smart Suffixes:** Converts *-het*, *-nad*, *-en* to Pitemål forms.
    *   **Grammar Particles:** Handles *men*→*män*, *och*→*å*, etc.

### 2. CLI Tool (`bondska-cli.py`)
A Python command-line interface for batch translation or terminal use.
*   **Usage:** `python3 bondska-cli.py`
*   **Logic:** Mirrors the web engine's rules for consistency.

### 3. Documentation
*   **[ALPHABET.md](ALPHABET.md):** Pitemål-specific phonetic guide (Thick L, Retroflex).
*   **[LEARNING-GUIDE.md](LEARNING-GUIDE.md):** A 4-phase curriculum for learning the dialect.
*   **[EXAMPLES.md](EXAMPLES.md):** 50+ verified translation examples.
*   **[RULES.md](RULES.md):** Detailed breakdown of the linguistic rules used in the engine.

---

## 🧬 How It Works (The Engine)

Unlike simple dictionary swappers, this project uses a **Rule-Based Architecture**. It processes text through a linguistic pipeline:

1.  **Particle Check:** High-frequency function words are swapped first (e.g., *sverige* → *Schwerje*).
2.  **Verb Apocope:** Present tense verbs lose their *-ar/-er* suffix (e.g., *dansar* → *dans*).
3.  **Suffix Transformation:** Morphological endings are adapted (e.g., *osäkerhet* → *osäkerhe*).
4.  **Phonology:** Consonant clusters and vowels are shifted (e.g., *bord* → *boL*).
5.  **Final Apocope:** Remaining final vowels are dropped where appropriate.

---

## 🚀 Next Steps
This branch is now **complete** and serves as the **prototype** for other dialect branches.
*   **Next Dialect:** Värmländska (Rural Värmland)

*Hald fram Pitemålet!*
