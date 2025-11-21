class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 使用 Counter 計算每個元素出現次數
        count = collections.Counter(nums)

        # 目標是要找到出現次數大於 n/2 的元素
        target = len(nums)//2

        # 遍歷每個元素及其出現次數
        for num, appear in count.items():
            # 題目保證一定存在答案
            # 如果出現次數大於 n/2，就表示找到答案了
            if appear > target:
                return num