## 🧩 Word Ladder Game
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-brightgreen)
![NLTK](https://img.shields.io/badge/WordCheck-WordNet-yellow)

This is a classic **Word Ladder puzzle game** built with **Python Tkinter** and validated using **NLTK's WordNet** dictionary.

### 🎮 Game Objective
Transform a **4-letter start word** into a given **4-letter end word**, by entering exactly **4 intermediate valid English words**.  
Each step must:
- Change **only one letter**
- Be a **real English word**
- Be exactly **4 letters**
- **No repeats** allowed

You win when you successfully complete the 6-step ladder with valid transitions.

### 🛠 Features
- Clean GUI using only `tkinter`
- Valid English word checking using `nltk.corpus.wordnet`
- Random start & end word pairs on each game/reset
- Entry validation: length, dictionary check, and letter-difference
- Ladder visualization with vertical and horizontal lines
- Keyboard Enter support for quick submission
- Restart button to replay with a new challenge

### 📦 Requirements
- Python 3.x
- `nltk` (only for WordNet validation)

### 🔧 To Run
1. Install NLTK (only once):
    ```bash
    pip install nltk
    ```
2. Download WordNet (only once in your script or setup):
    ```python
    import nltk
    nltk.download('wordnet')
    ```
   ```python
    import nltk
    nltk.download('word')
    ```
3. Run the game:
    ```bash
    Word Ladder.py
    ```
