class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = m + n - 1
        m = m-1
        n = n-1
        
        while m>-1 or n>-1:
            if m < 0:
                nums1[x] = nums2[n]
                n-=1
            elif n < 0:
                nums1[x] = nums1[m]
                m-=1
            elif nums1[m] > nums2[n]:
                nums1[x] = nums1[m]
                m-=1
            else:
                nums1[x] = nums2[n]
                n-=1
            x-=1

