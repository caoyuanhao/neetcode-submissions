class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dist = {c: i for i, c in enumerate(order)}
        
        def translate(word):
            return [dist[c] for c in word]
        
        translated = [translate(word) for word in words]
        return translated == sorted(translated)