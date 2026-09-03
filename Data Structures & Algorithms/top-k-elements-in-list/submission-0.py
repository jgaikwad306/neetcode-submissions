class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map ={}
        ans = []
        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1
        for x in range(k):
            max_key = max(nums_map, key=nums_map.get)
            ans.append(max_key)
            nums_map.pop(max_key)
        return ans
        
        
        
        