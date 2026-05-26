# Rabin-Karp Pattern Searching Algorithm in Python

This project implements the Rabin-Karp Pattern Searching Algorithm using Python.

The Rabin-Karp algorithm is an efficient string searching technique that uses hashing to find occurrences of a pattern inside a text.

---

## Features

- Searches for a pattern inside a text
- Uses rolling hash technique
- Returns all matching index positions
- Measures execution time
- User-friendly input and output

---

## Technologies Used

- Python
- Hashing Technique
- Rolling Hash Algorithm
- Time Module

---

## How the Algorithm Works

1. Calculate hash value for the pattern
2. Calculate hash value for the first window of text
3. Compare hash values
4. If hashes match, compare characters
5. Slide the window and update hash efficiently

---

## Example

### Input

```python
Enter the text : ABABDABACDABABCABAB
Enter the pattern : ABAB
```

### Output

```python
Pattern found at index positions : [0, 10, 15]
Text Length : 19
Pattern Length : 4
Execution Time : 0.00001
```

---

## Time Complexity

| Case | Complexity |
|------|-------------|
| Best/Average Case | O(n + m) |
| Worst Case | O(n × m) |

Where:
- n = length of text
- m = length of pattern

---

## Applications

- Plagiarism Detection
- Search Engines
- DNA Sequence Matching
- Virus Detection
- Text Processing

---

## How to Run

```bash
python rabin_karp.py
```

---

## Author

Implementation of Rabin-Karp Algorithm using Python for pattern searching and performance analysis.
