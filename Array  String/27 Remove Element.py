class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k 用來記錄目前有效元素的位置，也就是沒有要刪除的值
        k = 0
        for i in range(len(nums)):
            # 如果 nums[i] 不是要刪除的值，就把它放到前面
            if nums[i] != val:
                nums[k] = nums[i]   # 把非 val 的數字往前放
                k += 1              # 更新有效元素數量（下一個可放位置）
        # 回傳不等於有效元素個數
        return k