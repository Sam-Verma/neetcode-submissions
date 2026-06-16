class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        for word in strs:

            li = [0]*26
            for c in word:
                li[ord(c)-ord('a')]+=1

            hashmap[tuple(li)].append(word)
        
        return [word for word in hashmap.values()]