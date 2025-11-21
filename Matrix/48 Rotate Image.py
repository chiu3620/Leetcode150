class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 解題思路：
        # 透過觀察，我們可以發現旋轉 90 度後
        # 會讓第一個column的值移動到第一個row上
        # 會讓第i個column的值移動到第i個row上
        # 但數值的排列卻是相反的

        # 所以我們第一步就可以透過轉置矩陣的方式
        # 將第i個column的值移動到第i個row上
        # 再將每個row的順序反轉

        n = len(matrix)

        # 1. 轉置矩陣
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. 將每個row的順序反轉
        for i in range(n):
            matrix[i].reverse()