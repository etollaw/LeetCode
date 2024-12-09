class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
 
        k = 0
        # Keep checking for k + 1 repetitions of word in sequence
        while word * (k + 1) in sequence:
            k += 1
        return k
