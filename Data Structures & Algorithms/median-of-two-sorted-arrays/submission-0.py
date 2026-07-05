class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        if len(nums2) < len(nums1):
            B,A = A,B
        
        plength = (len(nums1) + len(nums2)) // 2
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = plength - i - 2

            #handle out of bounds
            ALeft = A[i] if i >= 0 else float("-infinity")
            ARight = A[i + 1] if i + 1 < len(A) else float("infinity")
            BLeft = B[j] if j >= 0 else float("-infinity")
            BRight = B[j + 1] if j + 1 < len(B) else float("infinity")

            if (ALeft <= BRight and BLeft <= ARight):
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return min(ARight, BRight)
                else:
                    return (max(ALeft,BLeft) + min(ARight,BRight)) / 2
            if (ALeft > BRight):
                r = i - 1
            else:
                l = i + 1