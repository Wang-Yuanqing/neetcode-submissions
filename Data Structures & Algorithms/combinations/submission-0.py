class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 保存所有完整组合
        path = []    # 当前正在构造的组合

        def dfs(start):
            # 已经选够 k 个数：保存这个组合
            if len(path) == k:
                result.append(path.copy())
                return

            # 下一位可以从 start 一直选到 n
            for num in range(start, n + 1):
                path.append(num)  # 选当前数字
                dfs(num + 1)      # 继续选择后面的数字
                path.pop()        # 撤销当前选择，准备换下一个数字

        dfs(1)
        return result