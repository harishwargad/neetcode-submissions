class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matched = []

        for i in range(len(words)):
            for j in range(len(words)):
                if j == i:
                    continue
                elif words[i] in words[j]:
                    matched.append(words[i])
                    break
        return matched