class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 解題思路：
        # 如果一個數字n是連續數列的起點，就表示 n-1 不存在 

        # 將nums存成 set 中讓查詢速度變成 O(1)
        num_set = set(nums)
        longest = 0

        # 逐一檢查每個數字是否是「連續序列的起點」
        for n in num_set:
            # 若 n-1 不在集合中，代表 n 是這段序列的第一個數字
            # 若 n-1 存在，代表 n 會被前面的序列處理，不需要重複計算
            if n - 1 not in num_set:
                # 因為序列必定包含 n 自己，所以長度至少是1
                length = 1

                # 依序往上找，確認更大的值是否存在，n+1、n+2、n+3...
                while n + length in num_set:
                    length += 1

                # 更新目前最長的連續序列長度
                longest = max(longest, length)

        return longest
