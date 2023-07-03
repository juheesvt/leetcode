class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        answer = ""
        conti = True
        end_idx = min([len(str) for str in strs])

        for i in range(end_idx):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    conti = False
                    break
            else:
                answer += strs[0][i]

            if not conti:
                break

        return answer
