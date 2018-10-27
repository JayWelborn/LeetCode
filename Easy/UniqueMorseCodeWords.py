class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        letters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                   ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                   "...","-","..-","...-",".--","-..-","-.--","--.."]

        morse_words = []
        for word in words:
            morse_word = []
            for c in word:
                morse_word.append(letters[ord(c) - 97])
            morse_words.append(''.join(morse_word))
                
        return len(set(morse_words))
