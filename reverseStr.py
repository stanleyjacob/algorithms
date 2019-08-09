class Solution:
    def reverseString(self, arr: List[str]) -> None:
        """
        modifies arr in-place
        """
        i = 0
        j = len(s) - 1
        while i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
