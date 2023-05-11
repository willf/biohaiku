import random
import sys

import syllapy


def hello_world(s: str = "Hello World!") -> str:
    """
    Returns the string "Hello World!"

    >>> hello_world()
    'Hello World!'

    >>> hello_world("Hello World!")
    'Hello World!'

    >>> hello_world("Hello World")
    'Hello World'

    """
    return s


def is_acronym(s: str) -> bool:
    """
    Returns True if the string is an acronym

    >>> is_acronym("Hello World!")
    False
    >>> is_acronym("TV")
    True
    >>> is_acronym("T.V.")
    True
    """
    return s.isupper()


def syllable_count(s: str) -> int:
    """
    Returns the number of syllables in a string

    >>> syllable_count("Hello World!")
    3
    >>> syllable_count("Hello TV")
    3
    """
    words = s.split()
    count = 0
    for word in words:
        count += syllable_count_word(word)
    return count


def syllable_count_word(s: str) -> int:
    """
    Returns the number of syllables in a word

    >>> syllable_count_word("Hello")
    2
    >>> syllable_count_word("World")
    1
    """
    if is_acronym(s):
        # remove all non-alphabetic characters
        s2 = [i for i in s if i.isalpha()]
        return len(s2)
    else:
        return syllapy.count(s)


def collect_haiku_sentences(sentences):
    """
    Collects sentences that are haiku candidates
    """
    d = {5: [], 7: []}
    for s in sentences:
        count = syllable_count(s)
        if count in d:
            d[count].append(s)
    return d

def generate_haiku(haiku_dictionary):
    """
    Generates a haiku from a list of sentences
    """
    haiku = []
    d = haiku_dictionary
    haiku.append(random.choice(d[5]))
    haiku.append(random.choice(d[7]))
    haiku.append(random.choice(d[5]))
    return haiku


def generate_haikus(sentences, n = 100):
    """
    Generates a list of haikus from a list of sentences
    """
    haikus = []
    d = collect_haiku_sentences(sentences)
    for i in range(n):
        haikus.append(generate_haiku(d))
    return haikus

if __name__ == "__main__":
    sentences = [l.strip() for l in sys.stdin.readlines()]
    haikus = generate_haikus(sentences)
    for haiku in haikus:
        print("  \n".join(haiku))
        print()
