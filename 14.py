class Solution(object):
    def longestCommonPrefix(self, strs):
        char_index = 0
        keep_going = True
        common_prefix = ''
        char_to_look = ''
        while keep_going and char_index < len(strs[0]):
            char_to_look = strs[0][char_index]
            for word in strs:
                if char_index == len(word):
                    keep_going = False
                    break
                if word[char_index] == char_to_look:
                    pass
                else:
                    keep_going = False
                    break
            char_index += 1
            if keep_going:
                common_prefix += char_to_look
        return common_prefix

teste = Solution()
print(teste.longestCommonPrefix(["ab", "a"]))