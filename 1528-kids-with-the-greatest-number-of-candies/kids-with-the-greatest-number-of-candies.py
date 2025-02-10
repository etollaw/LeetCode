class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        min_val = max_val - extraCandies
        newlist = []
        for num in candies:
            if num >= min_val:
                newlist.append(True)
            else:
                newlist.append(False)
        return newlist