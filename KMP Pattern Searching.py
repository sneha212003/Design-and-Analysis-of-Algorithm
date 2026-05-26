import time

# Function to perform KMP Search
def KMPSearch(pat, txt):

    m = len(pat)
    n = len(txt)

    # Create LPS array
    lps = [0] * m

    j = 0

    # Compute LPS array
    computeLPSArray(pat, m, lps)

    found = False

    i = 0

    while i < n:

        # Match characters
        if pat[j] == txt[i]:
            i += 1
            j += 1

        # Pattern found
        if j == m:
            print("Pattern found at index :", i - j)
            found = True

            j = lps[j - 1]

        # Mismatch after j matches
        elif i < n and pat[j] != txt[i]:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    if not found:
        print("Pattern not found")


# Function to compute LPS array
def computeLPSArray(pat, m, lps):

    length = 0

    lps[0] = 0

    i = 1

    while i < m:

        if pat[i] == pat[length]:

            length += 1

            lps[i] = length

            i += 1

        else:

            if length != 0:
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1


# User Input
txt = input("Enter text : ")
pat = input("Enter pattern : ")

# Start Time
stime = time.time()

# Function Call
KMPSearch(pat, txt)

# End Time
etime = time.time()

# Additional Information
print("Text Length :", len(txt))
print("Pattern Length :", len(pat))

# Execution Time
print("Execution Time :", etime - stime)
