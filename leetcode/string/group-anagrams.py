import collections


class Solution:
    def groupAnagrams(self, strs):
        # defaultdict 사용
        # value를 리스트로 줄 수도 있다.
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()