from collections import Counter

def count_words(words):
    words = "".join([w for w in words if w.isalpha() or w == " " or w == "'"])
    word_count = Counter(words.lower().split())

    return word_count