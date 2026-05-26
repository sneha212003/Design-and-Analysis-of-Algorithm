# KMP Pattern Searching Algorithm in Python

This project implements the Knuth-Morris-Pratt (KMP) Pattern Searching Algorithm using Python.

The KMP algorithm is an efficient string matching algorithm that avoids unnecessary comparisons by using the LPS (Longest Prefix Suffix) array.

---

## Features

- Efficient pattern searching
- Uses LPS array preprocessing
- Finds all occurrences of pattern
- Measures execution time
- User-friendly input and output

---

## Technologies Used

- Python
- String Matching
- LPS Array
- Time Module

---

## How the Algorithm Works

1. Build the LPS array
2. Compare text and pattern characters
3. Skip unnecessary comparisons using LPS values
4. Find all matching positions efficiently

---

## Example

### Input

```python
Enter text : ABABDABACDABABCABAB
Enter pattern : ABAB
```

### Output

```python
Pattern found at index : 0
Pattern found at index : 10
Pattern found at index : 15

Text Length : 19
Pattern Length : 4
Execution Time : 0.00001
```

---

## Time Complexity

| Case | Complexity |
|------|-------------|
| Best Case | O(n) |
| Average Case | O(n + m) |
| Worst Case | O(n + m) |

Where:
- n = length of text
- m = length of pattern

---

## Applications

- Text Editors
- Search Engines
- DNA Sequence Matching
- Plagiarism Detection
- Data Processing

---

## How to Run

```bash
python kmp_search.py
```

---

## Author

Implementation of KMP Pattern Searching Algorithm using Python.
