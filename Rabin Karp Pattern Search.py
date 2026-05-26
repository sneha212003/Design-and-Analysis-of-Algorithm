import time

# Rabin-Karp Pattern Searching Algorithm
def rabin_karp(text, pattern, d=256, q=101):

    n = len(text)
    m = len(pattern)

    # If pattern length is greater than text length
    if m > n:
        return []

    # Hash multiplier
    h = pow(d, m - 1) % q

    # Hash values
    p = 0   # Pattern hash
    t = 0   # Text window hash

    result = []

    # Preprocessing
    # Calculate hash for pattern and first text window
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Slide pattern over text
    for s in range(n - m + 1):

        # If hash values match
        if p == t:

            # Check characters one by one
            if text[s:s + m] == pattern:
                result.append(s)

        # Calculate hash for next window
        if s < n - m:

            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q

            # Convert negative hash to positive
            if t < 0:
                t += q

    return result


# User Input
text = input("Enter the text : ")
pattern = input("Enter the pattern : ")

# Start Time
stime = time.time()

# Function Call
matches = rabin_karp(text, pattern)

# End Time
etime = time.time()

# Output
if matches:
    print("Pattern found at index positions :", matches)
else:
    print("Pattern not found")

# Additional Information
print("Text Length :", len(text))
print("Pattern Length :", len(pattern))

# Execution Time
print("Execution Time :", etime - stime)
