def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    for i in range(len(s), -1, -1):
        for j in range(len(s) - i + 1):
            if s[j:j+i] == s[j:j+i][::-1]:
                return s[j:j+i]
    return ''