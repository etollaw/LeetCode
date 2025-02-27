class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Strip leading and trailing spaces
        s = s.strip()
        print(s)
        # Step 2: Split the string into words, ignoring extra spaces
        words = s.split()
        print(s)
        # Step 3: Reverse the list of words
        words.reverse()
        print(s)
        # Step 4: Join the reversed words with a single space and return the result
        return ' '.join(words)