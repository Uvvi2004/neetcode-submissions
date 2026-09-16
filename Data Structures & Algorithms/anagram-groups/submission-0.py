class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        track = {}

        for i in strs:
            if ''.join(sorted(i)) in track:
                track[''.join(sorted(i))].append(i)
            else:
                track[''.join(sorted(i))] = [i]
        
        return list(track.values())