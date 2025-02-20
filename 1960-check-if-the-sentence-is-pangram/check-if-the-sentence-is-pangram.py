class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        set1 = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
        set2 = set()

        for char in sentence:
            if char not in set2:
                set2.add(char)

        return set1 == set2