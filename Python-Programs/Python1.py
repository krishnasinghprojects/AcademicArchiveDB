from collections import Counter

filename = input("Enter the filename: ")

with open(filename, "r") as file:
    words = file.read().lower().split()

word_counts = Counter(words)
frequent = word_counts.most_common(5)

print("Most frequent words:")
for word, count in frequent:
    print(word,":",count)