class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # array長度小於等於 2 的話，不需要處理，因為最多保留兩個一樣的值
        if len(nums) <= 2:
            return len(nums)

        # k 代表「下一個可放置有效元素的位置」
        # 前兩個元素一定是有效的（最多保留 2 個）
        k = 2

        # i 從 index 2 開始掃描
        for i in range(2, len(nums)):
            # nums[k-2] 是「有效陣列中倒數第二個數」
            # 若 nums[i] != nums[k-2]，代表不會造成超過兩次
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k