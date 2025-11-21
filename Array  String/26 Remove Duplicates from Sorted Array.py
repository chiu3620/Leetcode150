class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 如果是空array，直接回傳 0
        if len(nums) == 0:
            return 0

        # k 是「下一個要放入不同數字」的位置
        # nums[0] 一定是要保留的，所以從 1 開始
        k = 1
        for i in range(1, len(nums)):
            # 因為array是有排序的
            # 所以如果當前元素不等於前一個有效元素
            # 表示遇到新的不同元素，應該保留
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        # k 就是去除重複後的長度
        return k