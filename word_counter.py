import sys
counts=dict()

def word_count(str):
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


for line in sys.stdin:
    word_count(line)

print(counts)

