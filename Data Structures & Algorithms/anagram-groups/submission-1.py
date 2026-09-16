class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = {}

        for i in strs:
            s = "".join(sorted(i))
            if s in track:
                track[s].append(i)
            else:
                track[s] = [i]
            
        return list(track.values())

strs=["act","pots","tops","cat","stop","hat"]
        