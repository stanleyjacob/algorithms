def longestCommonPrefix(self, strs: List[str]) -> str:
    i = 0
    prev_let = None

    done_visiting = False
    ret_pref = ''
    while not done_visiting:
        for j in range(len(strs)):

            if done_visiting:
                break

            curr_word = strs[j]
            if prev_let is not None and \
                i < len(curr_word) and \
                prev_let == curr_word[i]:
                continue

            elif prev_let == None and \
                i < len(curr_word):
                prev_let = curr_word[i]

            else:
                done_visiting = True

        if not done_visiting:
            ret_pref += prev_let
        prev_let = None

    return ret_pref
