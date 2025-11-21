class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 核心想法：
        # 題目要求在 nums1 原地（in-place）完成合併，
        # 而 nums1 的前半段有實際資料、後半段是預留空間。
        # 若從前往後放，會覆蓋掉 nums1 尚未比較的值，因此必須「從後往前」合併。
        # 這樣可以確保每次把目前最大的值放到 nums1 的尾端，避免資料遺失。

        # 1. 確認由後往前更新的index
        index = m + n - 1 # index 指向 nums1 最後一個可放置的位置
        pointer_1 = m - 1 # pointer_1 指向 nums1 中待比較的最後一個元素
        pointer_2 = n - 1 # pointer_2 指向 nums2 中待比較的最後一個元素

        # 2. 開始跑loop，當 nums2 還有剩餘元素時，持續合併
        while pointer_2 >= 0:

            # 若 nums1 還有元素未比較完，且 nums1 的當前值比較大
            # 則把 nums1 的值放到 index 位置
            if pointer_1 >= 0 and nums1[pointer_1] > nums2[pointer_2]:
                nums1[index] = nums1[pointer_1]
                pointer_1 -= 1

            # 否則把 nums2 的值放到 index 位置
            else:
                nums1[index] = nums2[pointer_2]
                pointer_2 -= 1

            # 填完值後，將 index 往前移動
            index -= 1