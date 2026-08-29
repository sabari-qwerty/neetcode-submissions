class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for i in nums:

            freq[i] = freq.get(i, 0) + 1


        freqbucekt = {}

        max_value = 0 


        for key, value in freq.items():

            max_value = max(value, max_value)

            if value in freqbucekt: 
                freqbucekt[value].append(key)
            else: 
                freqbucekt[value] = [key]

        ans = []

        print(freqbucekt)

        for i in range(max_value, 0, -1): 

            if i in freqbucekt:
                ans.extend(freqbucekt[i])

        return ans[:k]