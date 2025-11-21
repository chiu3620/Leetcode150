class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 解題思路：
        # 透過2 bit的方式表示在同一個格子同時呈現新舊狀態
        # 0代表死，1代表活
        # 第1個bit表示原本的狀態
        # 第2個bit表示更新後的狀態
        # 00 -> 0：新死，舊死
        # 01 -> 1：新死，舊活
        # 10 -> 2：新活，舊死
        # 11 -> 3：新活，舊活

        # m: row 數, n: col 數
        m, n = len(board), len(board[0])

        # 八個方向：上、下、左、右、四個斜角
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # 1. 根據「舊狀態」計算「新狀態」
        for i in range(m):
            for j in range(n):
                live_neighbors = 0

                # 計算 (i, j) 周圍 8 個鄰居目前有幾個是活的
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    # 檢查是否有超出邊界，注意python的index是從0開始
                    if 0 <= x < m and 0 <= y < n:
                        # 如果格子為1 or 3
                        # 表示舊狀態是活細胞
                        if board[x][y] in [1, 3]:
                            live_neighbors += 1

                # 確認目前這一格的舊狀態
                # 因為還沒有更新過，所以0代表死，1代表活
                curr = board[i][j]

                # 根據規則決定下一代是否為活細胞
                # 如果當前是活細胞
                if curr == 1:
                    # 活鄰居為 2 或 3 個才能活下來
                    if live_neighbors == 2 or live_neighbors == 3:
                        new_state = 1
                    else:
                        new_state = 0
                # 如果當前是死細胞
                else:
                    # 剛好有 3 個活鄰居會復活
                    if live_neighbors == 3:
                        new_state = 1
                    else:
                        new_state = 0

                # 如果更新後是活細胞的，第2個bit就是變成1
                # 原值 00 or 01 變成 10 or 11
                # 二進位10換算成十進位就是2
                # 也就是代表將原本的數值加2
                if new_state == 1:
                    board[i][j] += 2

        # 2. 更新成新狀態
        # 00 -> 0：新死，舊死，不用處理，保持0
        # 01 -> 1：新死，舊活，更新成0
        # 10 -> 2：新活，舊死，更新成1
        # 11 -> 3：新活，舊活，更新成1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] in [2, 3]:
                     board[i][j] = 1
