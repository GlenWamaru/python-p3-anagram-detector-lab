class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        anagrams = []
        for w in words:
            # Convert both words to lowercase for case-insensitive comparison
            w_lower = w.lower()
            # Check if the word is not the same as the initialized word and if it's an anagram
            if w_lower != self.word and self.is_anagram(w_lower):
                anagrams.append(w)
        return anagrams

    def is_anagram(self, other_word):
        # Check if the sorted letters of both words are equal
        return sorted(self.word) == sorted(other_word)
